#!/usr/bin/env python3
"""Collect merged PRs, releases and direct-to-default-branch commits from the
repositories listed in config/repositories.yml, and append them to the
monthly devlog files under logs/YYYY/YYYY-MM.md.

The monthly files are the canonical record. logs/today.md,
logs/yesterday.md and logs/latest.md are read-only convenience views
regenerated from them on every run (see "Daily views" / "Latest view" below).

Design notes:
  - Standard library only (urllib, json, re, datetime). This script runs on
    every GitHub Actions run, so it deliberately avoids extra dependencies
    (no PyYAML, no requests) to keep CI fast and dependency-free.
  - Deduplication does not rely on a separate state file. Each event's
    GitHub URL is embedded in the rendered log line, and that same URL is
    used as the dedup marker: before adding an event we check whether its
    URL already appears in the target month file. This keeps logs/ as the
    single source of truth (self-healing if a run is skipped or a line is
    edited by hand) instead of a state file that can drift out of sync.
  - A lookback window (LOOKBACK_DAYS) bounds how far back each run looks,
    so a daily cron only ever re-scans a small, recent slice of history. It
    can be overridden per-run (e.g. for a one-off historical backfill) via
    the DEVLOG_LOOKBACK_DAYS environment variable / workflow_dispatch input.
  - devlog is one of the repositories it collects, so its own log commit is
    skipped as a direct commit; see SELF_AUTO_COMMIT_SUBJECT below.
  - Listing commits, pull requests and releases uses the REST API. The one
    exception is deciding which commits already belong to a merged pull
    request: asking REST costs one request per commit, so that single
    question is asked for a batch of commits at a time over GraphQL.
  - Every run prints per-repository timings and API request counts, so a run
    that gets slow can be diagnosed from the workflow log alone.
  - GitHub timestamps are UTC. Log entries are dated by Japan Standard Time
    (JST), since this is a development *diary* meant to read naturally for
    a JST-based team: an event just after midnight JST should land on that
    JST day, not the previous UTC day. JST is a fixed UTC+9 offset with no
    DST, so a plain `timezone(timedelta(hours=9))` is used instead of
    `zoneinfo.ZoneInfo("Asia/Tokyo")` - the latter depends on the IANA tz
    database being installed on the host OS (fine on GitHub Actions' Ubuntu
    runners, but not guaranteed e.g. on Windows), and a fixed offset needs
    no such external data.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "repositories.yml"
LOGS_DIR = ROOT / "logs"

API_ROOT = "https://api.github.com"
GRAPHQL_URL = f"{API_ROOT}/graphql"
LOOKBACK_DAYS = 7  # the cron runs daily; a week of overlap is plenty of slack

# How many commits are resolved per GraphQL request when deciding which ones
# belong to a merged PR. Each commit in the query pulls up to
# ASSOCIATED_PRS_PER_COMMIT pull request nodes, so the batch size trades query
# size (and GitHub's node limit) against the number of round trips; 30 x 30
# nodes is comfortably inside the limits while turning a week of commits in a
# busy repository into one or two requests.
COMMITS_PER_GRAPHQL_BATCH = 30
ASSOCIATED_PRS_PER_COMMIT = 30  # matches the REST endpoint's default page size
JST = timezone(timedelta(hours=9))

# devlog collects itself, so the workflow's own log commit would come back as a
# direct commit on the next run and keep re-triggering the workflow. That one
# commit is skipped - matched on this repository *and* this exact subject, so a
# same-named commit in any other repository is still recorded normally. Keep
# SELF_AUTO_COMMIT_SUBJECT in sync with the commit message in
# .github/workflows/collect.yml.
SELF_REPO = "YanTKYS/devlog"
SELF_AUTO_COMMIT_SUBJECT = "chore(logs): update devlog entries"

API_REQUEST_COUNT = 0  # for the timing summary printed by main()
PAGINATION_SAFETY_MAX_PAGES = 200  # backstop only; fetch functions normally
                                    # stop earlier once they pass `since`


class GitHubError(RuntimeError):
    pass


# ---------------------------------------------------------------------------
# config/repositories.yml loading
# ---------------------------------------------------------------------------


def load_repositories(path: Path = CONFIG_PATH) -> list[str]:
    """Parse the `repositories:\n  - owner/repo` list from repositories.yml.

    Hand-rolled on purpose: the config format is a flat list under a single
    top-level key, so pulling in a YAML library for this alone isn't worth
    the dependency.
    """
    repos: list[str] = []
    in_list = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        is_indented_or_item = raw_line[:1].isspace() or raw_line.lstrip().startswith("-")
        if not is_indented_or_item:
            in_list = line.strip() == "repositories:"
            continue
        if in_list:
            m = re.match(r"^\s*-\s*(.+)$", line)
            if m:
                value = m.group(1).strip().strip("'\"")
                if value:
                    repos.append(value)
    return repos


# ---------------------------------------------------------------------------
# GitHub API access
# ---------------------------------------------------------------------------


def api_request(path: str, token: str | None, params: dict | None = None):
    url = path if path.startswith("http") else f"{API_ROOT}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    global API_REQUEST_COUNT
    for attempt in range(2):
        API_REQUEST_COUNT += 1
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (403, 502, 503) and attempt == 0:
                time.sleep(2)
                continue
            body = e.read().decode("utf-8", "replace")
            raise GitHubError(f"GET {url} -> {e.code}: {body[:300]}") from e


def graphql_request(query: str, variables: dict, token: str | None):
    """POST one GraphQL query, using the same token as the REST calls.

    GraphQL needs authentication even for public data, so an unauthenticated
    run cannot use it - the caller turns that into a warning rather than
    silently reporting fewer direct commits.
    """
    if not token:
        raise GitHubError(
            "GraphQL requires authentication; set DEVLOG_READ_TOKEN (or GITHUB_TOKEN)"
        )

    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(GRAPHQL_URL, data=body, method="POST")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {token}")

    global API_REQUEST_COUNT
    for attempt in range(2):
        API_REQUEST_COUNT += 1
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            if e.code in (403, 502, 503) and attempt == 0:
                time.sleep(2)
                continue
            detail = e.read().decode("utf-8", "replace")
            raise GitHubError(f"POST {GRAPHQL_URL} -> {e.code}: {detail[:300]}") from e

    # A GraphQL error arrives with HTTP 200 and (possibly partial) data; treat
    # it as a failure rather than reading an incomplete answer as "no PR".
    if payload.get("errors"):
        messages = "; ".join(str(err.get("message", err)) for err in payload["errors"])
        raise GitHubError(f"GraphQL error: {messages[:300]}")
    return payload.get("data") or {}


def paginate(
    path: str,
    token: str | None,
    params: dict | None = None,
    max_pages: int = PAGINATION_SAFETY_MAX_PAGES,
):
    """Yield items across all pages.

    There is no small fixed page cap here: callers that only want a bounded
    time range (e.g. "events since X") are expected to stop consuming the
    generator (via `break`) once they see an item older than their cutoff,
    which is what every fetch_* function below does. `max_pages` is only a
    safety backstop against unbounded pagination (e.g. `since` not being
    reached because a repo has more history than any caller expected); if
    it is hit, a warning is printed so an incomplete backfill is never
    silent.
    """
    params = dict(params or {})
    params.setdefault("per_page", 100)
    page = 1
    while page <= max_pages:
        data = api_request(path, token, {**params, "page": page})
        if not data:
            return
        for item in data:
            yield item
        if len(data) < params["per_page"]:
            return
        page += 1
    print(
        f"warning: pagination safety limit ({max_pages} pages) reached for {path}; "
        "results may be incomplete - consider narrowing lookback_days",
        file=sys.stderr,
    )


def parse_dt(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def to_jst_date(dt: datetime) -> str:
    """Log entries are dated by JST local date, not the raw UTC date."""
    return dt.astimezone(JST).date().isoformat()


# ---------------------------------------------------------------------------
# Event collection
# ---------------------------------------------------------------------------


def fetch_merged_prs(owner: str, repo: str, token: str | None, since: datetime) -> list[dict]:
    events = []
    for pr in paginate(
        f"/repos/{owner}/{repo}/pulls",
        token,
        {"state": "closed", "sort": "updated", "direction": "desc"},
    ):
        if parse_dt(pr["updated_at"]) < since:
            break  # sorted by updated desc: everything after this is older
        if not pr.get("merged_at"):
            continue
        merged_at = parse_dt(pr["merged_at"])
        if merged_at < since:
            continue
        events.append(
            {
                "type": "pr",
                "date": to_jst_date(merged_at),
                "repo": repo,
                "number": pr["number"],
                "title": pr["title"],
                "url": pr["html_url"],
            }
        )
    return events


def fetch_releases(owner: str, repo: str, token: str | None, since: datetime) -> list[dict]:
    events = []
    for rel in paginate(f"/repos/{owner}/{repo}/releases", token):
        if rel.get("draft"):
            continue
        published = rel.get("published_at") or rel.get("created_at")
        if not published:
            continue
        published_dt = parse_dt(published)
        if published_dt < since:
            break  # releases are returned newest-first
        events.append(
            {
                "type": "release",
                "date": to_jst_date(published_dt),
                "repo": repo,
                "tag": rel.get("tag_name") or "release",
                "name": rel.get("name") or "",
                "url": rel["html_url"],
            }
        )
    return events


def is_self_log_commit(owner: str, repo: str, subject: str) -> bool:
    """True for the log commit this repository's own workflow pushes."""
    return f"{owner}/{repo}" == SELF_REPO and subject == SELF_AUTO_COMMIT_SUBJECT


def build_associated_prs_query(count: int) -> str:
    """A query asking, for `count` commits of one repository, whether each has
    an associated pull request that was merged.

    One aliased `object(oid: ...)` field per commit (c0, c1, ...), with the
    SHAs passed as variables rather than interpolated into the query text.
    Only `merged` is requested: whether to skip the commit is the only thing
    the caller decides.
    """
    var_defs = ", ".join(f"$s{i}: GitObjectID!" for i in range(count))
    fields = "\n".join(
        f"    c{i}: object(oid: $s{i}) {{ ... on Commit {{ "
        f"associatedPullRequests(first: {ASSOCIATED_PRS_PER_COMMIT}) {{ nodes {{ merged }} }} }} }}"
        for i in range(count)
    )
    return (
        f"query($owner: String!, $name: String!, {var_defs}) {{\n"
        f"  repository(owner: $owner, name: $name) {{\n{fields}\n  }}\n}}"
    )


def fetch_shas_in_merged_prs(
    owner: str, repo: str, token: str | None, shas: list[str]
) -> set[str]:
    """Of `shas`, the ones that belong to a merged pull request.

    This replaces the old per-commit REST call to
    /repos/{owner}/{repo}/commits/{sha}/pulls: the same question is asked for
    COMMITS_PER_GRAPHQL_BATCH commits at a time, so the number of requests no
    longer grows with the number of commits. An empty list asks nothing.
    """
    in_merged_pr: set[str] = set()
    for start in range(0, len(shas), COMMITS_PER_GRAPHQL_BATCH):
        batch = shas[start : start + COMMITS_PER_GRAPHQL_BATCH]
        variables = {"owner": owner, "name": repo}
        variables.update({f"s{i}": sha for i, sha in enumerate(batch)})
        data = graphql_request(build_associated_prs_query(len(batch)), variables, token)

        repository = data.get("repository") or {}
        for i, sha in enumerate(batch):
            commit_node = repository.get(f"c{i}") or {}
            nodes = (commit_node.get("associatedPullRequests") or {}).get("nodes") or []
            if any(pr.get("merged") for pr in nodes):
                in_merged_pr.add(sha)
    return in_merged_pr


def fetch_direct_commits(owner: str, repo: str, token: str | None, since: datetime) -> list[dict]:
    # No `sha` parameter and no /repos/{owner}/{repo} lookup to find one: the
    # commits API already defaults to the repository's default branch.
    since_param = since.strftime("%Y-%m-%dT%H:%M:%SZ")

    candidates = []
    for commit in paginate(
        f"/repos/{owner}/{repo}/commits",
        token,
        {"since": since_param},
    ):
        commit_info = commit.get("commit", {})
        message = commit_info.get("message") or ""
        first_line = message.splitlines()[0] if message else ""
        date_field = (commit_info.get("committer") or commit_info.get("author") or {}).get("date")
        if not date_field:
            continue
        if is_self_log_commit(owner, repo, first_line):
            continue  # excluded before the query below, so it costs no request

        candidates.append(
            {
                "type": "commit",
                "date": to_jst_date(parse_dt(date_field)),
                "repo": repo,
                "short_sha": commit["sha"][:7],
                "message": first_line,
                "url": commit["html_url"],
                "_sha": commit["sha"],
            }
        )

    # Whether each candidate belongs to a merged PR is asked in batches, not
    # once per commit. Commit messages are never used for this: a commit is
    # skipped only because GitHub reports a merged PR containing it.
    in_merged_pr = fetch_shas_in_merged_prs(owner, repo, token, [c["_sha"] for c in candidates])
    return [
        {k: v for k, v in c.items() if k != "_sha"}
        for c in candidates
        if c["_sha"] not in in_merged_pr
    ]


# Ordered as they run, with the label used in the per-repository timing report.
FETCH_STEPS = (
    ("merged PRs", fetch_merged_prs),
    ("releases", fetch_releases),
    ("direct commits", fetch_direct_commits),
)


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------


def render_entry(event: dict) -> str:
    if event["type"] == "pr":
        return "\n".join(
            [
                f"- PR #{event['number']} {event['title']}".rstrip(),
                "  - merged",
                f"  - {event['url']}",
            ]
        )
    if event["type"] == "release":
        title = f"Release {event['tag']}"
        if event["name"] and event["name"] != event["tag"]:
            title += f" ({event['name']})"
        return "\n".join([f"- {title}", "  - release", f"  - {event['url']}"])
    # direct commit
    suffix = f" {event['message']}" if event["message"] else ""
    return "\n".join(
        [
            f"- Commit `{event['short_sha']}`{suffix}".rstrip(),
            "  - direct commit",
            f"  - {event['url']}",
        ]
    )


def marker_for(event: dict) -> str:
    return event["url"]


# ---------------------------------------------------------------------------
# Monthly log file: parse -> merge -> serialize
# ---------------------------------------------------------------------------

_DATE_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$")
_REPO_RE = re.compile(r"^### (.+?)\s*$")
_ENTRY_START_RE = re.compile(r"^- ")
_MONTH_HEADER_RE = re.compile(r"^# \d{4}-\d{2}\s*$")


def parse_month_file(text: str) -> dict[str, dict[str, list[str]]]:
    """Return {date: {repo: [entry_text, ...]}} preserving entry content."""
    sections: dict[str, dict[str, list[str]]] = {}
    cur_date: str | None = None
    cur_repo: str | None = None
    cur_entry_lines: list[str] = []

    def flush():
        nonlocal cur_entry_lines
        if cur_entry_lines and cur_date and cur_repo:
            sections.setdefault(cur_date, {}).setdefault(cur_repo, []).append(
                "\n".join(cur_entry_lines)
            )
        cur_entry_lines = []

    for line in text.splitlines():
        if _MONTH_HEADER_RE.match(line):
            continue
        date_m = _DATE_RE.match(line)
        if date_m:
            flush()
            cur_date, cur_repo = date_m.group(1), None
            continue
        repo_m = _REPO_RE.match(line)
        if repo_m:
            flush()
            cur_repo = repo_m.group(1)
            continue
        if _ENTRY_START_RE.match(line):
            flush()
            cur_entry_lines = [line]
            continue
        if cur_entry_lines:
            cur_entry_lines.append(line)
    flush()
    return sections


def serialize_month_file(month: str, sections: dict[str, dict[str, list[str]]]) -> str:
    lines = [f"# {month}", ""]
    for date in sorted(sections):
        lines.append(f"## {date}")
        lines.append("")
        for repo in sorted(sections[date]):
            lines.append(f"### {repo}")
            lines.append("")
            for entry in sections[date][repo]:
                lines.append(entry)
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def month_path(date_str: str) -> Path:
    year, month, _ = date_str.split("-")
    return LOGS_DIR / year / f"{year}-{month}.md"


def add_events_to_logs(events: list[dict]) -> list[Path]:
    changed_files: list[Path] = []
    parsed_cache: dict[Path, dict] = {}
    raw_cache: dict[Path, str] = {}

    for event in sorted(events, key=lambda e: (e["date"], e["repo"], e["type"])):
        path = month_path(event["date"])
        if path not in raw_cache:
            raw_cache[path] = path.read_text(encoding="utf-8") if path.exists() else ""
            parsed_cache[path] = parse_month_file(raw_cache[path])

        marker = marker_for(event)
        if marker in raw_cache[path]:
            continue  # already recorded

        sections = parsed_cache[path]
        sections.setdefault(event["date"], {}).setdefault(event["repo"], []).append(
            render_entry(event)
        )
        raw_cache[path] += f"\n{marker}\n"  # keep in-run dedup consistent
        if path not in changed_files:
            changed_files.append(path)

    for path in changed_files:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(serialize_month_file(path.stem, parsed_cache[path]), encoding="utf-8")

    return changed_files


# ---------------------------------------------------------------------------
# Daily views: logs/today.md and logs/yesterday.md
# ---------------------------------------------------------------------------
#
# These two files are *derived* views, never a source of truth: the monthly
# files under logs/YYYY/ remain canonical, and each run rewrites today.md /
# yesterday.md from scratch out of them (no appending, no merging). They are
# regenerated on every run - not only when new events arrive - because "today"
# and "yesterday" move even on days where nothing was collected.

TODAY_PATH = LOGS_DIR / "today.md"
YESTERDAY_PATH = LOGS_DIR / "yesterday.md"
AUTOGEN_NOTICE = "<!-- このファイルは自動生成されます。手で編集しないでください。 -->"
NO_ENTRIES_TEXT = "記録はありません。"


def render_daily_view(heading: str, date_str: str) -> str:
    """Render the single `## <date_str>` section of its month file as a page.

    The month file is resolved from the date itself, so month and year
    boundaries need no special casing (2027-01-01's "yesterday" reads
    logs/2026/2026-12.md).
    """
    path = month_path(date_str)
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    day = parse_month_file(text).get(date_str, {})

    lines = [AUTOGEN_NOTICE, "", f"# {heading} - {date_str}", ""]
    if not day:
        lines.append(NO_ENTRIES_TEXT)
    else:
        for repo in sorted(day):
            lines.append(f"### {repo}")
            lines.append("")
            for entry in day[repo]:
                lines.append(entry.rstrip())
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_daily_views(now: datetime | None = None) -> list[Path]:
    """(Re)generate logs/today.md and logs/yesterday.md. Returns changed files."""
    today = (now or datetime.now(timezone.utc)).astimezone(JST).date()
    targets = [
        (TODAY_PATH, "Today", today.isoformat()),
        (YESTERDAY_PATH, "Yesterday", (today - timedelta(days=1)).isoformat()),
    ]

    changed: list[Path] = []
    for path, heading, date_str in targets:
        content = render_daily_view(heading, date_str)
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue  # byte-identical: leave the file alone so no empty commit
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        changed.append(path)
    return changed


# ---------------------------------------------------------------------------
# Latest view: logs/latest.md
# ---------------------------------------------------------------------------
#
# A whole-fleet overview: one row per repository listed in
# config/repositories.yml, showing the most recent event devlog has already
# collected for it. Like the daily views this is derived - it reads only
# repositories.yml and the monthly logs, never the GitHub API, so it says
# "latest as recorded in devlog", not "latest on GitHub right now".
#
# Entries are read back with parse_month_file() (the same parser the monthly
# files are written through) and then split into their fields by inverting
# render_entry(); the marker line (`merged` / `release` / `direct commit`) is
# what identifies the event type.

LATEST_PATH = LOGS_DIR / "latest.md"
NO_RECORD_TEXT = "記録なし"

_MONTH_STEM_RE = re.compile(r"^\d{4}-\d{2}$")
_ENTRY_PR_RE = re.compile(r"^- PR (#\d+(?: .*)?)$")
_ENTRY_RELEASE_RE = re.compile(r"^- Release (.*)$")
_ENTRY_COMMIT_RE = re.compile(r"^- Commit (`[0-9a-f]+`(?: .*)?)$")
_ENTRY_KIND_RE = re.compile(r"^  - (merged|release|direct commit)\s*$")
_ENTRY_URL_RE = re.compile(r"^  - (https?://\S+)\s*$")

_KIND_LABELS = {"merged": "PR", "release": "Release", "direct commit": "direct commit"}


def iter_month_files() -> list[Path]:
    """All logs/YYYY/YYYY-MM.md files, oldest first.

    Deliberately a plain glob over logs/: at devlog's scale (a handful of
    month files) reading them all is cheap, and it avoids an index or state
    file that could drift away from the logs themselves.
    """
    return sorted(
        p
        for p in LOGS_DIR.glob("*/*.md")
        if _MONTH_STEM_RE.match(p.stem) and p.parent.name == p.stem[:4]
    )


def parse_log_entry(entry: str) -> dict:
    """Split a rendered log entry back into {kind, label, url}.

    The inverse of render_entry(). Anything that doesn't match (e.g. a
    hand-written line) still yields a usable row rather than being dropped.
    """
    lines = entry.strip().splitlines()
    first = lines[0] if lines else ""
    kind, url = "", None
    for line in lines[1:]:
        kind_m = _ENTRY_KIND_RE.match(line)
        if kind_m:
            kind = kind_m.group(1)
        url_m = _ENTRY_URL_RE.match(line)
        if url_m:
            url = url_m.group(1)

    for regex in (_ENTRY_PR_RE, _ENTRY_RELEASE_RE, _ENTRY_COMMIT_RE):
        m = regex.match(first)
        if m:
            label = m.group(1).strip()
            break
    else:
        label = first[2:].strip() if first.startswith("- ") else first.strip()

    return {"kind": _KIND_LABELS.get(kind, kind or "-"), "label": label, "url": url}


def collect_latest_events() -> dict[str, dict]:
    """Return {repo_name: {"date": ..., "entry": ...}} across every month file.

    "Latest" is the event on the newest JST date recorded for that repo. The
    monthly logs carry no intra-day time, so when a repo has several entries
    on that date the last one recorded is used.
    """
    latest: dict[str, dict] = {}
    for path in iter_month_files():
        sections = parse_month_file(path.read_text(encoding="utf-8"))
        for date, repos in sections.items():
            for repo, entries in repos.items():
                if not entries:
                    continue
                if repo not in latest or date > latest[repo]["date"]:
                    latest[repo] = {"date": date, "entry": entries[-1]}
    return latest


def _cell(text: str) -> str:
    """Escape what would otherwise break a Markdown table cell / link text."""
    return text.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def render_latest_view(repositories: list[str], latest: dict[str, dict]) -> str:
    lines = [
        AUTOGEN_NOTICE,
        "",
        "# Latest",
        "",
        "`config/repositories.yml` の全リポジトリについて、devlog に収集済みの最新イベントを"
        "1件ずつ並べたものです（GitHub 上の最終更新をその場で問い合わせるものではありません）。",
        "",
        "| Repository | 最新記録 | 種別 | 内容 |",
        "| --- | --- | --- | --- |",
    ]
    for full_name in repositories:
        name = full_name.split("/", 1)[1] if "/" in full_name else full_name
        found = latest.get(name)
        if not found:
            lines.append(f"| {_cell(name)} | - | - | {NO_RECORD_TEXT} |")
            continue
        parsed = parse_log_entry(found["entry"])
        label = _cell(parsed["label"])
        content = f"[{label}]({parsed['url']})" if parsed["url"] else label
        lines.append(f"| {_cell(name)} | {found['date']} | {_cell(parsed['kind'])} | {content} |")
    return "\n".join(lines).rstrip() + "\n"


def write_latest_view() -> list[Path]:
    """(Re)generate logs/latest.md. Returns [path] if it changed, else [].

    The page carries no "generated at" stamp: it would only ever record when
    the table last *changed* (an unchanged run rewrites nothing, by design),
    which is what the dates in the table already say.
    """
    content = render_latest_view(load_repositories(), collect_latest_events())
    current = LATEST_PATH.read_text(encoding="utf-8") if LATEST_PATH.exists() else None
    if current == content:
        return []  # nothing moved: leave the file - and the commit - alone

    LATEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    LATEST_PATH.write_text(content, encoding="utf-8")
    return [LATEST_PATH]


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def requests_phrase(count: int) -> str:
    return f"{count} API request" + ("" if count == 1 else "s")


def report_step(label: str, started: float, requests_before: int) -> str:
    """One line of the per-repository timing report.

    Timings are what actually tells us where a slow run went; they are printed
    with plain perf_counter() arithmetic rather than a logging framework.
    """
    return (
        f"  {label + ':':<16}{time.perf_counter() - started:6.1f}s"
        f"  ({requests_phrase(API_REQUEST_COUNT - requests_before)})"
    )


def get_lookback_days() -> int:
    """Normal runs use LOOKBACK_DAYS. A manual run (workflow_dispatch) may
    override this via DEVLOG_LOOKBACK_DAYS, e.g. to backfill history."""
    raw = os.environ.get("DEVLOG_LOOKBACK_DAYS", "").strip()
    if not raw:
        return LOOKBACK_DAYS
    try:
        days = int(raw)
    except ValueError:
        print(
            f"warning: invalid DEVLOG_LOOKBACK_DAYS={raw!r}, using default {LOOKBACK_DAYS}",
            file=sys.stderr,
        )
        return LOOKBACK_DAYS
    return max(1, days)


def main() -> None:
    token = os.environ.get("DEVLOG_READ_TOKEN") or os.environ.get("GITHUB_TOKEN")
    lookback_days = get_lookback_days()
    since = datetime.now(timezone.utc) - timedelta(days=lookback_days)
    print(f"Looking back {lookback_days} day(s), since {since.isoformat()}")

    repos = load_repositories()
    if not repos:
        # Not fatal: the daily views below are still regenerated so that
        # today.md / yesterday.md keep tracking the calendar.
        print("No repositories configured in config/repositories.yml", file=sys.stderr)

    all_events: list[dict] = []
    run_started = time.perf_counter()
    for full_name in repos:
        if "/" not in full_name:
            print(f"warning: skipping invalid repository entry: {full_name!r}", file=sys.stderr)
            continue
        owner, repo = full_name.split("/", 1)
        print(f"Collecting {full_name} ...")
        repo_started, repo_requests = time.perf_counter(), API_REQUEST_COUNT
        for label, fetch_fn in FETCH_STEPS:
            step_started, step_requests = time.perf_counter(), API_REQUEST_COUNT
            try:
                all_events += fetch_fn(owner, repo, token, since)
            except GitHubError as e:
                print(f"warning: {full_name}: {fetch_fn.__name__} failed: {e}", file=sys.stderr)
            print(report_step(label, step_started, step_requests))
        print(report_step("total", repo_started, repo_requests))

    print(f"Collected in {time.perf_counter() - run_started:.1f}s "
          f"using {requests_phrase(API_REQUEST_COUNT)}.")

    changed = add_events_to_logs(all_events)
    if not changed:
        print("No new events; nothing to update.")

    # Always regenerate the derived views, even when no new event was
    # collected: "today" and "yesterday" move with the calendar.
    changed += write_daily_views()
    changed += write_latest_view()

    if changed:
        print("Updated files:")
        for p in changed:
            print(f"  {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

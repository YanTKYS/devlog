#!/usr/bin/env python3
"""Collect merged PRs, releases and direct-to-default-branch commits from the
repositories listed in config/repositories.yml, and append them to the
monthly devlog files under logs/YYYY/YYYY-MM.md.

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
  - GitHub timestamps are UTC. Log entries are dated by Asia/Tokyo local
    date (JST), since this is a development *diary* meant to read naturally
    for a JST-based team: an event just after midnight JST should land on
    that JST day, not the previous UTC day.
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
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "repositories.yml"
LOGS_DIR = ROOT / "logs"

API_ROOT = "https://api.github.com"
LOOKBACK_DAYS = 35
JST = ZoneInfo("Asia/Tokyo")


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

    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (403, 502, 503) and attempt == 0:
                time.sleep(2)
                continue
            body = e.read().decode("utf-8", "replace")
            raise GitHubError(f"GET {url} -> {e.code}: {body[:300]}") from e


def paginate(path: str, token: str | None, params: dict | None = None, max_pages: int = 10):
    params = dict(params or {})
    params.setdefault("per_page", 50)
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


def fetch_direct_commits(owner: str, repo: str, token: str | None, since: datetime) -> list[dict]:
    repo_info = api_request(f"/repos/{owner}/{repo}", token)
    branch = repo_info["default_branch"]
    since_param = since.strftime("%Y-%m-%dT%H:%M:%SZ")

    events = []
    for commit in paginate(
        f"/repos/{owner}/{repo}/commits",
        token,
        {"sha": branch, "since": since_param},
        max_pages=5,
    ):
        sha = commit["sha"]
        associated_prs = api_request(f"/repos/{owner}/{repo}/commits/{sha}/pulls", token) or []
        if any(p.get("merged_at") for p in associated_prs):
            continue  # already recorded as part of its merged PR

        commit_info = commit.get("commit", {})
        message = commit_info.get("message") or ""
        first_line = message.splitlines()[0] if message else ""
        date_field = (commit_info.get("committer") or commit_info.get("author") or {}).get("date")
        if not date_field:
            continue
        dt = parse_dt(date_field)
        events.append(
            {
                "type": "commit",
                "date": to_jst_date(dt),
                "repo": repo,
                "short_sha": sha[:7],
                "message": first_line,
                "url": commit["html_url"],
            }
        )
    return events


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
# main
# ---------------------------------------------------------------------------


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
        print("No repositories configured in config/repositories.yml", file=sys.stderr)
        return

    all_events: list[dict] = []
    for full_name in repos:
        if "/" not in full_name:
            print(f"warning: skipping invalid repository entry: {full_name!r}", file=sys.stderr)
            continue
        owner, repo = full_name.split("/", 1)
        print(f"Collecting {full_name} ...")
        for fetch_fn in (fetch_merged_prs, fetch_releases, fetch_direct_commits):
            try:
                all_events += fetch_fn(owner, repo, token, since)
            except GitHubError as e:
                print(f"warning: {full_name}: {fetch_fn.__name__} failed: {e}", file=sys.stderr)

    changed = add_events_to_logs(all_events)
    if changed:
        print("Updated files:")
        for p in changed:
            print(f"  {p.relative_to(ROOT)}")
    else:
        print("No new events; nothing to update.")


if __name__ == "__main__":
    main()

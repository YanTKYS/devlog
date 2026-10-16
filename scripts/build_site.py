#!/usr/bin/env python3
"""Build the static GitHub Pages site (a log viewer) into _site/.

The monthly files logs/YYYY/YYYY-MM.md stay the single source of truth. This
script only *reads* them (it never writes under logs/), converts them into
one viewer-oriented JSON file, and copies the static assets from site/.

    python3 scripts/build_site.py [--out _site]

Design notes:
  - Standard library only, like scripts/collect.py. The month-file parser is
    imported from collect.py so the format has one owner.
  - Pages is a public site. Only repositories listed in config/pages.yml are
    emitted; everything else (records *and* repository names) is dropped here,
    before anything is written or printed. Nothing is published by default.
  - Nothing is inferred: every field comes straight from the log entry. A
    field the log does not carry is null.
  - Dates are the JST dates already stored in the logs. "Today" is the date
    of the last collection (the heading of logs/today.md), not the viewer's
    clock, so the page never presents stale data as live.
  - Notes are published only when listed in PUBLIC_NOTES. Each listed file is
    copied to notes/<id>.md with its relative links rewritten: a link to
    another published note becomes a #notes route, a link to anything else in
    the repository points at the file on GitHub, so unlisted files (other
    notes, data/deepresearch/) are never copied into the site.
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import shutil
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import collect  # noqa: E402  (shared month-file parser, JST, config loader)

ROOT = collect.ROOT
LOGS_DIR = collect.LOGS_DIR
REPOSITORIES_PATH = collect.CONFIG_PATH
PAGES_CONFIG_PATH = ROOT / "config" / "pages.yml"
SITE_SRC = ROOT / "site"
DATA_FILE = "data/devlog.json"
NOTES_DATA_FILE = "data/notes.json"
SCHEMA_VERSION = 1

# Notes shown in the viewer's "ノート" tab. Only these files are published;
# add an entry here to publish another note. `id` is the URL (#notes/<id>).
PUBLIC_NOTES = (
    {
        "id": "free-apis",
        "source": "notes/free-apis.md",
        "description": "個人開発・PoC で使える無料・無料枠の API とデータサービスの比較",
    },
    {
        "id": "ai-coding-tools",
        "source": "notes/ai-coding-tools.md",
        "description": "主要 AI コーディングツール10製品の料金・利用制限・開発機能と、用途別の選び方",
    },
)
# Where links to unpublished repository files point (the file on GitHub).
SOURCE_REPOSITORY = os.environ.get("GITHUB_REPOSITORY") or "YanTKYS/devlog"
SOURCE_BRANCH = "main"

_PR_RE = re.compile(r"^- PR #(\d+)(?:[ \t]+(.*))?$")
_RELEASE_RE = re.compile(r"^- Release (\S+)(?: \((.*)\))?$")
_COMMIT_RE = re.compile(r"^- Commit `([0-9a-fA-F]+)`(?:[ \t]+(.*))?$")
_URL_LINE_RE = re.compile(r"^\s+-\s+(.*\S)\s*$")
_MD_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^\s)]+)\)")
_ANGLE_URL_RE = re.compile(r"<(https?://[^>\s]+)>")
_BARE_URL_RE = re.compile(r"https?://\S+")
_TODAY_HEADING_RE = re.compile(r"^# Today - (\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
_MONTH_STEM_RE = re.compile(r"^\d{4}-\d{2}$")
_NOTE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
_CODE_SPAN_RE = re.compile(r"(`+)(?:.*?[^`])?\1(?!`)")
_LINK_TARGET_RE = re.compile(r"\]\((\s*)(<[^>\n]*>|[^\s()<>]+)")
_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
_H1_RE = re.compile(r"^# +(.+?)\s*#*\s*$", re.MULTILINE)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


def load_public_repositories(path: Path = PAGES_CONFIG_PATH) -> list[str]:
    """Parse `public_repositories:\n  - owner/repo` (same flat format as
    repositories.yml). A missing file means nothing is public."""
    if not path.exists():
        return []
    repos: list[str] = []
    in_list = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if not (raw_line[:1].isspace() or raw_line.lstrip().startswith("-")):
            in_list = line.strip() == "public_repositories:"
            continue
        if in_list:
            m = re.match(r"^\s*-\s*(.+)$", line)
            if m and m.group(1).strip().strip("'\""):
                repos.append(m.group(1).strip().strip("'\""))
    return repos


# ---------------------------------------------------------------------------
# Log entry parsing
# ---------------------------------------------------------------------------


def extract_url(entry_lines: list[str]) -> str | None:
    """First http(s) URL on the entry's detail lines.

    Accepts a Markdown link, <url> or a bare URL; the URL is returned as
    written (never re-encoded).
    """
    for line in entry_lines[1:]:
        m = _URL_LINE_RE.match(line)
        if not m:
            continue
        text = m.group(1)
        for regex in (_MD_LINK_RE, _ANGLE_URL_RE):
            found = regex.search(text)
            if found:
                return found.group(1)
        if _BARE_URL_RE.fullmatch(text):
            return text
    return None


def parse_entry(entry: str, date: str, repo: str) -> dict | None:
    """Turn one log entry into a record, or None if it is not a known kind."""
    lines = entry.strip().splitlines()
    if not lines:
        return None
    first = lines[0].rstrip()
    record = {
        "date": date,
        "repo": repo,
        "type": None,
        "title": "",
        "url": extract_url(lines),
        "number": None,
        "tag": None,
        "release_name": None,
        "sha": None,
    }
    m = _PR_RE.match(first)
    if m:
        record.update(type="pr", number=int(m.group(1)), title=(m.group(2) or "").strip())
        return record
    m = _RELEASE_RE.match(first)
    if m:
        name = (m.group(2) or "").strip() or None
        record.update(type="release", tag=m.group(1), release_name=name, title=name or m.group(1))
        return record
    m = _COMMIT_RE.match(first)
    if m:
        record.update(type="commit", sha=m.group(1), title=(m.group(2) or "").strip())
        return record
    return None


def url_matches_repo(url: str | None, full_name: str) -> bool:
    """A record's link must be on github.com under the repository it is
    filed under; anything else is not published."""
    if not url:
        return True  # nothing to leak; the card simply has no link
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or parts.netloc.lower() != "github.com":
        return False
    return parts.path.lower().startswith(f"/{full_name.lower()}/")


def iter_month_files(logs_dir: Path) -> list[Path]:
    return sorted(
        p
        for p in logs_dir.glob("*/*.md")
        if _MONTH_STEM_RE.match(p.stem) and p.parent.name == p.stem[:4]
    )


# ---------------------------------------------------------------------------
# Data build
# ---------------------------------------------------------------------------


def read_collection_date(logs_dir: Path, now: datetime) -> str:
    """The JST date of the last collection: today.md's heading, else `now`."""
    path = logs_dir / "today.md"
    if path.exists():
        m = _TODAY_HEADING_RE.search(path.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return now.astimezone(collect.JST).strftime("%Y-%m-%d")


def build_data(
    logs_dir: Path,
    repositories: list[str],
    public_repositories: list[str],
    now: datetime,
    warn=lambda msg: print(msg, file=sys.stderr),
) -> dict:
    # Only repos that are both collected and explicitly public are published.
    configured = {r.lower() for r in repositories}
    published: dict[str, str] = {}  # repo name -> owner/name
    for full in public_repositories:
        if "/" not in full:
            warn(f"warning: invalid entry in pages.yml: {full!r}")
        elif full.lower() not in configured:
            warn(f"warning: {full} is in pages.yml but not in repositories.yml; ignored")
        else:
            published[full.split("/", 1)[1]] = full

    records: list[dict] = []
    seen: set = set()
    excluded = 0
    for path in iter_month_files(logs_dir):
        sections = collect.parse_month_file(path.read_text(encoding="utf-8"))
        for date in sorted(sections):
            for repo, entries in sections[date].items():
                full = published.get(repo)
                if full is None:
                    excluded += len(entries)  # count only; never print content
                    continue
                for entry in entries:
                    record = parse_entry(entry, date, repo)
                    if record is None:
                        warn(f"warning: {path.name}: unrecognized entry under {repo} on {date}; skipped")
                        continue
                    if not url_matches_repo(record["url"], full):
                        warn(f"warning: {path.name}: link outside {full} on {date}; skipped")
                        continue
                    key = record["url"] or (date, repo, record["type"], record["title"])
                    if key in seen:
                        continue
                    seen.add(key)
                    records.append(record)

    # Latest = last recorded entry on the newest date, the same rule that
    # produces logs/latest.md (entries carry no time of day).
    latest: dict[str, dict] = {}
    for record in records:
        current = latest.get(record["repo"])
        if current is None or record["date"] >= current["date"]:
            latest[record["repo"]] = record

    # Newest date first; the order within a day stays as written in the log.
    records.sort(key=lambda r: r["date"], reverse=True)

    collected_today = read_collection_date(logs_dir, now)
    collected_yesterday = (
        datetime.strptime(collected_today, "%Y-%m-%d") - timedelta(days=1)
    ).strftime("%Y-%m-%d")

    repository_rows = []
    for full in repositories:
        name = full.split("/", 1)[1] if "/" in full else full
        if published.get(name) != full:
            continue
        repository_rows.append(
            {
                "name": name,
                "full_name": full,
                "url": f"https://github.com/{full}",
                "latest": latest.get(name),
            }
        )

    print(f"records: {len(records)} published, {excluded} excluded (not in pages.yml)")
    return {
        "schema": SCHEMA_VERSION,
        "generated_at": now.astimezone(collect.JST).isoformat(timespec="seconds"),
        "collected": {"today": collected_today, "yesterday": collected_yesterday},
        "months": sorted({r["date"][:7] for r in records}, reverse=True),
        "repositories": repository_rows,
        "records": records,
    }


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------


def note_title(markdown: str, fallback: str) -> str:
    m = _H1_RE.search(markdown)
    return m.group(1).strip() if m else fallback


def rewrite_note_link(
    target: str, source: str, note_id: str, published: dict[str, str], repository: str, branch: str
) -> str:
    """Where a link in a published note should point.

    `#frag` -> `#notes/<id>/frag` (a heading of this note, kept apart from the
    viewer's own routes); a published note -> `#notes/<id>[/frag]`; any other
    repository path -> the file on GitHub. URLs with a scheme are unchanged.
    """
    if _SCHEME_RE.match(target) or target.startswith("//"):
        return target
    path, _, fragment = target.partition("#")
    if not path:
        return f"#notes/{note_id}/{fragment}" if fragment else f"#notes/{note_id}"
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
    if resolved.startswith("../") or resolved == "..":
        return target  # outside the repository; the viewer shows it as text
    if resolved in published:
        route = f"#notes/{published[resolved]}"
        return f"{route}/{fragment}" if fragment else route
    url = f"https://github.com/{repository}/blob/{branch}/{resolved}"
    return f"{url}#{fragment}" if fragment else url


def rewrite_note_links(
    markdown: str,
    source: str,
    note_id: str,
    published: dict[str, str],
    repository: str = SOURCE_REPOSITORY,
    branch: str = SOURCE_BRANCH,
) -> str:
    """Rewrite inline link targets `](...)` outside code blocks and code spans."""
    out: list[str] = []
    fence = None
    for line in markdown.split("\n"):
        m = _FENCE_RE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not line.strip(" `~"):
                fence = None
            out.append(line)
            continue
        if m:
            fence = m.group(1)
            out.append(line)
            continue
        parts = []
        pos = 0
        for code in _CODE_SPAN_RE.finditer(line):
            parts.append((line[pos : code.start()], True))
            parts.append((code.group(0), False))
            pos = code.end()
        parts.append((line[pos:], True))

        def repl(lm: re.Match) -> str:
            raw = lm.group(2)
            target = raw[1:-1] if raw.startswith("<") else raw
            new = rewrite_note_link(target, source, note_id, published, repository, branch)
            if new == target:
                return lm.group(0)
            return f"]({lm.group(1)}<{new}>" if raw.startswith("<") else f"]({lm.group(1)}{new}"

        out.append("".join(_LINK_TARGET_RE.sub(repl, text) if rewrite else text for text, rewrite in parts))
    return "\n".join(out)


def build_notes(notes=PUBLIC_NOTES, root: Path = ROOT) -> tuple[list[dict], dict[str, str]]:
    """The notes manifest and the published Markdown, keyed by output path.

    A listed note that is missing, or a malformed or duplicate id, fails the
    build instead of silently dropping the note.
    """
    published: dict[str, str] = {}
    for note in notes:
        if not _NOTE_ID_RE.match(note["id"]) or note["id"] in published.values():
            raise SystemExit(f"invalid or duplicate note id: {note['id']!r}")
        published[posixpath.normpath(note["source"])] = note["id"]

    manifest: list[dict] = []
    files: dict[str, str] = {}
    for note in notes:
        source = posixpath.normpath(note["source"])
        path = root / source
        if not path.is_file():
            raise SystemExit(f"note listed in PUBLIC_NOTES not found: {source}")
        text = path.read_text(encoding="utf-8")
        out_path = f"notes/{note['id']}.md"
        files[out_path] = rewrite_note_links(text, source, note["id"], published)
        manifest.append(
            {
                "id": note["id"],
                "title": note_title(text, note["id"]),
                "description": note["description"],
                "path": out_path,
                "source": source,
            }
        )
    return manifest, files


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def build_site(
    out_dir: Path,
    data: dict,
    site_src: Path = SITE_SRC,
    notes: tuple[list[dict], dict[str, str]] = ([], {}),
) -> None:
    resolved = out_dir.resolve()
    if resolved == site_src.resolve() or resolved == ROOT or resolved in ROOT.parents:
        raise SystemExit(f"refusing to clear {out_dir}: it contains the repository sources")
    if out_dir.exists():
        shutil.rmtree(out_dir)
    shutil.copytree(site_src, out_dir)
    data_path = out_dir / DATA_FILE
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest, files = notes
    for rel, text in files.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    (out_dir / NOTES_DATA_FILE).write_text(
        json.dumps({"schema": SCHEMA_VERSION, "notes": manifest}, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--out", type=Path, default=ROOT / "_site", help="output directory")
    args = parser.parse_args()

    data = build_data(
        LOGS_DIR,
        collect.load_repositories(REPOSITORIES_PATH),
        load_public_repositories(),
        datetime.now(collect.JST),
    )
    notes = build_notes()
    build_site(args.out, data, notes=notes)
    print(f"Built {args.out} ({len(data['repositories'])} repositories, {len(notes[0])} notes)")


if __name__ == "__main__":
    main()

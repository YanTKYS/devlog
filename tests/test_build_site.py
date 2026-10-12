"""Tests for scripts/build_site.py (stdlib unittest; run: python3 -m unittest discover -s tests)."""

import json
import re
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_site as bs  # noqa: E402
import collect  # noqa: E402

NOW = datetime(2026, 10, 12, 6, 0, tzinfo=timezone.utc)  # 15:00 JST, 2026-10-12

MONTH_OCT = """# 2026-10

## 2026-10-12

### alpha

- PR #7 日本語のタイトル (括弧付き) with `code` and [brackets]
  - merged
  - https://github.com/o/alpha/pull/7

- Commit `abc1234` direct change
  - direct commit
  - https://github.com/o/alpha/commit/abc1234def

### secret

- PR #1 PRIVATE-TITLE
  - merged
  - https://github.com/o/secret/pull/1

## 2026-10-11

### alpha

- Release v1.2.0 (v1.2.0 - 設定対応 (beta))
  - release
  - https://github.com/o/alpha/releases/tag/v1.2.0

- PR #6 older
  - merged
  - https://github.com/o/alpha/pull/6

### beta

- Commit `ffff000`
  - direct commit
  - https://github.com/o/beta/commit/ffff000aaa
"""

MONTH_SEP = """# 2026-09

## 2026-09-30

### alpha

- PR #5 september
  - merged
  - https://github.com/o/alpha/pull/5

- PR #5 september
  - merged
  - https://github.com/o/alpha/pull/5
"""

TODAY = "<!-- auto -->\n\n# Today - 2026-10-12\n\nbody\n"


def make_logs(tmp: Path, today=TODAY) -> Path:
    logs = tmp / "logs"
    (logs / "2026").mkdir(parents=True)
    (logs / "2026" / "2026-10.md").write_text(MONTH_OCT, encoding="utf-8")
    (logs / "2026" / "2026-09.md").write_text(MONTH_SEP, encoding="utf-8")
    if today is not None:
        (logs / "today.md").write_text(today, encoding="utf-8")
    return logs


REPOS = ["o/alpha", "o/beta", "o/gamma", "o/secret"]


def build(logs, public=("o/alpha", "o/beta", "o/gamma"), repos=REPOS, now=NOW):
    warnings = []
    data = bs.build_data(logs, list(repos), list(public), now, warn=warnings.append)
    return data, warnings


class ParseEntryTests(unittest.TestCase):
    def parse(self, text):
        return bs.parse_entry(text, "2026-10-12", "alpha")

    def test_pr(self):
        r = self.parse("- PR #68 Enable PDF reflow\n  - merged\n  - https://github.com/o/alpha/pull/68")
        self.assertEqual((r["type"], r["number"], r["title"]), ("pr", 68, "Enable PDF reflow"))
        self.assertEqual(r["url"], "https://github.com/o/alpha/pull/68")

    def test_release_with_and_without_name(self):
        r = self.parse("- Release v1.2.1 (v1.2.1 - 不具合修正)\n  - release\n  - https://x/y")
        self.assertEqual((r["type"], r["tag"], r["release_name"]), ("release", "v1.2.1", "v1.2.1 - 不具合修正"))
        self.assertEqual(r["title"], "v1.2.1 - 不具合修正")
        r = self.parse("- Release v2.0.0\n  - release\n  - https://github.com/o/alpha/releases/tag/v2.0.0")
        self.assertEqual((r["tag"], r["release_name"], r["title"]), ("v2.0.0", None, "v2.0.0"))

    def test_release_name_with_parentheses(self):
        r = self.parse("- Release v1 (name (beta))\n  - release")
        self.assertEqual(r["release_name"], "name (beta)")

    def test_commit_with_and_without_message(self):
        r = self.parse("- Commit `fa71e58` chore: news\n  - direct commit\n  - https://github.com/o/alpha/commit/fa71e58b")
        self.assertEqual((r["type"], r["sha"], r["title"]), ("commit", "fa71e58", "chore: news"))
        r = self.parse("- Commit `fa71e58`\n  - direct commit")
        self.assertEqual((r["sha"], r["title"]), ("fa71e58", ""))

    def test_unknown_entry_is_none(self):
        self.assertIsNone(self.parse("- something handwritten\n  - merged"))

    def test_url_formats(self):
        self.assertEqual(bs.extract_url(["- x", "  - [t](https://a/b?c=1&d=2)"]), "https://a/b?c=1&d=2")
        self.assertEqual(bs.extract_url(["- x", "  - <https://a/b_(c)>"]), "https://a/b_(c)")
        self.assertEqual(bs.extract_url(["- x", "  - https://a/b_(c)#frag"]), "https://a/b_(c)#frag")
        self.assertIsNone(bs.extract_url(["- x", "  - merged"]))
        self.assertIsNone(bs.extract_url(["- x", "  - javascript:alert(1)"]))

    def test_long_title_kept_verbatim(self):
        title = "長い" * 300 + " <b>x</b> & \"quotes\""
        r = self.parse(f"- PR #1 {title}\n  - merged")
        self.assertEqual(r["title"], title)


class BuildDataTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.logs = make_logs(Path(self._tmp.name))

    def test_records_classified_and_ordered(self):
        data, warnings = build(self.logs)
        self.assertEqual(warnings, [])
        got = [(r["date"], r["repo"], r["type"], r["number"] or r["tag"] or r["sha"]) for r in data["records"]]
        self.assertEqual(got, [
            ("2026-10-12", "alpha", "pr", 7),
            ("2026-10-12", "alpha", "commit", "abc1234"),
            ("2026-10-11", "alpha", "release", "v1.2.0"),
            ("2026-10-11", "alpha", "pr", 6),
            ("2026-10-11", "beta", "commit", "ffff000"),
            ("2026-09-30", "alpha", "pr", 5),  # duplicate URL collapsed
        ])
        self.assertEqual(data["records"][0]["title"], "日本語のタイトル (括弧付き) with `code` and [brackets]")
        self.assertEqual(data["months"], ["2026-10", "2026-09"])

    def test_build_is_deterministic(self):
        a, _ = build(self.logs)
        b, _ = build(self.logs)
        self.assertEqual(json.dumps(a), json.dumps(b))

    def test_private_repo_never_in_output(self):
        data, _ = build(self.logs)
        blob = json.dumps(data, ensure_ascii=False)
        for needle in ("PRIVATE-TITLE", "secret"):
            self.assertNotIn(needle, blob)
        self.assertEqual({r["repo"] for r in data["records"]}, {"alpha", "beta"})
        self.assertEqual([r["name"] for r in data["repositories"]], ["alpha", "beta", "gamma"])

    def test_nothing_public_by_default(self):
        data, _ = build(self.logs, public=())
        self.assertEqual((data["records"], data["repositories"], data["months"]), ([], [], []))

    def test_public_entry_outside_repositories_yml_is_ignored(self):
        data, warnings = build(self.logs, public=("o/alpha", "o/unlisted"))
        self.assertEqual([r["name"] for r in data["repositories"]], ["alpha"])
        self.assertTrue(any("o/unlisted" in w for w in warnings))

    def test_link_outside_its_repository_is_dropped(self):
        path = self.logs / "2026" / "2026-10.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "https://github.com/o/alpha/pull/6", "https://github.com/o/secret/pull/6"), encoding="utf-8")
        data, warnings = build(self.logs)
        self.assertNotIn(6, [r["number"] for r in data["records"]])
        self.assertEqual(len(warnings), 1)
        self.assertNotIn("older", warnings[0])  # warnings never echo titles

    def test_latest_per_repo_and_repo_without_records(self):
        data, _ = build(self.logs)
        rows = {r["name"]: r for r in data["repositories"]}
        # newest date; the last entry written for that date (same rule as latest.md)
        self.assertEqual(rows["alpha"]["latest"]["sha"], "abc1234")
        self.assertEqual(rows["beta"]["latest"]["date"], "2026-10-11")
        self.assertIsNone(rows["gamma"]["latest"])
        self.assertEqual(rows["alpha"]["url"], "https://github.com/o/alpha")

    def test_collection_dates_from_today_md(self):
        data, _ = build(self.logs)
        self.assertEqual(data["collected"], {"today": "2026-10-12", "yesterday": "2026-10-11"})

    def test_collection_date_falls_back_to_jst_now(self):
        (self.logs / "today.md").unlink()
        # 2026-08-19 16:00 UTC is already 2026-08-20 in JST
        data, _ = build(self.logs, now=datetime(2026, 8, 19, 16, 0, tzinfo=timezone.utc))
        self.assertEqual(data["collected"], {"today": "2026-08-20", "yesterday": "2026-08-19"})
        self.assertTrue(data["generated_at"].endswith("+09:00"))

    def test_yesterday_crosses_year_boundary(self):
        (self.logs / "today.md").write_text("# Today - 2027-01-01\n", encoding="utf-8")
        data, _ = build(self.logs)
        self.assertEqual(data["collected"]["yesterday"], "2026-12-31")

    def test_empty_logs(self):
        with tempfile.TemporaryDirectory() as tmp:
            data, _ = build(Path(tmp))
        self.assertEqual(data["records"], [])
        self.assertEqual(len(data["repositories"]), 3)
        self.assertTrue(all(r["latest"] is None for r in data["repositories"]))


class PagesConfigTests(unittest.TestCase):
    def test_load_public_repositories(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "pages.yml"
            p.write_text("# c\npublic_repositories:\n  - o/a  # inline\n  - 'o/b'\nother:\n  - o/c\n", encoding="utf-8")
            self.assertEqual(bs.load_public_repositories(p), ["o/a", "o/b"])
            self.assertEqual(bs.load_public_repositories(Path(tmp) / "missing.yml"), [])


class OutputTests(unittest.TestCase):
    def test_build_site_writes_assets_and_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            logs = make_logs(Path(tmp))
            data, _ = build(logs)
            out = Path(tmp) / "out"
            out.mkdir()
            (out / "stale.txt").write_text("x")
            bs.build_site(out, data)
            self.assertFalse((out / "stale.txt").exists())
            self.assertTrue((out / "index.html").exists())
            loaded = json.loads((out / bs.DATA_FILE).read_text(encoding="utf-8"))
            self.assertEqual(loaded["records"][0]["title"], data["records"][0]["title"])

    def test_refuses_to_clear_repository_root(self):
        with self.assertRaises(SystemExit):
            bs.build_site(ROOT, {})
        with self.assertRaises(SystemExit):
            bs.build_site(ROOT / "site", {})

    def test_site_uses_relative_paths_only(self):
        """The site is served under /<repo>/, so no root-absolute URLs may be used."""
        html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
            self.assertFalse(m.group(1).startswith("/"), m.group(1))
            self.assertFalse(m.group(1).startswith("http"), m.group(1))
        app = (ROOT / "site" / "app.js").read_text(encoding="utf-8")
        self.assertRegex(app, r'DATA_URL = "data/devlog\.json"')
        self.assertNotIn("api.github.com", app)
        self.assertNotIn("innerHTML", app)


class RealLogsTests(unittest.TestCase):
    """Consistency of the JSON generated from the repository's actual logs."""

    @classmethod
    def setUpClass(cls):
        cls.repos = collect.load_repositories()
        cls.public = bs.load_public_repositories()
        cls.warnings = []
        cls.data = bs.build_data(bs.LOGS_DIR, cls.repos, cls.public, NOW, warn=cls.warnings.append)

    def test_every_record_is_well_formed(self):
        self.assertTrue(self.data["records"])
        published = {r.split("/", 1)[1]: r for r in self.public}
        for r in self.data["records"]:
            self.assertRegex(r["date"], r"^\d{4}-\d{2}-\d{2}$")
            self.assertIn(r["type"], ("pr", "release", "commit"))
            self.assertIn(r["repo"], published)
            self.assertTrue(r["url"].startswith(f"https://github.com/{published[r['repo']]}/"), r["url"])
            if r["type"] == "pr":
                self.assertIsNotNone(r["number"])
            elif r["type"] == "release":
                self.assertTrue(r["tag"])
            else:
                self.assertRegex(r["sha"], r"^[0-9a-f]+$")

    def test_no_duplicate_urls(self):
        urls = [r["url"] for r in self.data["records"]]
        self.assertEqual(len(urls), len(set(urls)))

    def test_only_allowlisted_repositories_are_published(self):
        allowed = {r.split("/", 1)[1] for r in self.public} & {r.split("/", 1)[1] for r in self.repos}
        self.assertEqual({r["name"] for r in self.data["repositories"]}, allowed)
        self.assertLessEqual({r["repo"] for r in self.data["records"]}, allowed)
        hidden = {r.split("/", 1)[1] for r in self.repos} - allowed
        blob = json.dumps(self.data, ensure_ascii=False)
        for name in hidden:
            self.assertNotIn(f"github.com/YanTKYS/{name}/", blob)

    def test_latest_matches_latest_md(self):
        """The viewer's per-repository latest equals the row in logs/latest.md."""
        rows = {}
        for line in (bs.LOGS_DIR / "latest.md").read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 4 and cells[1][:2] == "20":
                m = re.search(r"\((https://[^)]+)\)", cells[3])
                rows[cells[0]] = (cells[1], m.group(1) if m else None)
            elif len(cells) == 4 and cells[3] == "記録なし":
                rows[cells[0]] = None
        for repo in self.data["repositories"]:
            latest = repo["latest"]
            expected = rows.get(repo["name"], "missing")
            if latest is None:
                self.assertIsNone(expected, repo["name"])
            else:
                self.assertEqual((latest["date"], latest["url"]), expected, repo["name"])

    def test_today_matches_daily_view(self):
        today = self.data["collected"]["today"]
        text = (bs.LOGS_DIR / "today.md").read_text(encoding="utf-8")
        self.assertIn(f"# Today - {today}", text)


if __name__ == "__main__":
    unittest.main()

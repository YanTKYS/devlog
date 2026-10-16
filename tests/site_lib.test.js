// Tests for site/devlog-lib.js (run: node --test tests/)
"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const L = require("../site/devlog-lib.js");

const rec = (date, repo, type, extra) =>
  Object.assign({ date, repo, type, title: "t", url: "https://github.com/o/" + repo + "/x", number: null, tag: null, sha: null }, extra);

const records = [
  rec("2026-10-12", "alpha", "pr", { number: 7, title: "a1" }),
  rec("2026-10-12", "alpha", "commit", { sha: "abc1234", title: "a2" }),
  rec("2026-10-11", "beta", "release", { tag: "v1.0.0", title: "b1" }),
  rec("2026-10-11", "alpha", "pr", { number: 6, title: "a3" }),
  rec("2026-09-30", "beta", "pr", { number: 5, title: "b2" }),
];

test("filterRecords filters by month, repo and type, and combines them", () => {
  assert.equal(L.filterRecords(records, {}).length, 5);
  assert.equal(L.filterRecords(records, { month: "2026-10" }).length, 4);
  assert.equal(L.filterRecords(records, { month: "2026-09" }).length, 1);
  assert.equal(L.filterRecords(records, { repo: "beta" }).length, 2);
  assert.equal(L.filterRecords(records, { type: "pr" }).length, 3);
  assert.deepEqual(
    L.filterRecords(records, { month: "2026-10", repo: "alpha", type: "pr" }).map((r) => r.title),
    ["a1", "a3"]);
  assert.equal(L.filterRecords(records, { month: "2026-10", repo: "beta", type: "commit" }).length, 0);
});

test("sortByDate is stable within a day in both directions", () => {
  assert.deepEqual(L.sortByDate(records, "desc").map((r) => r.title), ["a1", "a2", "b1", "a3", "b2"]);
  assert.deepEqual(L.sortByDate(records, "asc").map((r) => r.title), ["b2", "b1", "a3", "a1", "a2"]);
  const shuffled = [records[4], records[1], records[3], records[0], records[2]];
  assert.deepEqual(L.sortByDate(shuffled, "desc").map((r) => r.date),
    ["2026-10-12", "2026-10-12", "2026-10-11", "2026-10-11", "2026-09-30"]);
});

test("groupByDate groups by day in the given order", () => {
  const g = L.groupByDate(L.sortByDate(records, "desc"));
  assert.deepEqual(g.map((x) => [x.date, x.records.length]),
    [["2026-10-12", 2], ["2026-10-11", 2], ["2026-09-30", 1]]);
  assert.deepEqual(L.groupByDate([]), []);
});

test("recordsOnDate extracts a single date", () => {
  assert.equal(L.recordsOnDate(records, "2026-10-11").length, 2);
  assert.deepEqual(L.recordsOnDate(records, "2026-10-13"), []);
});

test("latestMonth and month/day formatting", () => {
  assert.equal(L.latestMonth(["2026-09", "2026-10", "2026-05"]), "2026-10");
  assert.equal(L.latestMonth([]), null);
  assert.equal(L.formatMonth("2026-10"), "2026年10月");
  assert.equal(L.formatDay("2026-10-12"), "10月12日(月)");
  assert.equal(L.formatDay("2026-03-29"), "3月29日(日)");
  assert.equal(L.formatFullDay("2026-10-12"), "2026年10月12日(月)");
});

test("identifier shows the PR number, release tag or commit sha from the log", () => {
  assert.equal(L.identifier(records[0]), "PR #7");
  assert.equal(L.identifier(records[1]), "abc1234");
  assert.equal(L.identifier(records[2]), "v1.0.0");
  assert.equal(L.typeLabel("pr"), "Merged PR");
  assert.equal(L.typeLabel("commit"), "Direct commit");
});

test("safeUrl only allows http(s) links and keeps the URL intact", () => {
  const u = "https://github.com/o/r/pull/1?a=b&c=d#x_(y)";
  assert.equal(L.safeUrl(u), u);
  assert.equal(L.safeUrl("javascript:alert(1)"), null);
  assert.equal(L.safeUrl("data:text/html,x"), null);
  assert.equal(L.safeUrl(null), null);
});

test("repository search is case-insensitive and keeps repos without records", () => {
  const repos = [
    { name: "pdfengine", latest: rec("2026-10-12", "pdfengine", "pr") },
    { name: "idontlovepdf", latest: rec("2026-09-05", "idontlovepdf", "pr") },
    { name: "mailexporter", latest: null },
    { name: "clock", latest: null },
  ];
  assert.deepEqual(L.filterRepositories(repos, "PDF").map((r) => r.name), ["pdfengine", "idontlovepdf"]);
  assert.equal(L.filterRepositories(repos, "  ").length, 4);
  assert.equal(L.filterRepositories(repos, "zzz").length, 0);
  assert.deepEqual(L.sortRepositories(repos).map((r) => r.name),
    ["pdfengine", "idontlovepdf", "clock", "mailexporter"]);
});

test("empty data does not throw", () => {
  assert.deepEqual(L.filterRecords([], { month: "2026-10" }), []);
  assert.deepEqual(L.sortByDate([], "asc"), []);
  assert.deepEqual(L.filterRepositories([], "x"), []);
});

test("parseRoute: tabs, notes and note headings", () => {
  const r = (tab, note, anchor) => ({ tab, note: note || null, anchor: anchor || null });
  assert.deepEqual(L.parseRoute(""), r("recent"));
  assert.deepEqual(L.parseRoute("#recent"), r("recent"));
  assert.deepEqual(L.parseRoute("#daily"), r("daily"));
  assert.deepEqual(L.parseRoute("#repos"), r("repos"));
  assert.deepEqual(L.parseRoute("#unknown"), r("recent"));
  assert.deepEqual(L.parseRoute("#notes"), r("notes"));
  assert.deepEqual(L.parseRoute("#notes/"), r("notes"));
  assert.deepEqual(L.parseRoute("#notes/free-apis"), r("notes", "free-apis"));
  assert.deepEqual(L.parseRoute("#notes/ai-coding-tools/a-概要"), r("notes", "ai-coding-tools", "a-概要"));
  // Browsers report non-ASCII hashes percent-encoded.
  assert.deepEqual(L.parseRoute("#notes/ai-coding-tools/" + encodeURIComponent("c-料金利用制限の比較")),
    r("notes", "ai-coding-tools", "c-料金利用制限の比較"));
  assert.deepEqual(L.parseRoute("#notes/x/%E0%A4%A"), r("notes", "x", "%E0%A4%A"));  // malformed: kept as is
});

test("parseRoute: a heading named like a tab stays inside its note", () => {
  assert.deepEqual(L.parseRoute("#notes/free-apis/recent"), { tab: "notes", note: "free-apis", anchor: "recent" });
  assert.deepEqual(L.parseRoute("#notes/free-apis/notes"), { tab: "notes", note: "free-apis", anchor: "notes" });
  assert.ok(L.TABS.includes("notes") && L.TABS.length === 4);
});

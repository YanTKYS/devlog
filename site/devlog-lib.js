/* devlog viewer: pure data helpers (no DOM). Loaded by index.html and by
 * tests/site_lib.test.js (Node), so keep it free of browser globals. */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.DevlogLib = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var TYPE_LABELS = { pr: "Merged PR", release: "Release", commit: "Direct commit" };
  var TYPE_SHORT = { pr: "PR", release: "Release", commit: "Commit" };
  var WEEKDAYS = ["日", "月", "火", "水", "木", "金", "土"];

  function typeLabel(type) { return TYPE_LABELS[type] || type; }
  function typeShort(type) { return TYPE_SHORT[type] || type; }

  /** Badge text from the identifier the log carries: PR #68 / v1.2.1 / sha. */
  function identifier(r) {
    if (r.type === "pr" && r.number != null) return "PR #" + r.number;
    if (r.type === "release" && r.tag) return r.tag;
    if (r.type === "commit" && r.sha) return r.sha;
    return typeShort(r.type);
  }

  /** Only http(s) links are ever rendered as links. */
  function safeUrl(url) {
    return typeof url === "string" && /^https?:\/\//i.test(url) ? url : null;
  }

  function monthOf(date) { return date.slice(0, 7); }

  function formatMonth(month) {
    var p = month.split("-");
    return p[0] + "年" + Number(p[1]) + "月";
  }

  /** "2026-10-12" -> "10月12日(月)"; weekday from UTC so the viewer's time zone cannot shift it. */
  function formatDay(date) {
    var p = date.split("-").map(Number);
    var wd = new Date(Date.UTC(p[0], p[1] - 1, p[2])).getUTCDay();
    return p[1] + "月" + p[2] + "日(" + WEEKDAYS[wd] + ")";
  }

  function formatFullDay(date) {
    return date.split("-")[0] + "年" + formatDay(date);
  }

  /** filters: {month, repo, type}; an empty/undefined value means "all". */
  function filterRecords(records, filters) {
    var f = filters || {};
    return records.filter(function (r) {
      return (!f.month || monthOf(r.date) === f.month) &&
        (!f.repo || r.repo === f.repo) &&
        (!f.type || r.type === f.type);
    });
  }

  /** Stable sort by date only, so the order within a day stays as logged. */
  function sortByDate(records, order) {
    var dir = order === "asc" ? 1 : -1;
    return records
      .map(function (r, i) { return { r: r, i: i }; })
      .sort(function (a, b) {
        if (a.r.date !== b.r.date) return a.r.date < b.r.date ? -dir : dir;
        return a.i - b.i;
      })
      .map(function (x) { return x.r; });
  }

  /** Group consecutive records that share a date: [{date, records}]. */
  function groupByDate(records) {
    var groups = [];
    records.forEach(function (r) {
      var last = groups[groups.length - 1];
      if (last && last.date === r.date) last.records.push(r);
      else groups.push({ date: r.date, records: [r] });
    });
    return groups;
  }

  function recordsOnDate(records, date) {
    return records.filter(function (r) { return r.date === date; });
  }

  function latestMonth(months) {
    return months.length ? months.slice().sort().reverse()[0] : null;
  }

  /** Repository rows whose name contains the query (case-insensitive). */
  function filterRepositories(repos, query) {
    var q = (query || "").trim().toLowerCase();
    return repos.filter(function (r) { return !q || r.name.toLowerCase().indexOf(q) !== -1; });
  }

  /** Rows with a record first (newest date first), then rows without; name order breaks ties. */
  function sortRepositories(repos) {
    return repos.slice().sort(function (a, b) {
      var da = a.latest ? a.latest.date : "";
      var db = b.latest ? b.latest.date : "";
      if (da !== db) return da < db ? 1 : -1;
      return a.name < b.name ? -1 : a.name > b.name ? 1 : 0;
    });
  }

  var TABS = ["recent", "daily", "repos", "notes"];

  function decodePart(part) {
    try { return decodeURIComponent(part); } catch (e) { return part; }
  }

  /**
   * Location hash -> view. "#recent" / "#daily" / "#repos" / "#notes" select a
   * tab; "#notes/<id>" opens a note and "#notes/<id>/<heading>" one of its
   * headings. Headings live under the note's own path, so a heading can never
   * be mistaken for a tab or another note. Anything unknown shows "recent".
   */
  function parseRoute(hash) {
    var parts = String(hash || "").replace(/^#/, "").split("/");
    var tab = decodePart(parts[0]);
    if (tab !== "notes") {
      return { tab: TABS.indexOf(tab) === -1 ? "recent" : tab, note: null, anchor: null };
    }
    return {
      tab: "notes",
      note: parts[1] ? decodePart(parts[1]) : null,
      anchor: parts.length > 2 && parts.slice(2).join("/") ? decodePart(parts.slice(2).join("/")) : null
    };
  }

  return {
    TABS: TABS, parseRoute: parseRoute,
    typeLabel: typeLabel, typeShort: typeShort, identifier: identifier, safeUrl: safeUrl,
    monthOf: monthOf, formatMonth: formatMonth, formatDay: formatDay, formatFullDay: formatFullDay,
    filterRecords: filterRecords, sortByDate: sortByDate, groupByDate: groupByDate,
    recordsOnDate: recordsOnDate, latestMonth: latestMonth,
    filterRepositories: filterRepositories, sortRepositories: sortRepositories
  };
});

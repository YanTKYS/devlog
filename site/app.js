/* devlog viewer UI. All text is inserted via textContent (no HTML string
 * insertion), and data is fetched with a relative path so the site works under the
 * GitHub Pages project sub-path (/<repo>/). */
(function () {
  "use strict";
  var L = window.DevlogLib;
  var DATA_URL = "data/devlog.json";
  var TABS = ["recent", "daily", "repos"];
  var data = null;
  var state = {
    tab: "recent", month: null, repo: "", type: "", order: "desc",
    day: "today", query: ""
  };

  var panel = document.getElementById("panel");
  var footer = document.getElementById("footer");

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "text") node.textContent = attrs[k];
      else if (attrs[k] !== null && attrs[k] !== undefined) node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) node.appendChild(c); });
    return node;
  }

  function select(label, options, value, onChange) {
    var sel = el("select", { "aria-label": label });
    options.forEach(function (o) {
      var opt = el("option", { value: o.value, text: o.label });
      if (o.value === value) opt.selected = true;
      sel.appendChild(opt);
    });
    sel.addEventListener("change", function () { onChange(sel.value); });
    return sel;
  }

  function stateBox(title, detail, extra) {
    return el("div", { class: "state" }, [
      el("p", { class: "state-title", text: title }),
      detail ? el("p", { class: "state-detail", text: detail }) : null,
      extra || null
    ]);
  }

  /* A record as a card. The whole card is the link to the GitHub page. */
  function card(r, opts) {
    var href = L.safeUrl(r.url);
    var node = el(href ? "a" : "div", {
      "class": "card type-" + r.type,
      href: href, target: href ? "_blank" : null, rel: href ? "noopener noreferrer" : null
    }, [
      el("div", { class: "card-head" }, [
        el("span", { class: "repo", text: r.repo }),
        el("span", { class: "ident", text: L.identifier(r) })
      ]),
      el("p", { class: "title", text: r.title || "（タイトルなし）", title: r.title || null }),
      el("div", { class: "card-foot" }, [
        el("span", { class: "badge", text: L.typeLabel(r.type) }),
        opts && opts.showDate ? el("span", { class: "card-date", text: r.date }) : null,
        href ? el("span", { class: "ext", text: "↗", "aria-label": "GitHubで開く" }) : null
      ])
    ]);
    return node;
  }

  function cardGrid(records, opts) {
    var grid = el("div", { class: "grid" });
    records.forEach(function (r) { grid.appendChild(card(r, opts)); });
    return grid;
  }

  /* ---------- tab 1: recent ---------- */
  function renderRecent() {
    panel.textContent = "";
    if (!data.records.length) {
      panel.appendChild(stateBox("表示できる記録がありません", "公開対象のリポジトリに記録がまだありません。"));
      return;
    }
    if (!state.month) state.month = L.latestMonth(data.months);

    var monthOpts = data.months.map(function (m) { return { value: m, label: L.formatMonth(m) }; });
    var repoOpts = [{ value: "", label: "すべてのリポジトリ" }].concat(
      data.repositories.map(function (r) { return { value: r.name, label: r.name }; }));
    var typeOpts = [{ value: "", label: "すべての種別" }].concat(
      ["pr", "release", "commit"].map(function (t) { return { value: t, label: L.typeLabel(t) }; }));
    var orderOpts = [{ value: "desc", label: "新しい順" }, { value: "asc", label: "古い順" }];

    var summary = el("p", { class: "summary", role: "status" });
    var results = el("div", { class: "results" });

    function update() {
      var inMonth = L.filterRecords(data.records, { month: state.month });
      var shown = L.sortByDate(
        L.filterRecords(data.records, { month: state.month, repo: state.repo, type: state.type }),
        state.order);
      var text = L.formatMonth(state.month) + "：" + shown.length + "件";
      if (shown.length !== inMonth.length) text += "（この月の全体 " + inMonth.length + "件）";
      summary.textContent = text;
      results.textContent = "";
      if (!shown.length) {
        var reset = el("button", { type: "button", "class": "link-button", text: "絞り込みを解除" });
        reset.addEventListener("click", function () {
          state.repo = ""; state.type = ""; renderRecent();
        });
        results.appendChild(stateBox("条件に一致する記録がありません", null, reset));
        return;
      }
      L.groupByDate(shown).forEach(function (g) {
        results.appendChild(el("section", { class: "day" }, [
          el("h2", { class: "day-title" }, [
            el("span", { text: L.formatDay(g.date) }),
            el("span", { class: "day-count", text: g.records.length + "件" })
          ]),
          cardGrid(g.records)
        ]));
      });
    }

    panel.appendChild(el("div", { class: "controls" }, [
      select("月", monthOpts, state.month, function (v) { state.month = v; update(); }),
      select("リポジトリ", repoOpts, state.repo, function (v) { state.repo = v; update(); }),
      select("種別", typeOpts, state.type, function (v) { state.type = v; update(); }),
      select("並び順", orderOpts, state.order, function (v) { state.order = v; update(); })
    ]));
    panel.appendChild(summary);
    panel.appendChild(results);
    update();
  }

  /* ---------- tab 2: today / yesterday ---------- */
  function renderDaily() {
    panel.textContent = "";
    var dates = { today: data.collected.today, yesterday: data.collected.yesterday };
    var segment = el("div", { class: "segment", role: "group", "aria-label": "今日・昨日" });
    var results = el("div", { class: "results" });

    function update() {
      var date = dates[state.day];
      Array.prototype.forEach.call(segment.children, function (b) {
        b.setAttribute("aria-pressed", String(b.dataset.day === state.day));
      });
      var records = L.recordsOnDate(data.records, date);
      results.textContent = "";
      results.appendChild(el("h2", { class: "day-title" }, [
        el("span", { text: L.formatFullDay(date) }),
        el("span", { class: "day-count", text: records.length + "件" })
      ]));
      if (!records.length) {
        results.appendChild(stateBox("この日の記録はありません",
          "最後の収集時点（" + data.collected.today + "）までに収集された記録がありません。"));
        return;
      }
      results.appendChild(cardGrid(records));
    }

    [["today", "今日"], ["yesterday", "昨日"]].forEach(function (d) {
      var b = el("button", { type: "button", "data-day": d[0], text: d[1] });
      b.addEventListener("click", function () { state.day = d[0]; update(); });
      segment.appendChild(b);
    });
    panel.appendChild(segment);
    panel.appendChild(el("p", { class: "notice",
      text: "最後の収集時点（" + data.collected.today + " JST）までの記録です。GitHub 上のリアルタイムの活動ではありません。" }));
    panel.appendChild(results);
    update();
  }

  /* ---------- tab 3: repositories ---------- */
  function repoCard(row) {
    var latest = row.latest;
    var href = latest ? L.safeUrl(latest.url) : null;
    var head = el("div", { class: "card-head" }, [
      el("a", { class: "repo repo-link", href: L.safeUrl(row.url), target: "_blank",
        rel: "noopener noreferrer", text: row.name, "aria-label": row.name + " のリポジトリを開く" }),
      latest ? el("span", { class: "ident", text: L.identifier(latest) }) : null
    ]);
    if (!latest) {
      return el("div", { class: "card card-empty" }, [
        head, el("p", { class: "title muted", text: "記録なし" })
      ]);
    }
    return el("div", { class: "card type-" + latest.type }, [
      head,
      el("p", { class: "title", text: latest.title || "（タイトルなし）" }),
      el("div", { class: "card-foot" }, [
        el("span", { class: "badge", text: L.typeLabel(latest.type) }),
        el("span", { class: "card-date", text: latest.date }),
        href ? el("a", { class: "ext", href: href, target: "_blank", rel: "noopener noreferrer",
          text: "↗", "aria-label": latest.title + " をGitHubで開く" }) : null
      ])
    ]);
  }

  function renderRepos() {
    panel.textContent = "";
    if (!data.repositories.length) {
      panel.appendChild(stateBox("表示できるリポジトリがありません", "config/pages.yml に公開対象が設定されていません。"));
      return;
    }
    var input = el("input", { type: "search", placeholder: "リポジトリ名で絞り込み",
      "aria-label": "リポジトリ名で絞り込み", value: state.query, autocomplete: "off" });
    var summary = el("p", { class: "summary", role: "status" });
    var results = el("div", { class: "results" });

    function update() {
      var rows = L.sortRepositories(L.filterRepositories(data.repositories, state.query));
      summary.textContent = rows.length + " / " + data.repositories.length + " リポジトリ";
      results.textContent = "";
      if (!rows.length) {
        results.appendChild(stateBox("該当するリポジトリがありません"));
        return;
      }
      var grid = el("div", { class: "grid" });
      rows.forEach(function (r) { grid.appendChild(repoCard(r)); });
      results.appendChild(grid);
    }
    input.addEventListener("input", function () { state.query = input.value; update(); });

    panel.appendChild(el("div", { class: "controls" }, [input]));
    panel.appendChild(el("p", { class: "notice",
      text: "devlog に収集済みの最新記録です（" + data.collected.today + " JST 時点）。GitHub 上の最新活動をその場で取得したものではありません。" }));
    panel.appendChild(summary);
    panel.appendChild(results);
    update();
  }

  /* ---------- shell ---------- */
  function render() {
    Array.prototype.forEach.call(document.querySelectorAll("[role=tab]"), function (t) {
      var on = t.dataset.tab === state.tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
    });
    panel.setAttribute("aria-labelledby", "tab-" + state.tab);
    if (state.tab === "daily") renderDaily();
    else if (state.tab === "repos") renderRepos();
    else renderRecent();
  }

  function setTab(tab, push) {
    state.tab = TABS.indexOf(tab) === -1 ? "recent" : tab;
    if (push && location.hash !== "#" + state.tab) history.replaceState(null, "", "#" + state.tab);
    render();
  }

  function init() {
    var tabs = document.getElementById("tabs");
    tabs.addEventListener("click", function (e) {
      var t = e.target.closest("[role=tab]");
      if (t) setTab(t.dataset.tab, true);
    });
    tabs.addEventListener("keydown", function (e) {
      var i = TABS.indexOf(state.tab);
      if (e.key === "ArrowRight") i = (i + 1) % TABS.length;
      else if (e.key === "ArrowLeft") i = (i + TABS.length - 1) % TABS.length;
      else return;
      setTab(TABS[i], true);
      document.getElementById("tab-" + TABS[i]).focus();
    });
    window.addEventListener("hashchange", function () { setTab(location.hash.slice(1), false); });
    setTab(location.hash.slice(1), false);
    footer.textContent = "最終収集日 " + data.collected.today + "（JST）・データ生成 " +
      data.generated_at.replace("T", " ").replace(/\+09:00$/, " JST") +
      "。devlog に収集済みの記録を表示しています。";
  }

  function fail(err) {
    panel.textContent = "";
    var retry = el("button", { type: "button", "class": "link-button", text: "再読み込み" });
    retry.addEventListener("click", function () { location.reload(); });
    panel.appendChild(stateBox("データを読み込めませんでした",
      "ネットワークを確認して再読み込みしてください。（" + (err && err.message ? err.message : err) + "）", retry));
  }

  fetch(DATA_URL, { cache: "no-cache" })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (json) { data = json; init(); })
    .catch(fail);
})();

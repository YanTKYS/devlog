/* devlog viewer UI. All text is inserted via textContent (no HTML string
 * insertion), and data is fetched with a relative path so the site works under the
 * GitHub Pages project sub-path (/<repo>/). Notes are parsed by markdown-lib.js
 * into a syntax tree and built here with createElement, never from HTML strings. */
(function () {
  "use strict";
  var L = window.DevlogLib;
  var M = window.MarkdownLib;
  var DATA_URL = "data/devlog.json";
  var NOTES_URL = "data/notes.json";
  var TABS = L.TABS;
  var data = null, dataError = null;
  var state = {
    tab: "recent", month: null, repo: "", type: "", order: "desc",
    day: "today", query: "", note: null, anchor: null
  };
  var notesIndex = null;     // Promise of the notes manifest
  var noteTexts = {};        // note id -> Promise of its Markdown
  var renderSeq = 0;         // drops stale async renders after navigation
  var shownNote = null;      // id of the note currently on screen
  var BASE_TITLE = document.title;

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


  /* ---------- tab 4: notes ---------- */
  function fetchText(url) {
    return fetch(url, { cache: "no-cache" }).then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.text();
    });
  }

  function loadNotesIndex() {
    if (!notesIndex) {
      notesIndex = fetchText(NOTES_URL).then(function (t) { return JSON.parse(t).notes; });
      notesIndex.catch(function () { notesIndex = null; });  // allow a retry
    }
    return notesIndex;
  }

  function loadNote(note) {
    if (!noteTexts[note.id]) {
      noteTexts[note.id] = fetchText(note.path);
      noteTexts[note.id].catch(function () { delete noteTexts[note.id]; });
    }
    return noteTexts[note.id];
  }

  function headingId(slug) { return "h-" + slug; }

  function noteError(err) {
    var retry = el("button", { type: "button", "class": "link-button", text: "再読み込み" });
    retry.addEventListener("click", function () { render(); });
    return stateBox("ノートを読み込めませんでした",
      "ネットワークを確認して再読み込みしてください。（" + (err && err.message ? err.message : err) + "）", retry);
  }

  /* Inline syntax tree -> DOM. Link targets go through MarkdownLib.resolveLink:
   * anything that is not http(s), mailto or a #notes route is shown as text. */
  function mdInline(nodes, parent, noteId) {
    nodes.forEach(function (n) {
      if (n.type === "text") parent.appendChild(document.createTextNode(n.text));
      else if (n.type === "code") parent.appendChild(el("code", { text: n.text }));
      else if (n.type === "br") parent.appendChild(el("br"));
      else if (n.type === "strong" || n.type === "em" || n.type === "del") {
        var wrap = el(n.type);
        mdInline(n.children, wrap, noteId);
        parent.appendChild(wrap);
      } else if (n.type === "link" || n.type === "image") {
        var target = M.resolveLink(n.type === "link" ? n.href : n.src, noteId);
        var node;
        if (!target) node = el("span");
        else if (target.kind === "route") node = el("a", { href: target.hash });
        else node = el("a", { href: target.href, target: "_blank", rel: "noopener noreferrer" });
        if (n.title) node.setAttribute("title", n.title);
        if (n.type === "image") node.textContent = n.alt || n.src;  // images are not loaded
        else mdInline(n.children, node, noteId);
        parent.appendChild(node);
      }
    });
  }

  function mdBlocks(blocks, parent, ctx) {
    blocks.forEach(function (b) {
      if (b.type === "heading") {
        ctx.lastHeading = b.text;
        // The site header owns <h1>, so note headings start at <h2>.
        var h = el("h" + Math.min(b.level + 1, 6), { "class": "md-h" + b.level, id: headingId(b.slug), tabindex: "-1" });
        mdInline(b.inline, h, ctx.noteId);
        parent.appendChild(h);
      } else if (b.type === "paragraph") {
        var p = el("p");
        mdInline(b.inline, p, ctx.noteId);
        parent.appendChild(p);
      } else if (b.type === "list") {
        var list = el(b.ordered ? "ol" : "ul", { start: b.ordered && b.start !== 1 ? String(b.start) : null });
        b.items.forEach(function (item) {
          var li = el("li");
          if (!b.loose && item.blocks.length && item.blocks[0].type === "paragraph") {
            mdInline(item.blocks[0].inline, li, ctx.noteId);  // tight list: no <p>
            mdBlocks(item.blocks.slice(1), li, ctx);
          } else mdBlocks(item.blocks, li, ctx);
          list.appendChild(li);
        });
        parent.appendChild(list);
      } else if (b.type === "code") {
        // Focusable so a long line can be scrolled with the keyboard.
        parent.appendChild(el("pre", { tabindex: "0" }, [el("code", { text: b.text })]));
      } else if (b.type === "blockquote") {
        var q = el("blockquote");
        mdBlocks(b.blocks, q, ctx);
        parent.appendChild(q);
      } else if (b.type === "hr") {
        parent.appendChild(el("hr"));
      } else if (b.type === "table") {
        parent.appendChild(mdTable(b, ctx));
      }
    });
  }

  /* Tables scroll inside their own focusable region, never the page. */
  function mdTable(b, ctx) {
    // Width class per column from its longest cell: "◎" or "$20" columns stay on
    // one line; prose columns keep a readable width when the table scrolls.
    var widths = b.head.map(function (inline, i) {
      var longest = [inline].concat(b.rows.map(function (r) { return r[i]; })).reduce(function (max, cellInline) {
        return Math.max(max, M.plainText(cellInline).length);
      }, 0);
      return longest <= 12 ? "col-short" : longest > 40 ? "col-long" : null;
    });
    function cell(tag, inline, i) {
      var cls = [b.align[i] ? "align-" + b.align[i] : null, widths[i]].filter(Boolean).join(" ") || null;
      var c = el(tag, { "class": cls, scope: tag === "th" ? "col" : null });
      mdInline(inline, c, ctx.noteId);
      return c;
    }
    var headRow = el("tr");
    b.head.forEach(function (inline, i) { headRow.appendChild(cell("th", inline, i)); });
    var body = el("tbody");
    b.rows.forEach(function (row) {
      var tr = el("tr");
      row.forEach(function (inline, i) { tr.appendChild(cell("td", inline, i)); });
      body.appendChild(tr);
    });
    ctx.tables += 1;
    var label = "表" + ctx.tables + (ctx.lastHeading ? "（" + ctx.lastHeading + "）" : "");
    return el("div", { "class": "table-wrap", role: "region", "aria-label": label, tabindex: "0" }, [
      el("table", null, [el("thead", null, [headRow]), body])
    ]);
  }

  function backLink() {
    return el("p", { "class": "doc-nav" }, [el("a", { href: "#notes", text: "← ノート一覧に戻る" })]);
  }

  function renderNoteList(seq) {
    panel.appendChild(el("p", { "class": "state", text: "読み込み中…" }));
    loadNotesIndex().then(function (notes) {
      if (seq !== renderSeq) return;
      panel.textContent = "";
      document.title = "ノート - " + BASE_TITLE;
      panel.appendChild(el("p", { "class": "summary", text: notes.length + "件のノート" }));
      var grid = el("div", { "class": "grid" });
      notes.forEach(function (n) {
        grid.appendChild(el("a", { "class": "card note-card", href: "#notes/" + encodeURIComponent(n.id) }, [
          el("p", { "class": "title", text: n.title }),
          el("p", { "class": "note-desc", text: n.description })
        ]));
      });
      panel.appendChild(grid);
    }, function (err) {
      if (seq !== renderSeq) return;
      panel.textContent = "";
      panel.appendChild(noteError(err));
    });
  }

  function renderNote(seq) {
    panel.appendChild(el("p", { "class": "state", text: "読み込み中…" }));
    loadNotesIndex().then(function (notes) {
      var note = notes.filter(function (n) { return n.id === state.note; })[0];
      if (!note) return null;
      return loadNote(note).then(function (text) { return { note: note, text: text }; });
    }).then(function (res) {
      if (seq !== renderSeq) return;
      panel.textContent = "";
      if (!res) {
        panel.appendChild(stateBox("ノートが見つかりません", "「" + state.note + "」という名前のノートは公開されていません。",
          el("a", { href: "#notes", text: "ノート一覧に戻る" })));
        return;
      }
      var doc = M.parse(res.text);
      var article = el("article", { "class": "doc", "aria-label": res.note.title });
      mdBlocks(doc.blocks, article, { noteId: res.note.id, lastHeading: null, tables: 0 });
      panel.appendChild(backLink());
      panel.appendChild(article);
      panel.appendChild(backLink());
      shownNote = res.note.id;
      document.title = res.note.title + " - " + BASE_TITLE;
      showAnchor(true);
    }, function (err) {
      if (seq !== renderSeq) return;
      panel.textContent = "";
      panel.appendChild(noteError(err));
    });
  }

  /* Bring the requested heading (or the top of the note) into view and give it
   * focus, so keyboard and screen-reader users land where the link pointed. */
  function showAnchor(opened) {
    var target = state.anchor ? document.getElementById(headingId(state.anchor)) : null;
    if (target) {
      target.scrollIntoView();
      target.focus({ preventScroll: true });
    } else if (opened) {
      window.scrollTo(0, 0);
      var first = panel.querySelector(".doc h2, .doc h3, .doc h4, .doc h5, .doc h6");
      if (first) first.focus({ preventScroll: true });
    }
  }

  function renderNotes() {
    var seq = renderSeq;
    panel.textContent = "";
    shownNote = null;
    if (state.note) renderNote(seq);
    else renderNoteList(seq);
  }

  /* ---------- shell ---------- */
  function render() {
    renderSeq += 1;
    Array.prototype.forEach.call(document.querySelectorAll("[role=tab]"), function (t) {
      var on = t.dataset.tab === state.tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
    });
    panel.setAttribute("aria-labelledby", "tab-" + state.tab);
    // A whole note must not be announced as a live update.
    panel.setAttribute("aria-live", state.tab === "notes" ? "off" : "polite");
    if (state.tab !== "notes") document.title = BASE_TITLE;
    if (state.tab === "notes") { renderNotes(); return; }
    if (dataError) { renderDataError(); return; }
    if (!data) {
      panel.textContent = "";
      panel.appendChild(el("p", { "class": "state", text: "読み込み中…" }));
      return;
    }
    if (state.tab === "daily") renderDaily();
    else if (state.tab === "repos") renderRepos();
    else renderRecent();
  }

  function setTab(tab, push) {
    state.tab = TABS.indexOf(tab) === -1 ? "recent" : tab;
    state.note = null;
    state.anchor = null;
    if (push && location.hash !== "#" + state.tab) history.replaceState(null, "", "#" + state.tab);
    render();
  }

  /* Hash navigation: links, direct access and the back / forward buttons. */
  function applyRoute() {
    var route = L.parseRoute(location.hash);
    if (route.tab === "notes" && state.tab === "notes" && route.note && route.note === shownNote) {
      state.anchor = route.anchor;  // same note: only move to the heading
      showAnchor(true);
      return;
    }
    state.tab = route.tab;
    state.note = route.note;
    state.anchor = route.anchor;
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
    window.addEventListener("hashchange", applyRoute);
    // A link to the heading already in the URL fires no hashchange; scroll anyway.
    panel.addEventListener("click", function (e) {
      var a = e.target.closest("a[href^='#notes/']");
      if (!a || e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
      var to = L.parseRoute(a.getAttribute("href")), now = L.parseRoute(location.hash);
      if (to.note === now.note && to.anchor === now.anchor && to.note === shownNote) {
        e.preventDefault();
        showAnchor(true);
      }
    });
    applyRoute();
  }

  function renderDataError() {
    panel.textContent = "";
    var retry = el("button", { type: "button", "class": "link-button", text: "再読み込み" });
    retry.addEventListener("click", function () { location.reload(); });
    panel.appendChild(stateBox("データを読み込めませんでした",
      "ネットワークを確認して再読み込みしてください。（" +
      (dataError && dataError.message ? dataError.message : dataError) + "）", retry));
  }

  init();
  fetch(DATA_URL, { cache: "no-cache" })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (json) {
      data = json;
      footer.textContent = "最終収集日 " + data.collected.today + "（JST）・データ生成 " +
        data.generated_at.replace("T", " ").replace(/\+09:00$/, " JST") +
        "。devlog に収集済みの記録を表示しています。";
      if (state.tab !== "notes") render();
    })
    .catch(function (err) {
      dataError = err || new Error("unknown error");
      if (state.tab !== "notes") render();
    });
})();

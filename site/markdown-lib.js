/* devlog viewer: a small Markdown parser for the published notes (no DOM).
 *
 * It turns Markdown into a plain syntax tree; app.js builds the page from
 * that tree with createElement/textContent only. No HTML string is ever
 * produced or inserted, so raw HTML in a note is shown as text and cannot
 * run. Link targets are classified by resolveLink(): only http(s)/mailto
 * links and the viewer's own #notes routes become links.
 *
 * Supported (the subset the notes use, close to GitHub Flavored Markdown):
 * ATX headings, paragraphs, bullet/ordered lists (nested, with continuation
 * lines), fenced code blocks, block quotes, thematic breaks, tables, and
 * inline code, **strong**, *emphasis*, ~~strikethrough~~, [links](url),
 * <autolinks>, backslash escapes and hard line breaks. Not supported:
 * setext headings, indented code blocks, reference links, raw HTML, entities.
 *
 * Loaded by index.html and by tests/markdown_lib.test.js (Node). */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.MarkdownLib = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var FENCE_RE = /^( {0,3})(`{3,}|~{3,})[ \t]*([^`]*?)[ \t]*$/;
  var HEADING_RE = /^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$/;
  var HR_RE = /^ {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$/;
  var QUOTE_RE = /^ {0,3}> ?(.*)$/;
  var LIST_RE = /^( {0,3})([-*+]|\d{1,9}[.)])(?:([ \t]+)(.*)|[ \t]*)$/;
  var DELIM_CELL_RE = /^:?-+:?$/;
  var PUNCT = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

  function isBlank(line) { return /^[ \t]*$/.test(line); }

  function indentOf(line) {
    var n = 0;
    for (var i = 0; i < line.length; i++) {
      if (line[i] === " ") n += 1;
      else if (line[i] === "\t") n += 4 - (n % 4);
      else break;
    }
    return n;
  }

  /** Remove up to `n` columns of leading indentation. */
  function dedent(line, n) {
    var col = 0, i = 0;
    while (i < line.length && col < n) {
      if (line[i] === " ") col += 1;
      else if (line[i] === "\t") col += 4 - (col % 4);
      else break;
      i++;
    }
    return line.slice(i);
  }

  function listMarker(line) {
    var m = LIST_RE.exec(line);
    if (!m || HR_RE.test(line)) return null;
    var ordered = /\d/.test(m[2]);
    var spaces = m[3] ? indentOf(m[3]) : 1;
    if (spaces > 4) spaces = 1;  // content starts after one space; the rest is content
    return {
      ordered: ordered,
      start: ordered ? parseInt(m[2], 10) : null,
      delim: m[2].slice(-1),
      contentIndent: m[1].length + m[2].length + spaces,
      first: m[4] === undefined ? "" : (m[3] && indentOf(m[3]) > 4 ? m[3].slice(1) : "") + m[4]
    };
  }

  /* ---------- tables ---------- */

  /** Split a table row on unescaped pipes outside code spans. */
  function splitRow(line) {
    var s = line.trim();
    if (s[0] === "|") s = s.slice(1);
    if (s.length && s[s.length - 1] === "|" && s[s.length - 2] !== "\\") s = s.slice(0, -1);
    var cells = [], cur = "", i = 0;
    while (i < s.length) {
      var ch = s[i];
      if (ch === "\\" && s[i + 1] === "|") { cur += "|"; i += 2; continue; }
      if (ch === "\\" && i + 1 < s.length) { cur += ch + s[i + 1]; i += 2; continue; }
      if (ch === "`") {
        var run = backtickRun(s, i), close = findBacktickClose(s, i + run, run);
        if (close !== -1) { cur += s.slice(i, close + run); i = close + run; continue; }
        cur += s.slice(i, i + run); i += run; continue;
      }
      if (ch === "|") { cells.push(cur.trim()); cur = ""; i++; continue; }
      cur += ch; i++;
    }
    cells.push(cur.trim());
    return cells;
  }

  function delimiterRow(line) {
    if (line.indexOf("-") === -1) return null;
    var cells = splitRow(line);
    for (var i = 0; i < cells.length; i++) if (!DELIM_CELL_RE.test(cells[i])) return null;
    return cells.map(function (c) {
      var left = c[0] === ":", right = c[c.length - 1] === ":";
      return left && right ? "center" : right ? "right" : left ? "left" : null;
    });
  }

  function isTableStart(lines, i) {
    if (i + 1 >= lines.length || lines[i].indexOf("|") === -1 || indentOf(lines[i]) > 3) return false;
    var align = delimiterRow(lines[i + 1]);
    return !!align && align.length === splitRow(lines[i]).length;
  }

  /** Does `line` start a block that interrupts a paragraph? */
  function interrupts(lines, i) {
    var line = lines[i];
    if (FENCE_RE.test(line) || HEADING_RE.test(line) || HR_RE.test(line) || QUOTE_RE.test(line)) return true;
    var m = listMarker(line);
    if (m && m.first.trim() !== "" && (!m.ordered || m.start === 1)) return true;
    return isTableStart(lines, i);
  }

  /* ---------- blocks ---------- */

  function parseBlocks(lines) {
    var blocks = [], i = 0, m;
    while (i < lines.length) {
      var line = lines[i];
      if (isBlank(line)) { i++; continue; }

      if ((m = FENCE_RE.exec(line))) {
        var fence = m[2], pad = m[1].length, body = [];
        i++;
        while (i < lines.length) {
          var close = /^ {0,3}(`{3,}|~{3,})[ \t]*$/.exec(lines[i]);
          if (close && close[1][0] === fence[0] && close[1].length >= fence.length) { i++; break; }
          body.push(dedent(lines[i], pad));
          i++;
        }
        blocks.push({ type: "code", lang: m[3].split(/\s+/)[0] || null, text: body.join("\n") });
        continue;
      }
      if ((m = HEADING_RE.exec(line))) {
        blocks.push({ type: "heading", level: m[1].length, inline: parseInline(m[2] || "") });
        i++;
        continue;
      }
      if (HR_RE.test(line)) { blocks.push({ type: "hr" }); i++; continue; }
      if (QUOTE_RE.test(line)) {
        var quoted = [];
        while (i < lines.length && !isBlank(lines[i])) {
          var q = QUOTE_RE.exec(lines[i]);
          if (q) quoted.push(q[1]);
          else if (quoted.length && !interrupts(lines, i)) quoted.push(lines[i]);  // lazy line
          else break;
          i++;
        }
        blocks.push({ type: "blockquote", blocks: parseBlocks(quoted) });
        continue;
      }
      if (listMarker(line)) { i = parseList(lines, i, blocks); continue; }
      if (isTableStart(lines, i)) {
        var head = splitRow(line), align = delimiterRow(lines[i + 1]), rows = [];
        i += 2;
        while (i < lines.length && !isBlank(lines[i]) && !interrupts(lines, i)) {
          var cells = splitRow(lines[i]);
          while (cells.length < head.length) cells.push("");
          rows.push(cells.slice(0, head.length).map(parseInline));
          i++;
        }
        blocks.push({ type: "table", align: align, head: head.map(parseInline), rows: rows });
        continue;
      }
      var para = [line.replace(/^[ \t]+/, "")];  // keep trailing spaces: "  \n" is a hard break
      i++;
      while (i < lines.length && !isBlank(lines[i]) && !interrupts(lines, i)) {
        para.push(lines[i].replace(/^[ \t]+/, ""));
        i++;
      }
      blocks.push({ type: "paragraph", inline: parseInline(para.join("\n").replace(/[ \t]+$/, "")) });
    }
    return blocks;
  }

  function parseList(lines, i, blocks) {
    var first = listMarker(lines[i]);
    var list = { type: "list", ordered: first.ordered, start: first.start, loose: false, items: [] };
    var blankBefore = false;  // blank line(s) between the previous item and this one
    while (i < lines.length) {
      var m = listMarker(lines[i]);
      if (!m || m.ordered !== first.ordered || m.delim !== first.delim) break;
      if (blankBefore) list.loose = true;
      var body = [m.first];
      i++;
      while (i < lines.length) {
        var line = lines[i];
        if (isBlank(line)) { body.push(""); i++; continue; }
        if (indentOf(line) >= m.contentIndent) { body.push(dedent(line, m.contentIndent)); i++; continue; }
        if (body[body.length - 1] !== "" && !listMarker(line) && !interrupts(lines, i)) {
          body.push(line);  // lazy continuation of the item's paragraph
          i++;
          continue;
        }
        break;
      }
      blankBefore = false;
      while (body.length > 1 && body[body.length - 1] === "") { body.pop(); blankBefore = true; }
      if (body.indexOf("") !== -1) list.loose = true;  // blank line inside the item
      list.items.push({ blocks: parseBlocks(body) });
    }
    blocks.push(list);
    return i;
  }

  /* ---------- inline ---------- */

  function backtickRun(s, i) {
    var n = 0;
    while (s[i + n] === "`") n++;
    return n;
  }

  /** Index of a closing backtick run of exactly `len`, or -1. */
  function findBacktickClose(s, from, len) {
    var j = from;
    while (j < s.length) {
      if (s[j] === "`") {
        var run = backtickRun(s, j);
        if (run === len) return j;
        j += run;
      } else j++;
    }
    return -1;
  }

  /** Matching "]" for the "[" at `open`, skipping escapes, code spans and nesting. */
  function findBracketClose(s, open) {
    var depth = 0;
    for (var j = open; j < s.length; j++) {
      var ch = s[j];
      if (ch === "\\") { j++; continue; }
      if (ch === "`") {
        var run = backtickRun(s, j), close = findBacktickClose(s, j + run, run);
        if (close !== -1) { j = close + run - 1; continue; }
        j += run - 1;
        continue;
      }
      if (ch === "[") depth++;
      else if (ch === "]" && --depth === 0) return j;
    }
    return -1;
  }

  /** Parse "(dest "title")" starting at `i` (the "("). Returns {href, title, end} or null. */
  function parseLinkTail(s, i) {
    if (s[i] !== "(") return null;
    var j = i + 1;
    while (s[j] === " " || s[j] === "\t" || s[j] === "\n") j++;
    var href = "";
    if (s[j] === "<") {
      var gt = s.indexOf(">", j);
      if (gt === -1 || /[\n<]/.test(s.slice(j + 1, gt))) return null;
      href = s.slice(j + 1, gt);
      j = gt + 1;
    } else {
      var depth = 0;
      while (j < s.length) {
        var ch = s[j];
        if (ch === "\\" && j + 1 < s.length && PUNCT.indexOf(s[j + 1]) !== -1) { href += s[j + 1]; j += 2; continue; }
        if (/\s/.test(ch)) break;
        if (ch === "(") depth++;
        else if (ch === ")") { if (depth === 0) break; depth--; }
        href += ch;
        j++;
      }
    }
    while (s[j] === " " || s[j] === "\t" || s[j] === "\n") j++;
    var title = null;
    if (s[j] === '"' || s[j] === "'") {
      var endQ = s.indexOf(s[j], j + 1);
      if (endQ === -1) return null;
      title = s.slice(j + 1, endQ);
      j = endQ + 1;
      while (s[j] === " " || s[j] === "\t" || s[j] === "\n") j++;
    }
    if (s[j] !== ")") return null;
    return { href: href, title: title, end: j + 1 };
  }

  /** Closing delimiter run for emphasis, skipping code spans, links and escapes. */
  function findEmphasisClose(s, from, ch, len) {
    for (var j = from; j < s.length; j++) {
      var c = s[j];
      if (c === "\\") { j++; continue; }
      if (c === "`") {
        var run = backtickRun(s, j), close = findBacktickClose(s, j + run, run);
        if (close !== -1) { j = close + run - 1; continue; }
        j += run - 1;
        continue;
      }
      if (c === "[") {
        var rb = findBracketClose(s, j);
        if (rb !== -1 && parseLinkTail(s, rb + 1)) { j = parseLinkTail(s, rb + 1).end - 1; continue; }
      }
      if (c === ch) {
        var n = 0;
        while (s[j + n] === ch) n++;
        var before = s[j - 1], after = s[j + n];
        var closes = n >= len && before !== undefined && !/\s/.test(before) && j > from;
        if (closes && ch === "_" && after !== undefined && /[\p{L}\p{N}]/u.test(after)) closes = false;
        if (closes) return j;
        j += n - 1;
      }
    }
    return -1;
  }

  function parseInline(src) {
    var out = [], text = "", s = src, i = 0;
    function flush() { if (text) { out.push({ type: "text", text: text }); text = ""; } }

    while (i < s.length) {
      var ch = s[i];

      if (ch === "\\") {
        if (s[i + 1] === "\n") { flush(); out.push({ type: "br" }); i += 2; continue; }
        if (i + 1 < s.length && PUNCT.indexOf(s[i + 1]) !== -1) { text += s[i + 1]; i += 2; continue; }
        text += ch; i++; continue;
      }
      if (ch === "\n") {
        if (/ {2,}$/.test(text)) { text = text.replace(/ +$/, ""); flush(); out.push({ type: "br" }); }
        else { text = text.replace(/ +$/, ""); text += "\n"; }
        i++;
        while (s[i] === " ") i++;
        continue;
      }
      if (ch === "`") {
        var run = backtickRun(s, i), close = findBacktickClose(s, i + run, run);
        if (close === -1) { text += s.slice(i, i + run); i += run; continue; }
        var code = s.slice(i + run, close).replace(/\n/g, " ");
        if (/^ .*[^ ].* $/.test(code)) code = code.slice(1, -1);
        flush();
        out.push({ type: "code", text: code });
        i = close + run;
        continue;
      }
      if (ch === "<") {
        var auto = /^<([a-zA-Z][a-zA-Z0-9+.-]{1,31}:[^<>\s]*)>/.exec(s.slice(i));
        if (auto) {
          flush();
          out.push({ type: "link", href: auto[1], title: null, children: [{ type: "text", text: auto[1] }] });
          i += auto[0].length;
          continue;
        }
        text += ch; i++; continue;  // raw HTML stays literal text
      }
      if (ch === "[" || (ch === "!" && s[i + 1] === "[")) {
        var isImage = ch === "!", open = isImage ? i + 1 : i;
        var rb = findBracketClose(s, open);
        var tail = rb !== -1 ? parseLinkTail(s, rb + 1) : null;
        if (tail) {
          flush();
          var label = s.slice(open + 1, rb);
          if (isImage) out.push({ type: "image", src: tail.href, alt: label, title: tail.title });
          else out.push({ type: "link", href: tail.href, title: tail.title, children: parseInline(label) });
          i = tail.end;
          continue;
        }
        text += s.slice(i, open + 1); i = open + 1; continue;
      }
      if (ch === "~" && s[i + 1] === "~" && s[i + 2] !== "~" && s[i + 2] !== undefined && !/\s/.test(s[i + 2])) {
        var endDel = findEmphasisClose(s, i + 2, "~", 2);
        if (endDel !== -1) {
          flush();
          out.push({ type: "del", children: parseInline(s.slice(i + 2, endDel)) });
          i = endDel + 2;
          continue;
        }
      }
      if (ch === "*" || ch === "_") {
        var n = 0;
        while (s[i + n] === ch) n++;
        var next = s[i + n], prev = s[i - 1];
        var canOpen = next !== undefined && !/\s/.test(next) &&
          !(ch === "_" && prev !== undefined && /[\p{L}\p{N}]/u.test(prev));
        var len = Math.min(n, 3), endEm = canOpen ? findEmphasisClose(s, i + len, ch, len) : -1;
        while (canOpen && endEm === -1 && len > 1) { len--; endEm = findEmphasisClose(s, i + len, ch, len); }
        if (endEm !== -1) {
          text += s.slice(i, i + n - len);
          flush();
          var inner = parseInline(s.slice(i + n, endEm));
          var node = len === 1 ? { type: "em", children: inner }
            : len === 2 ? { type: "strong", children: inner }
            : { type: "strong", children: [{ type: "em", children: inner }] };
          out.push(node);
          i = endEm + len;
          continue;
        }
        text += s.slice(i, i + n); i += n; continue;
      }
      text += ch;
      i++;
    }
    flush();
    return out;
  }

  /* ---------- headings, links ---------- */

  function plainText(nodes) {
    return nodes.map(function (n) {
      if (n.type === "text" || n.type === "code") return n.text;
      if (n.type === "image") return n.alt;
      if (n.type === "br") return " ";
      return plainText(n.children || []);
    }).join("");
  }

  /** GitHub-compatible heading slugs ("## A. 概要" -> "a-概要"), de-duplicated per document. */
  function createSlugger() {
    var seen = Object.create(null);  // same de-duplication as github-slugger
    return function slug(text) {
      var base = text.toLowerCase().replace(/[^\p{L}\p{M}\p{N}\p{Pc} -]/gu, "").replace(/ /g, "-");
      var s = base;
      while (s in seen) {
        seen[base]++;
        s = base + "-" + seen[base];
      }
      seen[s] = 0;
      return s;
    };
  }

  /** Parse a document and give every heading its slug: {blocks, headings: [{level, text, slug}]}. */
  function parse(src) {
    var lines = String(src).replace(/\r\n?/g, "\n").split("\n");
    var blocks = parseBlocks(lines), slug = createSlugger(), headings = [];
    (function walk(list) {
      list.forEach(function (b) {
        if (b.type === "heading") {
          b.text = plainText(b.inline).trim();
          b.slug = slug(b.text);
          headings.push({ level: b.level, text: b.text, slug: b.slug });
        } else if (b.type === "blockquote") walk(b.blocks);
        else if (b.type === "list") b.items.forEach(function (it) { walk(it.blocks); });
      });
    })(blocks);
    return { blocks: blocks, headings: headings };
  }

  /**
   * Decide what a link target may become in the viewer:
   *   {kind: "route", hash}    a #notes route (another note, or a heading of this one)
   *   {kind: "external", href} an http(s) or mailto link, opened in a new tab
   *   null                      anything else (relative paths, javascript:, data:, ...): text only
   */
  function resolveLink(href, noteId) {
    var h = String(href || "").trim();
    if (/^#notes(?:\/|$)/.test(h)) return { kind: "route", hash: h };
    if (h[0] === "#") return { kind: "route", hash: "#notes/" + noteId + "/" + h.slice(1) };
    if (/^(?:https?:\/\/|mailto:)[^\s]*$/i.test(h)) return { kind: "external", href: h };
    return null;
  }

  return {
    parse: parse, parseInline: parseInline, createSlugger: createSlugger,
    plainText: plainText, resolveLink: resolveLink
  };
});

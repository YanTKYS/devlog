// Tests for site/markdown-lib.js (run: node --test tests/site_lib.test.js tests/markdown_lib.test.js)
"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const M = require("../site/markdown-lib.js");

const blocks = (src) => M.parse(src).blocks;
const text = (s) => ({ type: "text", text: s });
const inline = (src) => M.parseInline(src);

test("headings: levels 1-6, closing hashes, GitHub slugs", () => {
  const doc = M.parse("# Title\n## A. 概要\n### C. 料金・利用制限の比較 ##\n#### x\n##### y\n###### z\n#######  not");
  assert.deepEqual(doc.headings.map((h) => h.level), [1, 2, 3, 4, 5, 6]);
  assert.deepEqual(doc.headings.map((h) => h.slug), ["title", "a-概要", "c-料金利用制限の比較", "x", "y", "z"]);
  assert.equal(doc.blocks[6].type, "paragraph");
});

test("slugs: inline markup is stripped and duplicates are numbered like GitHub", () => {
  const doc = M.parse("## `code` and **bold** [link](x)\n## 補足: その他の製品\n# A\n# A\n# A-1\n# A");
  assert.deepEqual(doc.headings.map((h) => h.slug),
    ["code-and-bold-link", "補足-その他の製品", "a", "a-1", "a-1-1", "a-2"]);
});

test("paragraphs and soft / hard line breaks", () => {
  const b = blocks("first line\nsecond line\n\nnext  \nhard\\\nbreak");
  assert.equal(b.length, 2);
  assert.deepEqual(b[0].inline, [text("first line\nsecond line")]);
  assert.deepEqual(b[1].inline.map((n) => n.type), ["text", "br", "text", "br", "text"]);
});

test("lists: tight, nested, ordered and continuation lines", () => {
  const b = blocks("- a\n- **b**\n  → continued\n  - nested\n- c\n\n3. three\n4. four");
  assert.equal(b[0].type, "list");
  assert.equal(b[0].loose, false);
  assert.equal(b[0].items.length, 3);
  const second = b[0].items[1].blocks;
  assert.equal(second[0].type, "paragraph");
  assert.deepEqual(second[0].inline.map((n) => n.type), ["strong", "text"]);
  assert.equal(second[0].inline[1].text, "\n→ continued");
  assert.equal(second[1].type, "list");
  assert.equal(b[1].ordered, true);
  assert.equal(b[1].start, 3);
});

test("lists: blank lines between items make the list loose", () => {
  assert.equal(blocks("- a\n\n- b")[0].loose, true);
  assert.equal(blocks("- a\n- b")[0].loose, false);
});

test("inline: strong, emphasis, code, strikethrough, escapes", () => {
  assert.deepEqual(inline("**太字**で"), [{ type: "strong", children: [text("太字")] }, text("で")]);
  assert.deepEqual(inline("*em* and _em_"), [
    { type: "em", children: [text("em")] }, text(" and "), { type: "em", children: [text("em")] }]);
  assert.deepEqual(inline("snake_case_name"), [text("snake_case_name")]);
  assert.deepEqual(inline("`a ** b`"), [{ type: "code", text: "a ** b" }]);
  assert.deepEqual(inline("`` a`b ``"), [{ type: "code", text: "a`b" }]);
  assert.deepEqual(inline("~~old~~"), [{ type: "del", children: [text("old")] }]);
  assert.deepEqual(inline("\\*not\\* 2 * 3"), [text("*not* 2 * 3")]);
  assert.deepEqual(inline("**unclosed"), [text("**unclosed")]);
});

test("inline: links, titles, parentheses and autolinks", () => {
  assert.deepEqual(inline("[公式](https://example.com/a_(b)) x"), [
    { type: "link", href: "https://example.com/a_(b)", title: null, children: [text("公式")] }, text(" x")]);
  assert.deepEqual(inline('[t](<https://e.com/a b> "Title")')[0], {
    type: "link", href: "https://e.com/a b", title: "Title", children: [text("t")] });
  assert.equal(inline("[**b** `c`](#x)")[0].children.length, 3);
  assert.deepEqual(inline("<https://e.com>")[0].href, "https://e.com");
  assert.deepEqual(inline("[not a link] (x)"), [text("[not a link] (x)")]);
  assert.deepEqual(inline("![alt](https://e.com/i.png)")[0], { type: "image", src: "https://e.com/i.png", alt: "alt", title: null });
});

test("raw HTML is kept as literal text", () => {
  assert.deepEqual(inline('<img src=x onerror="alert(1)"> <b>x</b>'), [text('<img src=x onerror="alert(1)"> <b>x</b>')]);
  const b = blocks("<script>alert(1)</script>");
  assert.deepEqual(b, [{ type: "paragraph", inline: [text("<script>alert(1)</script>")] }]);
});

test("tables: alignment, escaped pipes, code spans and ragged rows", () => {
  const b = blocks("| a | b | c |\n| :--- | :---: | ---: |\n| `x|y` | a \\| b | 3 |\n| only |\n| 1 | 2 | 3 | 4 |\n\nafter");
  const t = b[0];
  assert.equal(t.type, "table");
  assert.deepEqual(t.align, ["left", "center", "right"]);
  assert.deepEqual(t.rows[0][0], [{ type: "code", text: "x|y" }]);
  assert.deepEqual(t.rows[0][1], [text("a | b")]);
  assert.deepEqual(t.rows[1], [[text("only")], [], []]);
  assert.equal(t.rows[2].length, 3);
  assert.equal(b[1].type, "paragraph");
  assert.equal(blocks("a | b\nnot a delimiter")[0].type, "paragraph");
});

test("fenced code blocks are not parsed as Markdown", () => {
  const b = blocks("```js\nconst a = **1**; // [x](javascript:y)\n<b>\n```\nafter");
  assert.deepEqual(b[0], { type: "code", lang: "js", text: "const a = **1**; // [x](javascript:y)\n<b>" });
  assert.equal(b[1].type, "paragraph");
  assert.equal(blocks("~~~\nunterminated")[0].text, "unterminated");
});

test("block quotes and thematic breaks", () => {
  const b = blocks("> quoted **x**\n> - item\n\n---\n***");
  assert.equal(b[0].type, "blockquote");
  assert.deepEqual(b[0].blocks.map((x) => x.type), ["paragraph", "list"]);
  assert.deepEqual(b.slice(1).map((x) => x.type), ["hr", "hr"]);
});

test("resolveLink: only http(s), mailto and #notes routes become links", () => {
  assert.deepEqual(M.resolveLink("https://e.com/x", "n"), { kind: "external", href: "https://e.com/x" });
  assert.deepEqual(M.resolveLink("HTTP://E.COM", "n"), { kind: "external", href: "HTTP://E.COM" });
  assert.deepEqual(M.resolveLink("mailto:a@b.c", "n"), { kind: "external", href: "mailto:a@b.c" });
  assert.deepEqual(M.resolveLink("#notes/other", "n"), { kind: "route", hash: "#notes/other" });
  assert.deepEqual(M.resolveLink("#notes", "n"), { kind: "route", hash: "#notes" });
  assert.deepEqual(M.resolveLink("#a-概要", "n"), { kind: "route", hash: "#notes/n/a-概要" });
  for (const bad of ["javascript:alert(1)", " JavaScript:alert(1)", "data:text/html,x", "vbscript:x",
    "../data/x.md", "/abs", "//evil.example", "file:///etc/passwd", "https://e.com/a b", ""]) {
    assert.equal(M.resolveLink(bad, "n"), null, bad);
  }
});

test("published notes: every in-document link resolves to a heading", () => {
  for (const name of ["free-apis.md", "ai-coding-tools.md"]) {
    const src = fs.readFileSync(path.join(__dirname, "..", "notes", name), "utf8");
    const doc = M.parse(src);
    const slugs = new Set(doc.headings.map((h) => h.slug));
    const anchors = [...src.matchAll(/\]\(#([^)]+)\)/g)].map((m) => m[1]);
    for (const a of anchors) assert.ok(slugs.has(a), `${name}: #${a}`);
    const tables = (src.match(/^\| ?:?-{3}/gm) || []).length;
    const count = (list) => list.reduce((n, b) => n + (b.type === "table" ? 1 : 0) +
      (b.type === "list" ? b.items.reduce((m, it) => m + count(it.blocks), 0) : 0), 0);
    assert.equal(count(doc.blocks), tables, `${name}: tables`);
  }
});

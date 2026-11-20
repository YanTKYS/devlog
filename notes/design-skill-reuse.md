# 独自デザインのAgent Skill化と別AIへの移植（2026年11月）

[design-lab](https://github.com/YanTKYS/design-lab) で制作した独自デザイン「糸の交点」を Agent Skill にまとめ、制作とは別の AI が別リポジトリの既存 Web アプリへ適用した PoC の振り返り。次にデザインを作る・再利用するときの手順と注意点を残す。経緯の詳細は各 Issue・PR を参照。

- 期間: 2026-11-19〜11-20
- 役割: 設計 Astra／design-lab の実装 Claude Code（Opus）／移植 Codex／最終レビュー ChatGPT／判断・マージ 利用者

## 1. 目的と結論

- **課題**: 汎用 UI デザインの比較だけでなく、沖縄の文化から着想した、業務で使いやすい独自デザインを作る（[design-lab Issue #31](https://github.com/YanTKYS/design-lab/issues/31)）
- **成果**: 宮古上布の経糸・緯糸・絣に着想した「糸の交点」（仮称）を制作し、design-lab の9番目の比較デザインとして登録した。Skill `okinawa-thread-ui` を作り、Codex が markdown-library と okinawa-watch の2サイトに適用した
- **評価**: **今回の条件で再利用 PoC が成立した**。すべての AI・アプリへの汎用性や、Skill の自動選択までは証明していない

## 2. 開発の流れ

| 工程 | 担当 | 内容 | 一次情報 |
| --- | --- | --- | --- |
| 1. 探索・選択 | Astra | 「琉球モダン」に限定せず、A案「庇と通路」とB案「糸の交点」をモックで比較。利用者がB案を選択 | [#31](https://github.com/YanTKYS/design-lab/issues/31)・[PR #32](https://github.com/YanTKYS/design-lab/pull/32)・[#33](https://github.com/YanTKYS/design-lab/issues/33) |
| 2. 動く独立試作 | Opus | 申請一覧・フォーム・ダッシュボードを操作できる形で試作。利用者が「わかりやすい、かつ過剰でない」と評価 | [PR #34](https://github.com/YanTKYS/design-lab/pull/34)・[#35](https://github.com/YanTKYS/design-lab/issues/35) |
| 3. 正式統合 | Opus | 9番目の比較デザインとして登録し、既存8デザインと同じ仕組みで比較可能に。独立試作と旧「彩」は保存 | [PR #36](https://github.com/YanTKYS/design-lab/pull/36) |
| 4. Skill化 | Opus | `SKILL.md`・参照資料・最小限のトークン・自作SVGを抽出。元CSS（約1,300行）は移植せず、業務メモで初回PoC | [#37](https://github.com/YanTKYS/design-lab/issues/37)・[PR #38](https://github.com/YanTKYS/design-lab/pull/38)・[Skill正本](https://github.com/YanTKYS/design-lab/tree/main/skills/okinawa-thread-ui) |
| 5. 別AIへの移植 | Codex | Skill を明示的に読み、元の実装を参照しない条件で2つの既存サイトへ適用 | markdown-library [#10](https://github.com/YanTKYS/markdown-library/issues/10)・[PR #11](https://github.com/YanTKYS/markdown-library/pull/11)／okinawa-watch [#11](https://github.com/YanTKYS/okinawa-watch/issues/11)・[PR #12](https://github.com/YanTKYS/okinawa-watch/pull/12) |
| 6. レビュー・判断 | Astra・ChatGPT・利用者 | Astra が Issue に一次レビュー（合否ゲートにはしない）、ChatGPT が PR に最終レビュー。利用者が判断・マージ | 各 Issue・PR |

## 3. Skill の核になったもの

- **色だけでなく読み順と配置規則**: 「章 → 項目名 → 値」の縦軸、格子帯、二重罫、行型の指標。`SKILL.md` は見た目の貼り付けではなく、読み順を対象の業務に合わせて組み直すことを目的に置いた
- **必須の規則と調整してよい点を分ける**: コピーするのは意図と最小限の素材（`tokens.css`・`thread-pattern.svg`）で、専用の HTML・JS・巨大な CSS ではない
- **適用側は用途に合わせる**: markdown-library はタイトルを識別軸にし、長文には明るい読書面。okinawa-watch は「タイトル → 開催日・期限の確認状態」の順。業務用の KPI や入力欄を無関係な画面に足さない
- **文化的着想と伝統図案を混同しない**: 宮古上布の公式な意匠や沖縄全域を代表する様式ではないと Skill に明記した

## 4. 試行で分かった注意点

- **375px で検索結果までが遠い**: markdown-library で Astra が改善候補に挙げた（[一次レビュー](https://github.com/YanTKYS/markdown-library/issues/10#issuecomment-7034310535)）。利用者の短時間の試用では支障がなかった（[okinawa-watch #11](https://github.com/YanTKYS/okinawa-watch/issues/11) に記録）ため、必須修正にはしなかった
- **「開催日未確認」ラベルが遅く出る**: okinawa-watch の 375px で Astra が指摘（[一次レビュー](https://github.com/YanTKYS/okinawa-watch/issues/11#issuecomment-7040825945)）。ニュースの正確性に関わるためタイトル直後へ移してからマージした。装飾の一貫性より誤認防止を優先した
- **SVG の相対パス**: Skill の先行レビューで参照資料と SVG のパスの食い違いが見つかった（PR #38）。移植では「適用先 CSS から見た相対パス」を条件にし、最終レビューで確認した
- **レビューを重くしない**: 形式的なテスト増量や大きなレビュー待ちは設けず、代表画面・代表操作で判断した

## 5. 確認済み／未検証

| 今回確認できたこと | 未検証・一般化できないこと |
| --- | --- |
| 設計者の意図（読み順・配置規則）を Skill に記述できた | 別の設計者が同じ品質で Skill を作れること。業務メモの見本は Skill と同じ作業で作ったもので、独立した再現ではない |
| Codex が Skill の文書・素材を明示的に読み、用途の異なる2リポジトリへ適用した | Codex や Claude Code が起動時に Skill を自動認識・自動選択すること（各PRで「未確認」と記載） |
| 提出画面・差分・代表操作の報告と、Astra・ChatGPT のレビューで妥当性を評価した。CI は okinawa-watch で成功、markdown-library は結果を取得できず実装者の Chromium 確認による | 実機の日本語 IME、スクリーンリーダー、Chromium 以外のブラウザ、実機スマートフォンでの品質。あらゆる Web アプリへの適合 |
| markdown-library は利用者が短時間試用し、目立った支障がなかった | okinawa-watch を含む長期利用での可読性・UX の定量評価 |

## 6. 次回のための手順

**探索 → 動く独立画面 → 実用評価 → Skill化 → 別AI・別用途へ移植 → 設計者／実装レビュアーで評価 → 利用者が判断**

- 見た目の一貫性だけでなく、対象サイトの情報と操作の意味が保たれているかを見る
- 移植の Issue には、参照してよい資料（Skill のみ）と参照しない資料（元の実装）を明記する
- 同じ方式をほかのデザインで試す価値はあるが、今回1例の結果を万能な標準手法とは断定しない
- Skill を増やすこと自体を目的にしない

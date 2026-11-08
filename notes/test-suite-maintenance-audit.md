# 継続開発リポジトリのテスト保守調査

調査日: 2026-11-08（JST）。[devlog #23](https://github.com/YanTKYS/devlog/issues/23) の第1段階。
**後続作業を勧める候補は5リポジトリ。テスト全体の一律削減は勧めない。**

## 範囲と判断方法

- 接続アカウントでYanTKYS所有の63リポジトリを列挙し、次ページが空であることまで確認。全件`archived=false`だが、継続判定にはREADME、運用文書、Issue/PRを使用した。
- 25件を既存の自動テスト・成果物/データ検証の調査対象とした。10件は停止等で除外、1件は凍結解除未確認で保留、27件は現行チェックアウトに整理対象の自動suiteなし。下表で全63件を扱う。
- 既定ブランチの追跡ファイル一覧、Workflow全文、package/build設定、テスト本体と関連実装を確認した。検索結果だけで「テストなし」としていない。PyInstallerの`.spec`、架空ファイル生成、製品内のPACテスト機能は開発回帰suiteと区別した。
- 基準は[lg_toolkit_guide §9](https://github.com/YanTKYS/lg_toolkit_guide/blob/main/guides/01_ai_coding_rules.md#9-テスト)、同[#46](https://github.com/YanTKYS/lg_toolkit_guide/issues/46)・[PR #47](https://github.com/YanTKYS/lg_toolkit_guide/pull/47)。[NestSuite方針](https://github.com/YanTKYS/nestsuite/blob/main/docs/development/test-suite-policy.md)・[PR #603](https://github.com/YanTKYS/nestsuite/pull/603)は参考のみ。
- 分類は「維持」「削除候補」「統合・置換候補」「要判断」。静的検査でもデータ保護、認証/権限、課金/Secret境界、配布の実用上必要な契約は残す。名称・版番号・assert数だけで判断しない。
- 今回はコードを読んだ保守性評価。各アプリのsuite・実機・外部APIを実行した結果ではなく、実行時間短縮やCI失敗頻度は未計測。候補の効果は更新時の追随箇所削減であり、速度向上の数値を推測しない。

## 対象判定

### 停止・休止等により除外／判定保留

| 判定 | リポジトリ・根拠 |
| --- | --- |
| 除外（Issue指定の9件） | [ideanest #98](https://github.com/YanTKYS/ideanest/issues/98)、[chatnest #23](https://github.com/YanTKYS/chatnest/issues/23)、[nestsuite #612](https://github.com/YanTKYS/nestsuite/issues/612)、[pdfengine休止記録](../projects/pdfengine.md)、[md2doc #64](https://github.com/YanTKYS/md2doc/issues/64)、[maskedpi #11](https://github.com/YanTKYS/maskedpi/issues/11)、[recorder #151](https://github.com/YanTKYS/recorder/issues/151)、[speech2text #1](https://github.com/YanTKYS/speech2text/issues/1)、[addresscvt #6](https://github.com/YanTKYS/addresscvt/issues/6)。テストの棚卸し・整理はしていない。 |
| 追加除外 | [itoman-reiki #2](https://github.com/YanTKYS/itoman-reiki/issues/2)がopenの開発保留。自動取得基盤が成立するまで保留する方針。 |
| 要判断・今回保留 | [txt2voice v0.9.0](https://github.com/YanTKYS/txt2voice/blob/main/release-notes/v0.9.0.md)に機能凍結を明記。その後v1.0.1や修正PRがあるが、凍結解除の明示を確認できず安全側に外した。現行のCore/WindowsテストとCIの存在確認までで、削除候補は出さない。 |

`memoez`は[#64](https://github.com/YanTKYS/memoez/issues/64)の開発保留がclosed（2026-10-29）となり、後続[#79](https://github.com/YanTKYS/memoez/issues/79)・[#81](https://github.com/YanTKYS/memoez/issues/81)で正式公開・運用変更が具体的に依頼されているため対象へ戻した。単に最終更新日が新しいからではない。

### 現行チェックアウトに整理対象suiteがない27件

いずれも追跡ファイル・設定・README（ある場合）・Workflowを確認。これはテスト新設の提案ではなく、既存テスト整理の対象外という判定。継続開発中との確定も不要なので、テストのないものを無理に「アクティブ」に数えない。

| 区分 | リポジトリ | 確認内容・推奨 |
| --- | --- | --- |
| 主に単体HTML/ASP/小規模アプリ（17件） | chouseisan、whiteboard、giin_iinkai、giin_zaiseki、gyoumu_flow、pingez、quotaplayer、nestlite、clock、signage、fusen、kanban、since、proxypac、winevtview、mailexporter、markdown-library | 実装と手動確認資料が中心。Pages/release Workflowは公開・ビルド用途。proxypacの登録URL回帰確認は製品機能。今回は変更不要。 |
| Python/.NET製アプリ等（5件） | marp2pptx、embed_qr_links_pdf、web2archive、jinji_hyouka、moviecvt | `.spec`はPyInstaller設定。ビルド手順・アプリ実装が中心で、既存suite整理は不要。 |
| 文書・ガイド・補助ツール（5件） | lg_tool_fs_05_context_re3、lg_toolkit、lg_toolkit_guide、prompt、sharescan-ps | 文書/生成補助が中心。`sharescan-ps/samples/create_test_files.ps1`はサンプル生成でassertするsuiteではない。今回は変更不要。 |

### 調査対象25件：現行テスト・CI・維持すべき保証

各リポジトリ名のリンクは確認したコミット。継続対象の根拠は、現行READMEに記載された利用/開発・配布手順とIssue/PRの変更継続（例: benri #165、editor #36、sheltermatch #57、devlog #21、ai-watch #54、memonow #33）。更新の少ないmanagead・sharescan等は、停止方針がない保守対象として扱い、活発さを断定しない。

| リポジトリ・確認版 | テスト構成・実行方法 | 維持する具体例/責務 | 推奨判断 |
| --- | --- | --- | --- |
| [managead `02a84f5d62`](https://github.com/YanTKYS/managead/tree/02a84f5d6208c77970efb6116a2cc443516bccbd) | `ManageAdTool.Tests/`／`build.yml`の`dotnet test` | `ChangeSetTests`、`UserEditPolicyServiceTests`、`DirectoryServicesWriteServiceValidationTests`、監査ログの秘密値マスク。AD接続前の禁止属性拒否を実呼出しで検証。 | 維持。AD実機・権限の統合確認を代替するとは扱わない。 |
| [memoez `864b60dc79`](https://github.com/YanTKYS/memoez/tree/864b60dc7999b1668ace4472c165c918f0ef2235) | `src/**/__tests__/`のJest、`tools/tests/`のunittest、更新AndroidモジュールのJUnit。`android-build.yml`・`release-signed-apk.yml`で実行 | `backupJson.test.ts`の復元・重複、`useEditNote.test.ts`の競合保存、`ApkSafetyTest.kt`の改ざん・別署名拒否、`test_release.py`の公開承認。 | 維持。定型ラベル検査はあるが単独整理の効果が小さく、今回の優先候補にしない。 |
| [memonow `f78556ae01`](https://github.com/YanTKYS/memonow/tree/f78556ae016c7b17251884287cb0ff5c4f9f2b44) | `app/src/test/`、`androidTest/`、`tools/tests/`。`android.yml`のunit・端末テスト、`release.yml`の公開ゲート | `BackupTest.kt`、`MoodMigrationTest.kt`、`UpdateVerifierDeviceTest.kt`、`test_release_plan.py`の旧版拒否。`MetadataTest.kt`は単なるメタ情報存在検査でなく、許可取消・編集競合・位置/天気取得の失敗を検証。 | 維持。版・schema・署名の比較を表示版の固定値テストと混同しない。 |
| [benri `073a53685a`](https://github.com/YanTKYS/benri/tree/073a53685a1e8a03fa375485896c4ffccf1e301a) | `test/*.test.mjs`を`node --test`（READMEに任意実行、CIなし） | `list-compare.test.mjs`の先頭ゼロ・明示的な正規化・TSV、`notice-docx.test.mjs`の生成DOCX内容。 | 維持。異なる入力条件は重複と決めない。 |
| [editor `ceb2f4442a`](https://github.com/YanTKYS/editor/tree/ceb2f4442a13bd6ed2fb51130b6de5d8ed55bd0d) | Vitest unit、Playwright E2E、`tests/release/run.sh`。`ci.yml`で型・unit・ZIP・E2E、releaseでもゲート | `backup.test.ts`、`persistence.test.ts`、`fileSafety.spec.ts`、文字コード/BOM、Undo/Redo、リリース成果物。 | 維持。unitとE2Eはロジックと画面結線を別々に保証している。 |
| [sheltermatch `42e7376677`](https://github.com/YanTKYS/sheltermatch/tree/42e7376677acd763578a132885064f221ee729cb) | `test/`のunittest／`ci.yml` | Notebookを実行する`test_address_conversion.py`、ハザード・設定反映・ZIP異常系、`test_notebook_module_source.py`の外部モジュール取得先。 | C4のみ統合候補。住所・ハザード・出典/取得先の保証は維持。 |
| [devlog `5ddf6a6a23`](https://github.com/YanTKYS/devlog/tree/5ddf6a6a23d50e354fbe0f2934f87d7720dee17e) | `tests/`のPython・Node／`pages.yml`で実行してから生成 | 公開許可リスト、リンク書換、生成先削除防止、Markdown危険URL拒否、`site_lib.test.js`のURL条件復元。 | C3のみ縮退候補。公開範囲と生成物の検査は維持。 |
| [news-watch `d86aa54a55`](https://github.com/YanTKYS/news-watch/tree/d86aa54a55f27f38140fb554123bb71be916d238) | `tests/`のunittest（Node呼出しも含む）／`test.yml` | 重複排除、収集/レビュー出力、検索、API回数・料金に関わる確認フラグとSecret/Artifact範囲（`test_plamo_workflow.py`等）。 | 変更不要。Workflowを静的に読む検査にも、誤課金・情報流出を防ぐ責務がある。 |
| [ai-watch `5f71618e9c`](https://github.com/YanTKYS/ai-watch/tree/5f71618e9cf080298e634d8e29bba93bd8236477) | Python・Node・Playwright／`test.yml` | `test_collect.py`のログ保護、`test_selection_quality.py`の選定品質、`test_view_url.cjs`とE2Eの条件復元、API・Secretの隔離。 | C2を推奨。安全上のWorkflow条件は残す。 |
| [okinawa-watch `08aba87359`](https://github.com/YanTKYS/okinawa-watch/tree/08aba8735939e2d9c694ab3872eb62683c13a76d) | Python・Node／`check.yml`・`collect.yml`。`tests/ui_smoke.py`は別途ブラウザ確認 | `test_watch.py`の取得失敗・採否、`test_sources.py`の分類/既存情報維持、`display.test.cjs`のJST・鮮度・終了日。 | 変更不要。live feed検査は外部依存だが、実失敗を低価値と断定しない。 |
| [lgpwmng `552e5cbb25`](https://github.com/YanTKYS/lgpwmng/tree/552e5cbb25743e55748c9d8626b309f0d2fad570) | `test/`のNode／webstore ZIP・internal CRX双方のWorkflowで`npm test` | `vault-store.test.js`の暗号化/復元、`consent.test.js`、`internal-crx.test.js`の署名/ID/秘密鍵混入、`package.test.js`の実ZIP内容。 | C1の文書検査のみ候補。安全・成果物の静的検査は保留または維持。 |
| [nonpaper `e2272cf19c`](https://github.com/YanTKYS/nonpaper/tree/e2272cf19c836d9ca1b85cb1e74d58a0b827adf8) | `tests/NonPaper.Tests/`のxUnit／`pull-request.yml`の`dotnet test` | `EventRepositoryTests`でJSON保存/再読込、同時更新、パス逸脱拒否、管理トークン、拒否時のデータ不変を実行。 | 維持。文言assertを含むが、状態遷移拒否・利用者への失敗通知と結び付く。 |
| [sharescan `a6fa65c939`](https://github.com/YanTKYS/sharescan/tree/a6fa65c939eb38687ff118d152a4dc6788d13ac1) | `internal/**/*_test.go`／READMEの`go test ./...`、CIなし | `scanner_test.go`の一時ディレクトリ走査、`csvout_test.go`のCSV/BOM、除外・出力。 | 変更不要。ファイル作成/存在の検査は出力処理の結果を確認するもの。 |
| [txt4genai `808fe85e32`](https://github.com/YanTKYS/txt4genai/tree/808fe85e32a08d1dbaa7db1137d2b0747549ef12) | `src/Txt4GenAI.Tests/`のxUnit／`build.yml`と`build/run-tests.ps1` | `DocxListRenderingTests`は実際にDOCXを作りMarkdownへ変換、`ConversionServiceTests`の失敗/キャンセル、フロントマター出力。 | 変更不要。`MetadataWriterTests`は文書台帳ではなく製品の出力形式。 |
| [markdownutil `ba0cb55cde`](https://github.com/YanTKYS/markdownutil/tree/ba0cb55cdecb35d40088998488138da7b2fb56ff) | `test/*.test.js`のNode／`npm test`、CIなし | Word出力、Clipboard失敗、`postmessage-security.test.js`の送信元/オリジン、スライド同期。vendor版検査は同梱物の整合。 | 変更不要。小さい関数の検査を件数だけで削減しない。 |
| [desknets_noticer `b78ea598d8`](https://github.com/YanTKYS/desknets_noticer/tree/b78ea598d8f086b50d892235c62564f2f85869c1) | `tests/*.test.js`のNode＋jsdom／`npm test`、CIなし | 投稿判定、重複通知、設定互換、`service-worker.test.js`の例外後の再実行、通知許可。 | C5のみ統合候補。MV3で動かないimportを防ぐ保証は残す。 |
| [drawio-poc `154d609218`](https://github.com/YanTKYS/drawio-poc/tree/154d6092182268d1760bfcb0a10084aad979e88d) | Playwright／`pages.yml`でdist・IIS用ZIP展開・公開先を確認 | `tests/smoke.spec.js`の保存/再読込、日本語編集、PNG/SVG、サブパス404・外部通信・PWA停止、配布LICENSE/NOTICE。 | 変更不要。配信物とZIPの反復は異なる配布経路の確認。 |
| [design-lab `647b5bf2ac`](https://github.com/YanTKYS/design-lab/tree/647b5bf2ac0739deec3906c3d650ee264d604773) | Node unit・Playwright／`test.yml`、Pagesはこれを再利用 | `query.test.mjs`の検索、全デザインの同じデータ/操作、フォーム、比較時の状態維持。 | 変更不要。描画結果HTMLや画面間比較が製品の主責務であり、source文字列検索と区別。 |
| [idontlovepdf `24371b38dd`](https://github.com/YanTKYS/idontlovepdf/tree/24371b38dd4150e4cbb49f33fe1bf4a376e50a59) | `scripts/ci/`のvendor整合・静的構成・Playwright smoke／`ci.yml` | engine/fontのSHA-256、参照ファイル、engine読込後のPDF選択UI、外部通信なし。 | 維持。`tests/`という名前のフォルダがないだけで対象外にしない。 |
| [idontlovepdf-engine `7d70d13733`](https://github.com/YanTKYS/idontlovepdf-engine/tree/7d70d13733f742ec64a6f3fe214f193bd7f713a4) | Node、no-WebCrypto経路、browser tests／`ci.yml`・`release.yml` | PDF保存後再読込、暗号認証/権限、xref、glyph/subset、安全な置換拒否、`dist-bundle.test.js`の配布API。 | 維持。通常経路と暗号fallback経路を同じ保証と決めない。 |
| [slide `56a692837a`](https://github.com/YanTKYS/slide/tree/56a692837af7fcbbb25565f5fd8b1cc01112758b) | `verify-bundle.yml`で`npm ci && npm run build`後、コミット済みbundleとの差分検査 | `assets/marp-core.bundle.js`が依存更新に追随すること。独立unit suiteではなく自動成果物検証。 | 維持。版固定だけのテストではなく、閉域配布物への更新漏れ防止。 |
| [poc-lab `e3a3f3d13c`](https://github.com/YanTKYS/poc-lab/tree/e3a3f3d13c9820d2f88a9547036ee39fdc5c7c87) | PeleのPlaywright、BeatAPIのNode／各test WorkflowとPages | `tests/pele.spec.js`の描画/失敗分離、`beatapi/test/poc.test.mjs`の単一API呼出し・タイムアウト・秘密値非出力。 | 継続部分のみ維持。READMEで検証終了/採用見送りの`flovia/`は整理対象から除外。 |
| [okinawa-dx-report `2149f04cfc`](https://github.com/YanTKYS/okinawa-dx-report/tree/2149f04cfc44e8334bc462ae1b19118ca4711838) | `python3 tools/test_checks.py`（READMEに実行手順、CIなし） | 得点上限・欠損/確認済み0点・相関の独立再計算。固定ルーブリック値は研究条件の契約。 | 維持。庁内情報の公開混入を防ぐsource/docs検査は要判断とし、削除を勧めない。 |
| [itoman-dx-policy `092bc0d62a`](https://github.com/YanTKYS/itoman-dx-policy/tree/092bc0d62aeeeb3ddd4f3c83642762a8abf049f5) | `tools/pptx_validate.py`・`pptx_layout_check.py`／`validate-pptx.yml`・改定案build Workflow | PPTXのZIP/OOXML、無編集保存後の再読込、パーツ/スライド数保持、枠外・文字溢れ。 | 維持。`test`という名前を持たないが、自動検証として対象へ含める。 |
| [yantkys.github.io `afd4aa8476`](https://github.com/YanTKYS/yantkys.github.io/tree/afd4aa847635cfd546576a877eb9ddfa2b9344ee) | `scripts/check-data.mjs`／`pages.yml`でデータ生成後に実行 | 公開JSONの構造・URL・重複、代表作品参照。失敗時は公開を止める。 | 維持。単なる資料の存在検査ではなく、利用画面へ配信するデータの契約。 |

## 後続Issueにできる候補

P2は通常の保守作業として先に検討、P3は該当箇所を変更する機会に統合する程度。緊急障害は確認していない。以下は採用前の候補であり、今回削除・skipはしていない。

### C1 / P2: lgpwmng — 掲載資料の文言検査を製品の安全検査から外す

根拠: [test/package.test.js](https://github.com/YanTKYS/lgpwmng/blob/552e5cbb25743e55748c9d8626b309f0d2fad570/test/package.test.js)。

- **削除候補**: `test/package.test.js`の「必須の掲載画像が資料全体で必須として書かれている」。4資料の`440x280`行に「必須」があるか、Marqueeに「任意」があるかだけを検査している。説明の言い換え・資料統合だけで失敗し、画像ファイルの正しさや拡張の動作は保証しない。
- **最小範囲/効果**: この1テストだけを文書レビューへ戻す。資料ごとに同じ掲載要件をassertする追随を減らす。Privacy Policyそのものや画像要件の記載を削る提案ではない。
- **維持/リスク**: `生成した ZIP の直下に manifest.json があり、中身が一致する`、CRX署名/秘密鍵混入、暗号化・同意の振る舞いは維持。申告種別・Privacy Policyの検査はストア申告契約を含むため**要判断**とし、まとめて削除しない。

### C2 / P2: ai-watch — Actionsの固定版とソースファイル一覧の固定を縮退

根拠: [tests/test_collect.py](https://github.com/YanTKYS/ai-watch/blob/5f71618e9cf080298e634d8e29bba93bd8236477/tests/test_collect.py)。

- **削除候補**: `tests/test_collect.py::RepoLayout.test_actions_use_node24_versions`はcheckout/setup-*をすべて`v7`に固定。目的は旧runtime排除だが、これでは互換な将来版への更新も必ず修正を要する。アプリの表示版とは別種だが、保守上は固定値追随の問題が同じ。
- **統合・置換候補**: 同`test_no_weekly_monthly_and_manual_ai_probe_is_isolated`の`scripts/*.py`全ファイル名の完全一致、`tests/test_search.py::RepoLayout.test_pages_ui`の`js.count('fetchText("data/search-index.json")') == 1`。無関係なスクリプト追加や同等な読込処理への書換でも失敗する。
- **最小範囲/効果**: 固定Actions版と全ファイル名リストのassertを外し、既存のSecret・PRトリガー・手動API分離の保証は残す。検索初回読込は既存の`tests/app_harness.cjs`を使う検索/再試行テスト・`tests/e2e/pages.spec.cjs`の保証と照合し、同じ保証があれば呼出し文字列のカウントをそちらへ集約する。新しい基盤は不要。
- **維持/リスク**: `test_no_pull_request_target_and_test_workflow_has_no_secrets`、APIキーを渡す範囲、取得失敗・ログ保護は維持。課金・外部送信防止まで「source検査だから」と外さない。Actionsのruntime更新可否は更新PRのレビューで確認する。

### C3 / P2: devlog — 公開ノートのタイトル完全一致だけを外す

根拠: [tests/test_build_site.py](https://github.com/YanTKYS/devlog/blob/5ddf6a6a23d50e354fbe0f2934f87d7720dee17e/tests/test_build_site.py)。

- **削除候補**: `tests/test_build_site.py::NotesBuildTests.test_only_listed_notes_are_published`の`manifest[0/1]["title"]`を現行の日本語タイトルへ固定する2assert。本文の見出し変更だけで落ちる。
- **最小範囲/効果**: タイトルの固定値だけ外す。タイトル抽出は既存の`test_missing_or_invalid_note_fails_the_build`が一時ノート`# A`→`A`で確認しており、実ノート本文の版/文言追随を減らせる。
- **維持/リスク**: 同じメソッドの公開ID/パスallowlist、`test_site_contains_only_published_markdown`、非公開repo/調査原文が出ない検査は残す。文書テストという名前でも、公開漏えいの保証を失う削除はしない。

### C4 / P3: sheltermatch — Colab入口の契約と配置固定を分ける

根拠: [test/test_colab_badges.py](https://github.com/YanTKYS/sheltermatch/blob/42e7376677acd763578a132885064f221ee729cb/test/test_colab_badges.py)。

- **統合候補**: `test/test_colab_badges.py`の`test_すべてのNotebookのタイトル直下にColabバッジがある`と`test_リンク先はmainブランチのNotebook自身`。前者がすでにNotebook自身のmain URLを含むバッジ全文と比較し、後者も同じURLを再確認する。
- **最小範囲/効果**: 同じmain URLの保証を1か所へ集約。最初のMarkdownセル・空行・3行目という配置固定を緩めるかは別途レビュー判断にする。
- **維持/リスク**: [#56](https://github.com/YanTKYS/sheltermatch/issues/56)で「入口を付け忘れない」テストが明示的に要求されている。バッジ・自分自身へのリンクの保証は残し、ファイル全体を削除しない。住所変換・ハザード判定には触れない。軽量テストなので性能上の効果は期待値に入れない。

### C5 / P3: desknets_noticer — 同じservice-worker検査を1回にする

根拠: [tests/service-worker-static-import.test.js](https://github.com/YanTKYS/desknets_noticer/blob/b78ea598d8f086b50d892235c62564f2f85869c1/tests/service-worker-static-import.test.js)。

- **統合候補**: `tests/service-worker-static-import.test.js`の`service-worker.jsにdynamic import()が存在しない`。直後の`background配下のすべてのファイルにdynamic import()が存在しない`が同じ述語で`service-worker.js`を再走査している。
- **最小範囲/効果**: 個別の先行テストを外し、後者のファイル名付きassertへ集約。現行は3ファイルの明示リストであり、「配下のすべて」というテスト名でも自動再帰走査ではないことに注意。
- **維持/リスク**: MV3 service workerのdynamic import非対応を防ぐ契約は維持。コメント/型参照の除外も残す。実行時間よりも同じ失敗の二重報告を減らす効果。

## 保留・変更不要の扱い

- schema版、APK/versionCode、CRX拡張ID、vendor SHA、研究の固定採点基準は互換性/署名/再現性の契約。表示版の固定値監視と同じ理由で削除しない。
- `lgpwmng/test/package.test.js`の同意チェックのsource順序・呼出し検査は、`consent.test.js`の関数単体テストだけでは呼出し元の未同意操作を保証できない。実際のpopup/background操作を確認する代替がない段階では削除保留。
- `devlog`のfavicon描画様式や`memoez`のラベル完全一致には低価値な要素もあるが、今回の5候補より効果が小さいため別Issueは勧めない。
- 実装時には上記の最小範囲について既存suiteを実行する。件数目標、全件台帳、恒久監視、整理専用CIは追加しない。

## このPRでの確認

この記録と`notes/README.md`の入口だけを追加する。個別リポジトリのproduction code・テスト・CI、Pagesの公開許可リストは変更しない。確認版を固定した30リンクのSHA/ファイル、25対象行の重複なし、相対リンク、候補テスト名、差分の空白を確認済み。アプリ全体のsuite成功や速度改善をこの調査の検証結果としては報告しない。

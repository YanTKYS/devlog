# AIコーディングツール比較（2026年10月）

個人開発者が、用途・開発環境・予算に応じてAIコーディングツールを選ぶための比較資料。

料金・利用制限・提供状況は頻繁に変わる。この資料は判断の出発点として使い、契約前に各製品の「公式」リンクとログイン後の利用状況画面で必ず再確認する。

- 調査基準日（確認日）: 2026-10-16
- 目的: 主要10製品の違いを共通の比較軸で把握し、自分の条件に合う候補を短時間で絞り込む
- 位置付け: 3者のDeep Research結果（[H. 参考資料](#h-参考資料)）を統合し、変動しやすい項目を公式情報で照合したもの

## 目次

- [A. 概要](#a-概要)
- [B. 総合比較表](#b-総合比較表)
- [C. 料金・利用制限の比較](#c-料金利用制限の比較)
- [D. 開発機能の比較](#d-開発機能の比較)
- [E. 製品別詳細](#e-製品別詳細)
- [F. 用途別の選び方](#f-用途別の選び方)
- [G. 比較上の注意点](#g-比較上の注意点)
- [H. 参考資料](#h-参考資料)

## A. 概要

### 調査対象

主要10製品: Claude Code / OpenAI Codex / GitHub Copilot / Cursor / Windsurf（現 Devin Desktop）/ Gemini CLI / Cline / Roo Code / OpenCode / Google Antigravity

2026年10月時点で、このうち3製品は前提が大きく変わっている。

| 製品 | 2026-10時点の状況 |
| --- | --- |
| Windsurf | 2026-06にCognitionが「Devin Desktop」へ改称。既存プランと価格は据え置き |
| Gemini CLI | 2026-06-18に、無料枠・Google AI Pro/Ultra など個人向けの提供を Antigravity CLI へ移行。組織ライセンスと有料APIキー経由のみ継続 |
| Roo Code | 2026-05-15に拡張機能・Cloud・Routerを含む全製品が提供終了。リポジトリはアーカイブ済み |

そのため、新規に選べる現役の選択肢は実質8系統（Claude Code / Codex / Copilot / Cursor / Devin Desktop / Antigravity / Cline / OpenCode）と、組織・API契約者向けの Gemini CLI になる。

### 比較の前提

- 個人開発者の新規契約を基準にする。旧プラン・年契約の経過措置は注記にとどめる
- 価格はUSD・税抜・月払い。年払い割引がある場合は併記する
- 「ツールの利用料金」と「モデルの推論料金」を分けて書く。BYOK（自分のAPIキー）型は、ツールが無料でも推論料金がかかる
- 独自のベンチマークは実施していない。コード品質・速度の優劣は判断しない
- 組織導入の観点は、個人が業務利用を検討する場合の参考として最小限に含める

### 情報源と確認方法

調査環境のネットワーク制限により、多くの公式サイトのページ本体を直接取得できなかった。そのため、次の方法で確認している。

- **直接確認**: Anthropic公式（claude.com、support.claude.com、code.claude.com）のページ本文と、GitHub上の公式リポジトリ（README・LICENSE）
- **公式ドメイン限定の検索で確認**: OpenAI、GitHub、Cursor、Cognition（Devin）、Google（Antigravity・Gemini CLI）、Cline、Roo Code、OpenCode。検索結果として得られた公式ページの記載内容を根拠にした
- **Deep Researchのみ**: 上記で確認できなかった事項は、Deep Research側の出典付き記述を使い「※DR」と付記した。第三者記事が根拠のものは「（第三者）」とした
- 確認できなかった事項は「未確認」、提供元が数値を公表していない事項は「非公開」とした

判断の優先順位は、(1) 2026年10月時点の公式情報、(2) 公式の変更履歴・リリースノート、(3) 出典と確認日が明確なDeep Researchの記述、(4) 信頼できる第三者の検証情報、の順とした。3者の記述が一致していても、変動しやすい項目は公式情報で照合した。

### 3者の調査結果の照合

調査原文は ChatGPT・Claude・Perplexity の3件（いずれも2026-10-16付）。

**共通して確認できた情報**（公式でも確認済み）

- Claude Code は Claude の有料プラン（Pro以上）またはAPIで利用し、Freeプランには含まれない。上限は5時間ごとのセッション上限と週間上限
- GitHub Copilot は2026-06-01から AI Credits（1クレジット＝$0.01）による使用量課金。Pro $10 / Pro+ $39 / Max $100
- Codex は ChatGPT プランに含まれ、APIキー利用はサブスクとは別のAPI従量課金
- Cline・OpenCode はツール本体が無料のOSSで、クラウドモデルを使えば推論料金が別にかかる
- 個人プランは学習利用があり得る（設定で変更）、組織プランは既定で学習なし、という傾向

**3者で異なっていた重要情報と判断**

| 項目 | ChatGPT | Claude | Perplexity | 採用した内容と根拠 |
| --- | --- | --- | --- | --- |
| Cursorの料金体系 | Free / Plus $8 / Premium $30 / Super $100 / Ultra $200、週間プール | Hobby / Pro $20 / Pro+ $60 / Ultra $200、月間（第三者記事） | ChatGPTと同じ新体系 | 新体系を採用。Cursor公式の料金・モデル料金ページとフォーラム告知で確認。Claudeの値は旧体系（既存契約者向けに残る） |
| Roo Code | 2026-05-15にアーカイブ | 2026-05-15に提供終了 | 現役製品として推奨 | 提供終了を採用。公式の終了告知とアーカイブ済みリポジトリで確認。Perplexityは情報が古い |
| Gemini CLI の無料利用 | 個人向けは2026-06-18に終了 | 同左 | 継続無料枠あり（1日1,000回） | 個人向け終了を採用。公式READMEの冒頭告知とGoogle Developers Blogで確認。Perplexityの数値は旧README由来 |
| Google Antigravity | 主要製品として扱う | 提供中（料金は第三者記事） | 製品範囲・料金とも未確認 | 提供中を採用。公式の料金・プラン・モデル・ダウンロードページで確認 |
| Windsurf / Devin Desktop の料金 | 製品移行のみ記載 | Free / Pro $20 / Max $200 / Teams（第三者） | 要再確認（ACU等の可能性） | Claudeの値を公式で確認できたため採用（Devin公式ドキュメント） |
| Codex のモデル | ChatGPTログインのGPT-5.5は2026-10-14退役、GPT-6系 | GPT-5.x-Codex系、GPT-6系は第三者報告 | 記載なし | 退役を採用。公式の変更履歴で確認（APIキー利用は対象外） |
| Codex の Free / Go | 記載あり | Freeで軽量タスク | Free・GoはCloud対象外 | Perplexityを採用。公式ヘルプで「Codex Cloud は Free・Go に含まれない」を確認 |
| Claude Code の料金の根拠 | 公式 | 第三者記事として記載 | 第三者記事 | 公式料金ページで確認（数値は3者一致） |
| Claude Code のWindows | Hooks・sandbox等を整理 | Git for Windows は任意 | Git for Windows 推奨、sandbox はネイティブWindows非対応 | 両方とも公式記載どおり（推奨だが必須ではない）。sandbox はネイティブWindows非対応を公式で確認 |
| Copilot の学習利用 | 記載少 | Free/Pro/Pro+ は2026-04-24以降オプトアウト制 | 個人は条件次第 | Claudeを採用。GitHub公式ブログで確認。現行ドキュメントは Max も対象に含める |

**情報の新旧で差が出た可能性が高い項目**

- Cursorの旧料金（Pro $20 等）、Windsurfのクレジット制、Gemini CLIの無料1,000回/日、Roo Codeの「無料で使える」、Copilotの「プレミアムリクエスト300回」は、いずれも2026年10月時点では旧情報
- Gemini CLI の公式料金ページには、個人向けの旧上限表（Code Assist 個人 1,000回/日 など）が残っている。同じリポジトリの README 冒頭の移行告知と矛盾するため、個人向けは利用不可として扱った
- Codex のモデル名は、公式ドキュメント内でも GPT-6.1 Sol / GPT-6 Luna / GPT-6 Astra など表記が揺れている

**公式資料での追加確認が必要な項目**（本資料では「未確認」「非公開」として扱った）

- Claude Code・Codex・Devin Desktop・Antigravity の上限の具体量（いずれも非公開または範囲表示）
- Copilot Free の AI Credits の量、Copilot の個人プランでの BYOK 可否
- Cursor 個人プランの Privacy Mode の既定値
- Devin Desktop の BYOK・ローカルモデル・Hooks
- Cline の Teams プランの価格
- Antigravity 個人プランのデータ利用条件（規約と概要ページで記述が分かれる）

## B. 総合比較表

### 提供形態と対応環境

| 製品 | 提供元 | 提供形態 | 対応OS | OSS |
| --- | --- | --- | --- | --- |
| Claude Code | Anthropic | CLI、IDE拡張（VS Code・JetBrains）、デスクトップ、Web（クラウド実行） | Windows 10 1809+（ネイティブ・WSL）、macOS、Linux | 非OSS |
| Codex | OpenAI | CLI、IDE拡張、ChatGPTデスクトップアプリ、Web（Codex Cloud）、iOS | Windows（ネイティブ・WSL2）、macOS、Linux | CLIは Apache-2.0 |
| GitHub Copilot | GitHub（Microsoft） | IDE拡張（VS Code・Visual Studio・JetBrains 等）、CLI、GitHub.com、Copilotアプリ、クラウドエージェント | Windows、macOS、Linux | 非OSS |
| Cursor | Anysphere | 独自IDE（VS Code系）、CLI、Web、Cloud Agents | Windows、macOS、Linux | 非OSS |
| Devin Desktop（旧 Windsurf） | Cognition | 独自IDE＋エージェント管理画面、Devin Local / Cloud、CLI | Windows、macOS、Linux | 非OSS |
| Gemini CLI | Google | CLI | Windows、macOS、Linux | Apache-2.0 |
| Cline | Cline | VS Code拡張、CLI、SDK（JetBrains版は Enterprise） | VS Code等が動く環境 | Apache-2.0 |
| Roo Code | Roo Code Inc. | （旧）VS Code拡張 | — | Apache-2.0（アーカイブ） |
| OpenCode | Anomaly（anomalyco） | ターミナルUI、デスクトップ（ベータ）、ACP対応エディタ連携 | Windows（Scoop・Chocolatey。WSL推奨）、macOS、Linux | MIT |
| Google Antigravity | Google | エージェント管理デスクトップアプリ、Antigravity IDE、Antigravity CLI（`agy`）、IDE拡張、SDK | Windows 10+（x64・ARM64）、macOS 12+、Linux | 非OSS |

### 料金・モデル・GitHub連携

| 製品 | 無料利用 | 主な料金体系 | 対応モデル・BYOK | GitHub連携 | 主な特徴 |
| --- | --- | --- | --- | --- | --- |
| Claude Code | なし（FreeはClaude Code対象外） | Claudeサブスク（Pro $20〜）またはAPI従量 | Anthropicモデルのみ。APIキー、Bedrock・Google Cloud・Microsoft Foundry経由も可 | GitHub App・GitHub Actions・クラウド実行からブランチ/PR | Hooks・Skills・サブエージェント・Pluginsの拡張性 |
| Codex | ChatGPT Free に限定的に含まれる（Go $8 も同様。Cloudは対象外） | ChatGPTプラン（Plus $20〜）と使用量を共有、またはAPI従量 | OpenAIモデル。APIキー利用可 | Codex Cloud、PRコードレビュー（`@codex review`） | ローカルとクラウドタスクを同一製品で使い分け |
| GitHub Copilot | Free（補完月2,000回＋少量のAI Credits） | 定額＋月間AI Credits（Pro $10〜） | 複数社のモデル。BYOKは組織向けVS Code・CLI等で提供 | Issue→クラウドエージェント→PR、PRレビューがGitHub上で完結 | GitHubの権限・課金・ポリシーと一体 |
| Cursor | Free（限定的、第三者モデル不可） | 定額＋週間プール（Plus $8〜）。第三者モデルはAPI定価で別課金 | Cursor/Grok系モデルが定額内。Claude・GPT・Gemini は Premium 以上で別課金 | Cloud AgentsがPR作成、Bugbot（PRレビュー） | IDE内のエージェント・ブラウザ確認・並列実行 |
| Devin Desktop | Free（軽いクォータ） | 定額＋日次/週次クォータ、超過はAPI価格（Pro $20〜） | 複数社モデル（管理者がモデルを制御可）。BYOKは未確認 | Devin Cloud による委任・PR | ローカルとクラウドのエージェントを一画面で管理 |
| Gemini CLI | 個人向けは終了 | 組織ライセンス（Code Assist Standard/Enterprise）または有料APIキー従量 | Geminiモデル。有料Gemini API・Vertex AI等 | GitHub Actions 連携 | OSSのCLI。個人は Antigravity CLI へ移行 |
| Cline | ツール無料（推論は別） | BYOK、Cline経由の従量、ClinePass $9.99（オープンモデル） | 多数のプロバイダ、ローカルLLM（Ollama等） | 標準機能は限定的（MCP・CLI経由） | 承認制の実行、Plan/Act、モデル選択の自由度 |
| Roo Code | — | 提供終了 | — | — | 新規採用不可。後継はZooCode・Cline |
| OpenCode | ツール無料（推論は別） | BYOK、Zen（従量）、Go $10 / Go Plus $40（オープンモデル） | 多数のプロバイダ、ローカルLLM | GitHub連携機能あり（詳細は公式参照） | プロバイダ非依存のターミナル型 |
| Google Antigravity | Individual $0（週間上限） | Google AIサブスク連動（Pro・Ultra）、超過はAIクレジット | Gemini系に加えClaude系など（プランで異なる） | 未確認 | 内蔵ブラウザ・複数エージェント・成果物（Artifacts） |

## C. 料金・利用制限の比較

確認日はいずれも2026-10-16。価格は月払いの税抜USD。

### 個人向けプラン

| 製品 | 無料 | 主要な有料プラン（月額） | 公式 |
| --- | --- | --- | --- |
| Claude Code | なし | Pro $20（年払いで月$17）、Max 5x $100〜、Max 20x（$200 と3者が記載。公式ページ本文では「From $100」のみ確認） | [Pricing](https://claude.com/pricing) |
| Codex | ChatGPT Free・Go（$8）に限定的に含まれる。Codex Cloud は対象外 | Plus $20、Pro $100 / $200 / $500 | [Codex Pricing](https://developers.openai.com/codex/pricing) |
| GitHub Copilot | Free: 補完 月2,000回＋限定的なAI Credits（量は未確認）、モデルは自動選択のみ | Pro $10（1,500 credits）、Pro+ $39（7,000）、Max $100（20,000） | [Plans](https://docs.github.com/en/copilot/get-started/plans) |
| Cursor | Free: 限定的、第三者モデル不可 | Plus $8、Premium $30、Super $100、Ultra $200 | [Pricing](https://cursor.com/pricing) |
| Devin Desktop | Free: 軽いクォータ | Pro $20、Max $200 | [Pricing](https://devin.ai/pricing) |
| Gemini CLI | 個人向けは2026-06-18に終了 | 個人向け定額は終了（Antigravityへ移行）。有料Gemini APIキーの従量は継続 | [移行告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) |
| Cline | ツール無料。アカウント保有者向けの無料モデル枠あり | ClinePass $9.99（オープンモデルのみ） | [Pricing](https://cline.bot/pricing) |
| Roo Code | — | 提供終了（未使用残高は返金） | [Sunset](https://docs.roocode.com/sunset) |
| OpenCode | ツール無料 | Go $10、Go Plus $40。Zen は従量 | [Go](https://opencode.ai/docs/go/) / [Zen](https://opencode.ai/zen) |
| Google Antigravity | Individual $0 | Google AI Pro（約$20）、Google AI Ultra $100（Proの5倍）/ $200（20倍） | [Pricing](https://antigravity.google/pricing) |

### 制限の単位・リセット・上限到達時

| 製品 | 制限の単位 | リセット | 上限到達時 | 追加料金の仕組み |
| --- | --- | --- | --- | --- |
| Claude Code | 5時間ごとのセッション上限＋週間上限。量は非公開。claude.ai・デスクトップと同じ枠を共有 | 5時間（ローリング）と週次 | リセット待ち、上位プランへ変更、または利用クレジットで継続 | 利用クレジット（月の上限額を設定可）。APIキー利用は通常のAPI従量 |
| Codex | 5時間ごとの枠（目安は範囲表示）。週間上限がかかる場合あり。ローカルとクラウドで同じ枠を共有し、クラウドタスクは消費が大きい | 5時間と週次 | Plus・Pro はクレジット購入で継続。Free・Go はアップグレード案内 | ChatGPTクレジット。APIキー利用はAPI従量 |
| GitHub Copilot | 月間AI Credits（モデルごとのトークン単価で換算）。有料プランの補完・Next Edit Suggestions は対象外で無制限 | 毎月1日 00:00 UTC。繰越なし | 追加予算（USD）を設定していなければ停止 | 1 credit＝$0.01 で追加利用。基本分→フレックス分の順に消費し、フレックス分は変動し得る |
| Cursor | Cursor/Grok系モデルの週間プール（Premium＝Plusの4倍、Super＝15倍、Ultra＝50倍）。xAIのGrok利用と共有 | 週次 | 追加購入またはリセット待ち | 第三者モデルは初回からプリペイド残高でAPI定価課金（個人は上乗せなし） |
| Devin Desktop | トークン基準のクォータ。Pro は日次＋週次、Max は週次のみ。量は非公開。無料モデルはクォータを消費しない | 日次・週次 | 有料プランは追加利用で継続 | 使用モデルのAPI定価 |
| Gemini CLI | 1日あたりのリクエスト数＋分単位の制限（組織: Standard 1,500回/日、Enterprise 2,000回/日） | 日次 | 翌日まで待つか、API従量へ | Gemini API / Vertex AI 等の従量 |
| Cline | 推論先プロバイダの制限に従う | プロバイダ依存 | プロバイダ側の挙動 | プロバイダへ直接、またはCline経由の従量 |
| OpenCode | Go: 月額の使用額上限。各モデルで5時間・週・月にそれぞれ月上限の20%・50%・100% | 5時間・週・月 | Zen残高への切り替え（第三者情報。公式未確認） | Zen 従量（上乗せなし、カード手数料のみ）またはBYOK |
| Google Antigravity | 週間上限（量は非公開）。Pro・Ultra は週間上限の範囲で5時間ごとに回復 | 5時間と週次 | 待機、またはAIクレジットで継続 | Google One のAIクレジット（モデルごとのAPI価格で消費）。**日本ではAIクレジットを購入できない** |

### 組織向けプラン

| 製品 | 組織向けプラン |
| --- | --- |
| Claude Code | Team: Standard席 $20（年払い）/ $25（月払い）、Premium席 $100 / $125。Enterprise: 席 $20（年払い・20席以上）＋API単価での使用量 |
| Codex | Business $20/人（公式表記に注記あり、条件の詳細と月払い額は未確認）、Enterprise・Edu は個別契約 |
| GitHub Copilot | Business $19/人（1,900 credits）、Enterprise $39/人（3,900 credits）。クレジットは組織単位でプール。組織では超過利用が既定で有効 |
| Cursor | Premium $30 / Super $100 / Ultra $200（いずれも1席あたり）。Teamsは第三者モデルに Cursor Token Rate（100万トークンあたり$0.25）が加算 |
| Devin Desktop | Teams: 最低 $80/月。フル席 $40/人（Pro相当のクォータ）、フレックス席は無料（Desktop利用不可） |
| Gemini CLI | Gemini Code Assist Standard / Enterprise、Google Workspace AI Ultra |
| Cline | Enterprise（個別。JetBrains・SSO・SCIM・監査ログ等）。Teams の価格は未確認 |
| Google Antigravity | Gemini Enterprise（Standard・Plus）に含まれる。Google Cloud の規約が適用 |

### サブスクリプションとAPI従量課金

同じ製品でも、認証方式によって課金と上限が変わる。

| 製品 | サブスク認証 | APIキー等の認証 |
| --- | --- | --- |
| Claude Code | プランの5時間・週間上限内で利用。超過は利用クレジット | Claude API の従量。サブスク上限は関係しない |
| Codex | ChatGPTプランの枠を消費 | OpenAI API の従量。ChatGPTログイン向けのモデル退役の影響を受けない |
| Gemini CLI | 組織ライセンスのみ | 有料Gemini API・Vertex AI 等の従量 |
| Cline / OpenCode | 該当なし（OpenCode Go は独自の定額） | 各プロバイダの従量。Claude の Pro/Max をサードパーティツールのログインに使うことは Anthropic が認めていない |

### 利用可能なモデル（2026-10時点）

モデルの入れ替えは月単位で起きる。ここでは傾向だけを示し、正確なモデル名は各製品のモデル一覧で確認する。

- **Claude Code**: Fable / Opus / Sonnet / Haiku。Pro では Fable は利用クレジット経由、Max では週間上限の50%まで
- **Codex**: GPT-6系。ChatGPTログインでの GPT-5.5 は2026-10-14に退役し、後継は GPT-6.1 Sol とされている（モデル名の表記は公式資料間で揺れがある）
- **GitHub Copilot**: 複数社のモデル。モデルごとにクレジット消費が異なる（[Models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)）
- **Cursor**: 定額内は Cursor/Grok 系のみ。Claude・GPT・Gemini は Premium 以上で別課金
- **Google Antigravity**: Gemini系（最上位の Gemini 4 Argon は Ultra・Enterprise）と Claude系など。プランと試用期間で使えるモデルが異なる

## D. 開発機能の比較

凡例: ◎ 標準機能 / ○ 設定・公式の拡張機能で対応 / △ 外部連携（MCP・自作スクリプト・他サービス）で実現 / － 非対応または公式の記載なし / ？ 未確認

Roo Code は提供終了のため除外した。

| 機能 | Claude Code | Codex | Copilot | Cursor | Devin Desktop | Gemini CLI | Cline | OpenCode | Antigravity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 複数ファイルの編集 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| コマンド・テスト実行 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| コードレビュー | ◎ | ◎ | ◎ | ◎ | ◎ | ○ | △ | △ | ？ |
| GitHub連携・PR作成 | ◎ | ◎ | ◎ | ◎ | ◎ | ○ | △ | ○ | ？ |
| クラウド実行 | ◎ | ◎ | ◎ | ◎ | ◎ | － | － | － | ？ |
| 並列エージェント・サブエージェント | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ◎ |
| MCP | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| Hooks | ◎ | ◎ | ◎ | ◎ | ？ | ◎ | ◎ | ？ | ◎ |
| Skills・カスタムルール | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ◎ | ◎ | ◎ |
| ローカルモデル | － | ？ | ○ | － | ？ | － | ◎ | ◎ | － |
| Windows対応 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ○ | ◎ |

表を読むときの補足（対応の条件と区別）:

- **コードレビュー**: Claude Code はローカルの `/code-review` が標準、GitHub上のPR自動レビュー（Code Review）は Team・Enterprise 向けで利用クレジット課金。Cursor の Bugbot は Premium 以上で使用量課金。Copilot のPRレビューも AI Credits を消費する
- **GitHub連携・PR作成**: Copilot はIssue割り当てからPR作成まで GitHub 上で完結する。Claude Code・Codex・Cursor は GitHub App 等の接続が前提。Gemini CLI は GitHub Actions 経由。Cline は gh CLI や MCP で実現する
- **クラウド実行**: Claude Code は Pro 以上（クラウドVMの追加料金なし、プランの上限を消費）。Codex Cloud は Plus 以上。Cursor の Cloud Agents は Premium 以上（Plus は不可）。Copilot のクラウドエージェント、Devin Cloud は各プランの課金に従う
- **Skills・カスタムルール**: ルールファイルは Claude Code が `CLAUDE.md`、Codex が `AGENTS.md`、Copilot が `.github/copilot-instructions.md` と `AGENTS.md`、Cursor が `.cursor/rules` と `AGENTS.md`、Gemini CLI が `GEMINI.md`、Cline が `.clinerules/` と `AGENTS.md`、OpenCode が `AGENTS.md`、Antigravity が `GEMINI.md` と `AGENTS.md`
- **ローカルモデル**: Copilot は VS Code の BYOK（Business・Enterprise）と Copilot CLI で Ollama 等を指定できる。Claude Code はAnthropicモデル前提で、ローカルモデルは公式にサポートされていない。Codex の OSS モデル対応は今回確認できなかった
- **Windows対応**: Claude Code はネイティブ対応だが、組み込みのsandboxはネイティブWindows非対応（WSL2なら利用可）。Codex はネイティブのWindows sandboxがあるが、WSL2に比べネットワーク分離が弱い。OpenCode は Scoop・Chocolatey で導入できるが、公式は WSL を推奨
- **Devin Desktop・Antigravity**: 機能欄は公式ドキュメントとDeep Researchの記述によるもので、料金ほど細かくは再確認していない

## E. 製品別詳細

比較表に書いた内容は繰り返さず、判断に必要な補足だけを書く。

### Claude Code

- 特徴: ターミナル中心のエージェント。同じエンジンをCLI・IDE・デスクトップ・Webで使え、`CLAUDE.md` や設定、MCP構成を共有できる
- 主な機能: コード探索、複数ファイル編集、コマンド実行、チェックポイントと巻き戻し、クラウド実行（端末を閉じても継続）、スケジュール実行（routines）、GitHub Actions（`@claude`）、Chrome連携によるブラウザ確認
- 料金・利用制限: Pro 以上に含まれる。Max には Claude Platform 用の月間APIクレジット（5x: $100、20x: $200）が付く。上限の量は非公開で、モデル・effort・会話の長さで消費が変わる。週間上限の25%引き上げ（2026-09-14〜）が報じられているが、公式ページでは未確認（※DR）
- 拡張性: Hooks、Skills、サブエージェント、Plugins、MCP、権限モード、sandbox。企業向けには Bedrock・Google Cloud・Microsoft Foundry 経由やゲートウェイ経由の構成がある
- 適した用途: 既存リポジトリの保守、ターミナルからの大きめの改修、Hooks等で独自ワークフローを組みたい場合
- 注意点: 無料枠がない。チャットと上限を共有する。ネイティブWindowsでは sandbox が使えない。個人プランはモデル改善への利用が選択制で、許可すると最長5年保持される
- 公式: [Pricing](https://claude.com/pricing) / [Usage limits](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) / [Setup](https://code.claude.com/docs/en/setup) / [Costs](https://code.claude.com/docs/en/costs) / [Data usage](https://code.claude.com/docs/en/data-usage)

### OpenAI Codex

- 特徴: ローカル（CLI・IDE・デスクトップ）とクラウド（Codex Cloud）を同じ製品で使い分けられる。CLIはOSS
- 主な機能: 複数ファイル編集、コマンド実行、Codex Cloud への非同期委任、GitHubのPRレビュー（`@codex review`、ルールは `AGENTS.md`）、ネイティブのWindows sandbox
- 料金・利用制限: ChatGPTプランの枠を消費し、上限は「目安の範囲」として示される。Business には固定月額なしの Codex 専用席もあったが、2026-06-24に新規販売を終了
- 拡張性: MCP、Skills（`.agents/skills`）、サブエージェント、Hooks（実行前に信頼確認が必要）、Plugins。MCP設定は `config.toml` で CLI・IDE・デスクトップに共通
- 適した用途: ChatGPT を既に契約している、ローカル作業とクラウド委任を併用したい場合
- 注意点: Free・Go では Codex Cloud を使えない。ChatGPTログイン向けのモデルは退役が頻繁で、スクリプトでモデル名を固定すると動かなくなる
- 公式: [Pricing](https://developers.openai.com/codex/pricing) / [ChatGPTプランでの利用](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) / [Changelog](https://learn.chatgpt.com/docs/changelog) / [Windows](https://developers.openai.com/codex/windows) / [GitHub](https://github.com/openai/codex)

### GitHub Copilot

- 特徴: IDE補完からクラウドエージェントまで、GitHubの権限・課金・ポリシーの中で提供される
- 主な機能: 補完、Next Edit Suggestions、IDEのエージェントモード、Copilot CLI、クラウドエージェント（Issue→ブランチ→PR）、PRコードレビュー、Copilotアプリでの並列作業
- 料金・利用制限: 補完は有料プランならクレジット対象外。エージェント・チャット・レビューはクレジットを消費する。年契約の旧 Pro/Pro+ は満了までリクエスト制が残る（※DR）。個人プランの新規受付は2026-04に一時停止し、2026-06-17から段階的に再開
- 拡張性: MCP、Hooks、Agent Skills、カスタムエージェント、Plugins、BYOK（組織向けVS Code、Copilot CLI、JetBrains等）
- 適した用途: GitHub の Issue・PR を中心にした開発、低価格（$10）からの導入
- 注意点: 「$10でエージェント使い放題」ではない。組織では超過利用が既定で有効なので、上限を設けたい場合は管理者がポリシーを無効にする。組織の席は2026-10-01から前払い課金に変わると告知されていた（適用状況は未確認）
- 公式: [Plans](https://docs.github.com/en/copilot/get-started/plans) / [個人の課金](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals) / [組織の課金](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises) / [Changelog](https://github.blog/changelog/)

### Cursor

- 特徴: VS Code系の独自IDE。IDE内のエージェント、Cloud Agents、ブラウザ確認、並列実行を統合している
- 主な機能: 補完（Tab）、エージェントによる複数ファイル編集、Cloud Agents（分離VMでテスト・PR作成・UI確認）、Bugbot、自分のマシンでツールを実行する Self-Hosted Machines
- 料金・利用制限: 2026年10月に新体系（The X Subscription）へ移行（第三者記事は2026-10-12と報じている）。定額内は Cursor/Grok 系モデルの週間プールで、Grok の利用と共有する。旧プラン（Pro・Pro+ 等）は既存契約者向けに残り、Pro+ には1対1の移行先がない
- 拡張性: Rules、Skills、Hooks（Cloud Agents でも `.cursor/hooks.json` が動く）、MCP、Plugins、サブエージェント
- 適した用途: IDE内で編集から画面確認まで完結したい、Webアプリの画面をエージェントに操作させたい場合
- 注意点: Plus（$8）は Cursor 独自モデルのみで、Cloud Agents・Bugbot・第三者モデル・自分のAPIキーは使えない。Premium 以上でも Claude・GPT は月額に含まれない。Self-Hosted Machines でもエージェントのループはクラウド側で動く
- 公式: [Pricing](https://cursor.com/pricing) / [Models & Pricing](https://cursor.com/docs/models-and-pricing) / [Team Pricing](https://cursor.com/docs/account/teams/pricing) / [X Subscription告知](https://forum.cursor.com/t/introducing-the-x-subscription/174450) / [Data use](https://cursor.com/data-use)

### Windsurf（現 Devin Desktop）

- 特徴: 旧 Windsurf を Cognition が Devin Desktop に改称した製品。IDEと、ローカル（Devin Local）・クラウド（Devin Cloud）のエージェントを一つの管理画面で扱う
- 主な機能: IDE、Tab補完、エージェント管理画面、クラウドへの委任、Windows のグループポリシー（ADMX）による集中管理（※DR）
- 料金・利用制限: クォータの量は非公開。2026-10-16まで SWE-2 の無料利用キャンペーンが告知されていた
- 拡張性: MCP、管理者によるモデル選択の制御。Hooks・BYOK は未確認
- 適した用途: ローカル作業とクラウド委任を一つの画面で管理したい、Windowsの集中管理が必要な組織
- 注意点: Windsurf 時代の料金（クレジット制）や旧エージェント（Cascade）の記事は現行仕様と一致しない。既定では学習利用され得る（有料プランはオプトアウト可、Teams は管理者のみ）
- 公式: [Pricing](https://devin.ai/pricing) / [Devin Desktop FAQ](https://docs.devin.ai/desktop/devin-desktop-faq) / [Self-serve plans](https://docs.devin.ai/admin/billing/self-serve) / [Security](https://docs.devin.ai/admin/security)

### Gemini CLI

- 特徴: GoogleのOSSのCLIエージェント。個人向けの役割は Antigravity CLI に引き継がれ、Gemini CLI は組織ライセンスと有料APIキーの利用者向けとして残っている
- 主な機能: コード探索、ファイル編集、シェル実行、Plan mode、チェックポイント、ヘッドレス実行、GitHub Actions 連携
- 料金・利用制限: 公式READMEは最新の Gemini モデル（Gemini 4 Argon）に最適化されていないと明記し、Antigravity の利用を案内している
- 拡張性: `GEMINI.md`、カスタムコマンド、Agent Skills、Hooks、拡張機能、MCP、サブエージェント
- 適した用途: Gemini Code Assist の組織ライセンスがある、Gemini API・Vertex AI を既に従量で使っている、OSSのCLIを改変・組み込みたい場合
- 注意点: 「Googleアカウントで無料1,000回/日」は終了した。無料（未払い）APIキーで継続できるかは未確認。個人は Antigravity CLI を検討する（設定・Skills・MCPは移行時に引き継がれる）
- 公式: [移行告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) / [GitHub](https://github.com/google-gemini/gemini-cli) / [Quotas and pricing](https://geminicli.com/docs/resources/quota-and-pricing/)

### Cline

- 特徴: OSSのエージェント。VS Code拡張・CLI・SDKが同じ実行基盤を使う。各操作を承認しながら進められる
- 主な機能: Plan/Act、複数ファイル編集、コマンド実行、ブラウザ操作、チェックポイント、CLIでの worktree 実行と並列エージェント
- 料金・利用制限: 推論料金はプロバイダへ直接払うか、Cline経由の従量。ClinePass は通常のAPI単価に比べ2〜5倍の利用量をうたうオープンモデル向け定額で、Claude・GPTは対象外（※DR）
- 拡張性: MCP、Hooks（承認ゲートとして使える）、`.clinerules/`、Plugins、サブエージェント（CLI・デスクトップ。MCPツールは使えない）
- 適した用途: 特定ベンダーの定額に縛られたくない、API料金を自分で管理したい、ローカルLLMを試したい場合
- 注意点: 自律的な探索や再試行でトークン消費が増えやすく、高性能モデルでは定額型より高くなることがある。API側で予算上限を設定する
- 公式: [Pricing](https://cline.bot/pricing) / [Docs](https://docs.cline.bot/) / [ClinePass](https://docs.cline.bot/getting-started/clinepass) / [GitHub](https://github.com/cline/cline)

### Roo Code（提供終了）

- 状況: 2026-05-15に VS Code拡張・Roo Code Cloud・Roo Code Router を含む全製品が終了した。未使用残高は返金され、リポジトリは読み取り専用でアーカイブされている
- 移行先: 公式は、コミュニティによるフォークの ZooCode と、派生元の Cline を案内している
- 注意点: Marketplace に掲載が残っていても保守されないため、新規採用しない。2026年以前の比較記事の「Roo Code は無料で使える」は現在当てはまらない
- 公式: [Sunset](https://docs.roocode.com/sunset) / [GitHub（アーカイブ）](https://github.com/RooCodeInc/Roo-Code)

### OpenCode

- 特徴: プロバイダ非依存のOSSのターミナル型エージェント。現行の公式リポジトリは `anomalyco/opencode`（旧 `sst/opencode`）
- 主な機能: ターミナルUI、デスクトップアプリ（ベータ）、ACP対応エディタからの利用、エージェントとサブエージェント、ルールベースの権限（allow / deny / ask）
- 料金・利用制限: Zen は動作検証済みのモデルを上乗せなしの従量で提供し、すべて米国でホストされる。Go はオープンモデル向けの定額
- 拡張性: MCP（ローカル・リモート、OAuth）、`AGENTS.md`、カスタムエージェント、Plugins。Hooks は未確認
- 適した用途: IDEに依存したくない、SSHやコンテナ内で使いたい、モデルを頻繁に切り替えたい場合
- 注意点: Claude の Pro/Max サブスクリプションでのログインは使えない（Anthropic はサードパーティツールでのサブスク認証を認めていない）。ChatGPT・Copilot のサブスク連携は今回公式で未確認。同名・類似名のプロジェクトがあるため、導入時はリポジトリの所有者を確認する
- 公式: [Docs](https://opencode.ai/docs/) / [Go](https://opencode.ai/docs/go/) / [Zen](https://opencode.ai/zen) / [GitHub](https://github.com/anomalyco/opencode)

### Google Antigravity

- 特徴: Google のエージェント開発環境。2026-05に Antigravity 2.0（エージェント管理デスクトップ）、Antigravity CLI（`agy`）、SDK が加わり、旧エディタは「Antigravity IDE」になった
- 主な機能: 複数エージェントの並列実行、内蔵ブラウザでの画面確認、タスク計画・スクリーンショット・ブラウザ録画などの成果物（Artifacts）、IDE拡張（VS Code、JetBrains 等）
- 料金・利用制限: 無料の Individual でも Tab 補完と Command は無制限で、エージェントに週間上限がある。上限の量は非公開
- 拡張性: Agent Skills、Hooks、サブエージェント、拡張機能（プラグイン）、MCP。アプリ・CLI・IDE拡張でモデル選択を共有する
- 適した用途: 画面確認を伴うWebアプリ開発、Gemini Code Assist 個人利用からの移行、Gemini Enterprise を契約している組織
- 注意点: 日本ではAIクレジットを購入できず、上限到達後に追加料金で続ける手段がない。個人向けプランでは、`agy` を他社のコーディングエージェントに組み込む使い方はサポート対象外。個人利用では操作データが製品改善に使われ、人による確認もあり得る（設定で変更可）
- 公式: [Pricing](https://antigravity.google/pricing) / [Plans](https://antigravity.google/docs/plans) / [Models](https://antigravity.google/docs/models/) / [Download](https://antigravity.google/download/) / [Terms](https://antigravity.google/terms/) / [AIクレジット](https://support.google.com/googleone/answer/16287445?hl=en)

### 補足: その他の製品

主要10製品と同じ深さでは調べていない。候補に加える場合は別途、料金・制限・データ条件を確認する。

| 製品 | 位置付け | 備考 |
| --- | --- | --- |
| Antigravity CLI（`agy`） | Gemini CLI の個人向け後継 | Antigravity の一部として提供 |
| Devin（Cloud・Review） | Cognition のクラウド型自律エージェント | Devin Desktop と同じ料金体系（※DR） |
| ZooCode | Roo Code のコミュニティフォーク | Roo Code 公式が移行先として案内 |
| Kilo Code | Roo Code 系のOSS拡張 | MITライセンスで更新が続いている（※DR） |
| Aider | Git連携を重視するCLI型のOSS | BYOK型（※DR） |

## F. 用途別の選び方

総合ランキングは作らない。条件ごとに「まず検討する候補」と「別の製品が合う条件」を示す（いずれも考察）。

### 無料または低予算での個人開発

- 候補: Copilot Free（補完中心）、Copilot Pro $10、Cursor Plus $8、Antigravity Individual $0、Codex（ChatGPT Free・Go）
- 推論料金も抑えたい場合: Cline・OpenCode とローカルLLM、または OpenCode Go $10・ClinePass $9.99 などのオープンモデル定額
- 別の製品が合う条件: 定額で上限を気にせず大きな改修を任せたいなら、Claude Code Pro・Codex Plus（いずれも $20）が月額で予算を固定しやすい。ローカルLLMはPCの性能（メモリ・GPU）とツール呼び出しの精度に左右される
- 注意: 無料枠ほど学習利用の条件が厳しい。業務のコードや個人情報は入れない

### アイデアから小規模アプリを素早く作成

- 候補: Cursor（IDEで編集から画面確認まで）、Antigravity（内蔵ブラウザ・成果物での確認）、Claude Code・Codex（ターミナルからまとめて実装）
- 別の製品が合う条件: すでにGitHubで管理していてPR単位で進めたいなら Copilot。モデルを選びたい・推論料金を自分で管理したいなら Cline・OpenCode

### 既存GitHubリポジトリの保守

- 候補: Claude Code、Codex、Copilot（CLI・エージェントモード）、Cursor
- 判断の観点: 差分確認、テスト失敗後の再試行、チェックポイント・Gitによる巻き戻し、ルールファイルで保守方針を固定できるか
- 別の製品が合う条件: 修正をIssue単位で非同期に任せたいなら、Copilot のクラウドエージェントか Codex Cloud。予算をAPI単位で管理したいなら Cline

### 複数ファイルにまたがる機能実装

- 候補: Claude Code（Max）、Codex（Pro）、Cursor（Premium 以上）、Devin Desktop
- 判断の観点: サブエージェントでの分担、計画（Plan mode）、長い会話の要約と再開、worktree などによる並列作業の分離
- 別の製品が合う条件: 低予算なら Copilot Pro+ のクレジットの範囲で進める。上位プランの上限に余裕がある製品ほど料金も上がる

### GitHub中心のPR駆動開発

- 候補: GitHub Copilot（Issue割り当て→クラウドエージェント→PR→レビューが GitHub 上で完結）
- 別の製品が合う条件: レビューの観点を自分で細かく定義したいなら Claude Code（GitHub Actions、`REVIEW.md`）や Codex のコードレビュー。IDE中心なら Cursor の Cloud Agents と Bugbot
- 注意: PRレビューもクレジット・使用量を消費する。Copilot のレビューは既定の深さを2026-09-28から「Balanced」に変えると告知されていた

### 大規模リポジトリ・長時間タスク

- 候補: Claude Code のクラウド実行、Codex Cloud、Cursor Cloud Agents、Devin Cloud
- 判断の観点: 実行時間そのものより、5時間・週間の上限、月間クレジット、週間プールが実際の制約になる。上限到達時に止まるのか、追加料金で続くのかを先に確認する
- 別の製品が合う条件: クラウドへコードやシークレットを送れない場合は、ローカル実行のCLI（Claude Code・Codex・OpenCode）を使う

### Windows中心の開発

- 候補: GitHub Copilot（Visual Studio・VS Code との統合）、Claude Code（ネイティブ。WSL不要）、Codex（ネイティブのWindows sandbox）
- 別の製品が合う条件: Linuxのツールチェーンや sandbox による隔離が必要なら、Claude Code・Codex を WSL2 で使う。OpenCode は WSL が推奨。組織でWindows端末を集中管理するなら Devin Desktop のグループポリシーも候補
- 注意: Excel VBA などはエディタに直接統合されないため、モジュールをファイルに書き出してGitで管理し、VS Code等で編集する運用になる（Deep Research（Claude）の考察）

### UI/UXを伴うWebアプリ開発

- 候補: Antigravity（内蔵ブラウザ・録画）、Cursor（Cloud Agents のブラウザ・デスクトップ操作）、Claude Code（Chrome連携）、Cline（ブラウザ操作）
- 別の製品が合う条件: ブラウザ機能のない製品でも、Playwright 等を MCP で接続すれば同様の確認ができる
- 注意: 画面を操作できることと、UI/UXの品質を評価できることは別。アクセシビリティ検査やビジュアル回帰テストを併用する。ブラウザ操作はログイン済みのセッションにも及ぶため、自動承認の範囲を狭くする

### 組織利用・セキュリティ重視

- 候補: Copilot Business/Enterprise、Claude Team/Enterprise、ChatGPT Business/Enterprise（Codex）、Cursor の Teams/Enterprise、Antigravity（Gemini Enterprise）
- 判断の観点: 学習に使わないことが既定か、データ保持期間、ゼロデータ保持（ZDR）、SSO・SCIM、監査ログ、MCP・Pluginsの許可リスト、ネットワーク制御、データ所在地
- 別の製品が合う条件: インターネット接続を前提にできない環境では、Cline・OpenCode とローカルLLMや組織内の推論APIの組み合わせが技術的な候補になる。ただし、モデル配布・ログ・認証・更新を自前で運用する必要がある
- 注意: 個人プランでの業務利用は避け、組織契約の条件（保持・所在地・監査）を契約書と設定で確認する

## G. 比較上の注意点

### 「無料」の意味が製品ごとに違う

- **継続的な無料枠**: Copilot Free、Antigravity Individual、Codex（ChatGPT Free の範囲）、Cursor Free、Devin Desktop Free
- **ツールだけ無料**: Cline・OpenCode。クラウドのモデルを使えば推論料金がかかる。無料になるのはローカルLLMと、提供元の無料モデル枠だけ
- **無料枠なし**: Claude Code（Freeプランでは使えない）
- **終了した無料枠**: Gemini CLI の個人向け無料利用、Roo Code

### サブスクとAPI従量は別の財布

- Claude Code・Codex は、サブスクでログインするとプランの上限内、APIキーを使うとAPI従量になる。APIの単価表から、サブスクで使える量を見積もることはできない
- Cursor の Premium 以上でも、Claude・GPT・Gemini は月額に含まれず、最初の1リクエストからAPI定価で課金される
- Claude の Pro/Max は、サードパーティ製ツール（OpenCode 等）のログインには使えない

### 上限は「回数」ではない

- ほとんどの製品で、1回の依頼が消費する量はモデル、推論の深さ（effort）、読み込むファイル数、会話の長さ、テストログ、サブエージェントの数で変わる
- 公式が上限の量を公表していない製品（Claude Code、Devin Desktop、Antigravity。Codex は範囲表示）では、利用者報告の「◯回/5時間」を公式値として扱わない
- リセット周期が製品ごとに違う（5時間・日次・週次・月次）。月間のCopilotと、週間のCursor・Antigravityは単純に比べられない

### モデル選択でコストが大きく変わる

- Copilot はモデルごとのトークン単価でクレジットを換算する。上位モデルを使うと同じ作業でも早く枠を使い切る
- 同じモデルを使っても、ツールによってコンテキストの集め方・編集方法・テストの回し方が違うため、結果が同じになるとは限らない

### データ利用条件は個人プランと組織プランで違う

| 製品 | 個人向けプラン | 組織向けプラン・API |
| --- | --- | --- |
| Claude Code | 学習利用は選択制。許可すると保持5年、許可しなければ30日 | Team・Enterprise・API は既定で学習なし。保持は標準30日、ZDRは適格な Enterprise 組織のみ |
| Codex | Free・Plus・Pro は「モデル改善」設定がオンだと学習に使われ得る（※DR） | Business・Enterprise・Edu・API は既定で学習なし（※DR） |
| GitHub Copilot | Free・Pro・Pro+・Max は2026-04-24以降、オプトアウトしない限り学習に使用 | Business・Enterprise は対象外 |
| Cursor | Privacy Mode オフだと学習に使われ得る。個人の既定値は未確認 | Teams・Enterprise は Privacy Mode が既定でオン（※DR） |
| Devin Desktop | 既定で学習に使われ得る。有料プランはオプトアウト可 | Teams は管理者のみオプトアウト可。Enterprise は書面同意なしに学習しない |
| Google Antigravity | 操作データを製品・機械学習の改善に使用し、人が確認することもある（設定で変更可） | Gemini Enterprise は Google Cloud の規約。学習に使わない |
| Cline・OpenCode | 推論先プロバイダの規約に従う。ローカルLLMなら推論データは外部に送られない | 同左 |

- 「ローカル実行」は推論までローカルとは限らない。ファイル操作だけがローカルで、エージェントのループや推論はクラウドという構成が多い
- `CLAUDE.md` や `AGENTS.md` などの指示はセキュリティの境界ではない。実際に何を許すかは、権限設定・sandbox・Hooks・OSの権限で制御する

### 情報の鮮度

- 2026年に、Copilot の課金方式、Cursor の料金体系、Windsurf の製品名、Gemini CLI の個人向け提供、Roo Code の提供が相次いで変わった。2025年以前の比較記事は前提が崩れている
- 再確認の目安: 料金・上限・モデル一覧は毎月、データ利用条件と提供状況は四半期ごと、または規約改定の通知時

## H. 参考資料

### Deep Research 原文（2026-10-16）

- [ChatGPT による調査](../data/deepresearch/ai-coding-tools-20261016-chatgpt.md)
- [Claude による調査](../data/deepresearch/ai-coding-tools-20261016-claude.md)
- [Perplexity による調査](../data/deepresearch/ai-coding-tools-20261016-perplexity.md)

### 公式料金ページ

| 製品 | 料金・プラン |
| --- | --- |
| Claude Code | [Claude Pricing](https://claude.com/pricing) |
| Codex | [Codex Pricing](https://developers.openai.com/codex/pricing) / [ChatGPT Plans](https://openai.com/chatgpt/pricing) |
| GitHub Copilot | [Plans for GitHub Copilot](https://docs.github.com/en/copilot/get-started/plans) / [Models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) |
| Cursor | [Pricing](https://cursor.com/pricing) / [Models & Pricing](https://cursor.com/docs/models-and-pricing) |
| Devin Desktop | [Plans and Pricing](https://devin.ai/pricing) |
| Gemini CLI | [Quotas and pricing](https://geminicli.com/docs/resources/quota-and-pricing/)（個人向けの表は旧情報） |
| Cline | [Pricing](https://cline.bot/pricing) |
| OpenCode | [Go](https://opencode.ai/docs/go/) / [Zen](https://opencode.ai/zen) |
| Google Antigravity | [Pricing](https://antigravity.google/pricing) / [Plans](https://antigravity.google/docs/plans) |

### 公式ドキュメント

- Claude Code: [Docs](https://code.claude.com/docs) / [Usage limits](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) / [Sandboxing](https://code.claude.com/docs/en/sandboxing) / [Cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web) / [Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- Codex: [ChatGPTプランでの利用](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) / [Sandbox](https://developers.openai.com/codex/concepts/sandboxing) / [GitHub PRレビュー](https://learn.chatgpt.com/docs/third-party/github)
- GitHub Copilot: [個人の課金](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals) / [組織の課金](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises) / [学習利用ポリシーの更新](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)
- Cursor: [Team Pricing](https://cursor.com/docs/account/teams/pricing) / [Data use](https://cursor.com/data-use)
- Devin Desktop: [FAQ](https://docs.devin.ai/desktop/devin-desktop-faq) / [Security](https://docs.devin.ai/admin/security)
- Gemini CLI: [GitHub](https://github.com/google-gemini/gemini-cli)
- Cline: [Docs](https://docs.cline.bot/) / [GitHub](https://github.com/cline/cline)
- Roo Code: [Sunset](https://docs.roocode.com/sunset)
- OpenCode: [Docs](https://opencode.ai/docs/) / [GitHub](https://github.com/anomalyco/opencode)
- Google Antigravity: [Models](https://antigravity.google/docs/models/) / [FAQ](https://antigravity.google/docs/faq/) / [Terms](https://antigravity.google/terms/)

### 公式変更履歴・告知

- OpenAI: [ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog)
- GitHub: [個人プランの新規受付再開（2026-06-17）](https://github.blog/changelog/2026-06-17-copilot-individual-plan-sign-ups-are-reopening/) / [ポリシーと課金の変更（2026-08-28）](https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing/) / [Copilot CLI の BYOK・ローカルモデル対応](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/)
- Cursor: [Introducing The X Subscription](https://forum.cursor.com/t/introducing-the-x-subscription/174450) / [Bugbot の課金変更](https://cursor.com/blog/may-2026-bugbot-changes)
- Google: [Gemini CLI から Antigravity CLI への移行](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) / [Google AI サブスクリプションの更新（I/O 2026）](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)

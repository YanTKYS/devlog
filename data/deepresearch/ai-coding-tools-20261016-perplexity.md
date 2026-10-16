以下は、`ai-coding-tools-202610.md` として保存できるMarkdown原文です。確認できない数値や仕様は推測せず、「未確認」「要再確認」と明示しています。

# AIコーディングツール比較調査（2026年10月版）

## 1. 調査概要

- **調査日**：2026年10月16日
- **調査目的**：個人開発者が、用途、開発環境、予算、セキュリティ要件に応じてAIコーディングツールを選定できるよう、機能、料金、利用制限、拡張性、長時間タスクへの対応、データ管理を横断的に整理する。
- **主要対象**：
  - Claude Code
  - Codex
  - GitHub Copilot
  - Cursor
  - Windsurf／Devin Desktop
  - Gemini CLI
  - Cline
  - Roo Code
  - OpenCode
  - Google Antigravity
- **情報源の優先順位**：
  1. 公式料金ページ
  2. 公式ドキュメント
  3. 公式変更履歴・リリースノート
  4. 公式GitHubリポジトリ
  5. 第三者による検証・利用報告
- **確認方針**：
  - 料金、利用上限、モデル、データ保持など、変更頻度が高い事項は2026年10月時点の情報を優先した。
  - 上限が非公開または動的な場合は、具体的なリクエスト数を推測していない。
  - 公式資料間で記載が矛盾する場合は、矛盾を明示した。
  - コード品質や開発速度について、独自ベンチマークを実施していないため断定的な順位付けは行っていない。

### 表記

| 記号 | 意味 |
|---|---|
| ◎ | ネイティブまたは主要機能として対応 |
| ○ | 対応するが、設定または追加構成が必要 |
| △ | 外部サービス、MCP、拡張機能などが必要 |
| － |非対応、または公式資料で確認できない |
| 未確認 | 2026年10月時点の一次資料で確認できなかった |

「無料」は、ツール本体が無料であることと、利用するLLMの推論料金が無料であることを区別して記載する。

***

## 2. 総合比較表

| 製品 | 提供元・正式名称 | 主な提供形態 | 対応環境 | OSS | 無料利用 | BYOK | 主な特徴 |
|---|---|---|---|---|---|---|---|
| Claude Code | Anthropic / Claude Code | CLI、Desktop、VS Code、Web、GitHub Actions、クラウド実行 | Windows、macOS、Linux | 非公開ソース | 原則として有料ClaudeプランまたはAPIが必要 | ○ | ターミナル中心のエージェント。MCP、Hooks、Skills、Subagents、Web並列実行、Chrome連携を備える |
| Codex | OpenAI / Codex | CLI、IDE拡張、ChatGPT Desktop、Web、Codex Cloud | Windows、macOS、Linux | CLIはApache-2.0 | Free・GoにもローカルCodexを含む。クラウド実行は対象外 | ○ | ローカル実行とクラウド委任を統合。MCP、Hooks、Skills、Subagents、サンドボックスに対応 |
| GitHub Copilot | GitHub / GitHub Copilot | IDE、CLI、Desktop、GitHub.com、クラウドエージェント | Windows、macOS、Linux | 非公開ソース | Freeあり | 条件付き○ | GitHub Issue、PR、レビュー、CIとの統合が強い。複数モデルとクラウドエージェントに対応 |
| Cursor | Anysphere / Cursor | AI IDE、CLI、Web、Cloud Agents | Windows、macOS、Linux | 非公開ソース | Freeあり | 限定的 | IDE内編集、クラウドエージェント、ブラウザ操作、Hooks、MCP、並列作業を統合 |
| Windsurf／Devin Desktop | Cognition / Devin Desktop | AI IDE、Desktop、クラウドエージェント | Windows、macOS、Linux | 非公開ソース | プラン依存 | 未確認 | 旧Windsurf。IDEからDevin Local・クラウドDevinへ委任する構成 |
| Gemini CLI | Google / Gemini CLI | CLI、IDE連携、GitHub Actions | Windows、macOS、Linux | OSS | 継続無料枠あり。ただし上限は要再確認 | ○ | Google系モデルとの親和性、MCP、設定ファイル、CLI中心の自動化 |
| Cline | Cline / Cline | VS Code拡張、CLI等 | Windows、macOS、Linux | OSS | ツール本体は無料。モデル料金は別途 | ◎ | APIプロバイダーを選択できるBYOK型。ローカルモデルやMCPと組み合わせやすい |
| Roo Code | Roo Code / Roo Code | VS Code拡張 | Windows、macOS、Linux | OSS | ツール本体は無料。モデル料金は別途 | ◎ | モード、役割、ルールを細かく分離できるCline系エージェント |
| OpenCode | OpenCode / OpenCode | CLI、TUI、Desktop等 | Windows、macOS、Linux | OSS | ツール本体は無料。モデル料金は別途 | ◎ | プロバイダー非依存のターミナル型エージェント |
| Google Antigravity | Google / Google Antigravity | エージェント型開発環境 | 要再確認 | 要再確認 | 要再確認 | 要再確認 | 製品範囲、料金、Gemini CLIとの役割分担を再確認する必要がある |

Claude CodeはWindows 10 1809以降、macOS 13以降、Ubuntu 20.04以降などに対応し、WindowsではPowerShell、CMDまたはGit Bashを利用できる。 Codex CLIはWindows、macOS、Linux向けのインストーラーを提供し、CLI本体はApache License 2.0で公開されている。 [code.claude](https://code.claude.com/docs/en/install)

GitHub CopilotはIDE、CLI、GitHub.com、Desktop、クラウドエージェントまで提供面が広く、Copilot DesktopはWindows、macOS、Linuxに対応する。 CursorはWindows、macOS、Linux向けのVS Code派生IDEとして提供され、Cloud Agentsでは分離されたVM内でブラウザやデスクトップを操作できる。 [docs.github](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app)

2026年にはWindsurfがDevin Desktopへ移行しているため、過去の「Windsurf料金」「Cascadeの機能」を現行仕様としてそのまま参照しないよう注意が必要である。 [docs.devin](https://docs.devin.ai/desktop/devin-desktop-faq)

***

## 3. 料金・利用制限比較表

### 3.1 主要プラン

| 製品 | 無料・入口プラン | 主な個人向け有料プラン | 上限の方式 | 上限到達時 |
|---|---|---|---|---|
| Claude Code | Claude Freeでは原則利用不可 | Pro $20、Max 5x $100、Max 20x $200／月 | 5時間単位のセッション上限＋週間上限 | リセット待ち、プラン変更、Usage Creditsによる追加利用 |
| Codex | Free・GoにローカルCodexを含む。Cloudは対象外 | Plus $20、Pro $100・$200・$500／月 | プラン内Agentic allowance。詳細量は動的・非公開 | 対象プランではクレジット購入に移行 |
| GitHub Copilot | Free：最大2,000コード補完など | Pro $10、Pro+ $39、Max $100／月 | 月間AI Credits | 追加利用予算を設定しない場合は高コスト機能が停止またはアップグレード案内 |
| Cursor | Free $0 | Plus $8、Premium $30、Super $100、Ultra $200／月 | Grokと共有する週間利用プール。第三者モデルは別課金 | Top-upまたは週間リセット待ち |
| Devin Desktop | 要再確認 | Cognition契約・Devinプランに依存 | ACU等の利用単位を含む可能性。現行条件は要再確認 | 要再確認 |
| Gemini CLI | 継続無料枠あり | Google AI、API、Workspace等の条件に依存 | リクエスト数・モデル別レート制限 | 制限解除待ち、API課金、上位プラン |
| Cline | 拡張機能本体は無料 | Cline提供プランまたは各社API課金 | モデルプロバイダーごとのトークン課金 | API残高追加、モデル変更、ローカルモデル利用 |
| Roo Code | 拡張機能本体は無料 | 原則として各社API課金 | モデルプロバイダー依存 | API残高追加、モデル変更、ローカルモデル利用 |
| OpenCode | 本体は無料 | 原則として各社API課金 | モデルプロバイダー依存 | API残高追加、モデル変更、ローカルモデル利用 |
| Google Antigravity | 未確認 | 未確認 | 未確認 | 未確認 |

### 3.2 Claude Code

Claude Codeは単独の定額プランではなく、Claude Pro、Max、Team、EnterpriseまたはAnthropic APIなどを通じて利用する。Proは月払い$20、Max 5xは$100、Max 20xは$200で、APIキー利用時はモデル別の従量課金となる。 [softr](https://www.softr.io/blog/claude-code-pricing)

定額プランには、5時間ごとに更新されるセッション上限と週間上限がある。消費量はモデル、会話の長さ、処理の複雑さ、選択したEffortなどで変動し、固定のメッセージ数は公開されていない。 [support.claude](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work%23:~:text=Automatic%2520context%2520management,-For%2520users%2520with%2520code%2520execution)

上限到達後は、リセットを待つ、プランを変更する、またはUsage Creditsを有効にして標準API相当の従量課金で継続する。Claude Chat、Claude Code、Claude Desktopの利用量は同じプラン上限を共有するため、Claude Codeだけの独立枠ではない。 [support.claude](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work%23:~:text=Automatic%2520context%2520management,-For%2520users%2520with%2520code%2520execution)

### 3.3 Codex

CodexはFreeおよびGoを含むChatGPTプランに含まれるが、Codex Cloudは対象となるPlus、Pro、Business、Enterprise等に限定され、Free・Goには含まれない。 [help.openai](https://help.openai.com/articles/11369540)

ChatGPT Plusは月額$20で、Proは2026年10月時点で$100、$200、$500の3段階が提供されている。Pro $500はCodexなどでUltrafastを利用できる最上位個人プランである。 [help.openai](https://help.openai.com/articles/9793128)

Plus、Proでは、Codex、ChatGPT Work、Excel、PowerPointなどがAgentic allowanceを共有する場合がある。プラン内枠を使い切った後は、対象アカウントではクレジット残高から消費されるが、具体的なタスク数やトークン数は固定公開されていない。 [help.openai](https://help.openai.com/articles/12642688)

ChatGPTサブスクリプションにAPI利用料は含まれない。APIキーでCodexを利用する場合は、ChatGPTプランとは別のAPI従量課金となる。 [help.openai](https://help.openai.com/en/articles/6950777)

### 3.4 GitHub Copilot

2026年10月時点の個人プランは次のとおりである。 [docs.github](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals)

| プラン | 月額 | Base Credits | Flex allotment | 合計AI Credits |
|---|---:|---:|---:|---:|
| Copilot Pro | $10 | 1,000 | 500 | 1,500 |
| Copilot Pro+ | $39 | 3,900 | 3,100 | 7,000 |
| Copilot Max | $100 | 10,000 | 10,000 | 20,000 |

1 AI Creditは$0.01として扱われ、使用モデルの入出力トークン単価からCreditsへ換算される。Base Creditsは固定だが、Flex allotmentはモデル価格やサービス経済性に応じて変化する可能性がある。 [docs.github](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing.md)

未使用Creditsは翌月へ繰り越されず、毎月1日00:00 UTCにリセットされる。含有枠を超えた場合は、追加利用予算をUSDで設定して継続できる。 [docs.github](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals)

Copilot Freeでは最大2,000コード補完などの無料枠が提供されるが、有料プランと同等のモデル、Agent、Cloud Agent利用量が保証されるわけではない。 [docs.github](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-self)

### 3.5 Cursor

2026年10月時点の新料金は次のとおりである。 [cursor](https://cursor.com/pricing)

| プラン | 月額 | 利用量 | 第三者モデル |
|---|---:|---|---|
| Free | $0 | Limited | 基本的に対象外 |
| Plus | $8 | 共有週間プール | Grok系のみ |
| Premium | $30 | Plusの4倍 | API定価で別課金 |
| Super | $100 | Plusの15倍 | API定価で別課金 |
| Ultra | $200 | Plusの50倍 | API定価で別課金 |

各プランの利用プールはCursorとGrokの対象機能で共有され、週間単位で更新される。含有枠到達後はTop-upまたは週間リセット待ちとなる。 [cursor](https://cursor.com/pricing)

Premium以上でClaudeやOpenAI系などの第三者モデルを使用する場合、月額料金にはモデル推論費用が含まれず、API定価相当の利用料を別途購入する。したがって、Premium $30を「ClaudeやGPTを$30の範囲で定額利用できるプラン」と解釈してはならない。 [cursor](https://cursor.com/pricing)

### 3.6 Gemini CLI

Gemini CLIの公式GitHub READMEでは、個人向け無料利用について過去に60 requests/minute、1,000 requests/dayと案内されていた。 ただし、モデル構成、認証方式、Google AIプランとの統合が更新されているため、2026年10月時点の実際の上限は、利用開始前に公式料金ページとアカウント画面で再確認する必要がある。 [github](https://github.com/google-gemini/gemini-cli/blob/main/README.md)

無料枠を超えた場合、Gemini API、Vertex AI、Google Cloud等の従量課金へ切り替える構成が考えられるが、認証方式によって料金、データ処理条件、レート制限が異なる。ツール本体がOSSであっても、Googleモデルの推論が無制限に無料になるわけではない。

### 3.7 Cline・Roo Code・OpenCode

Clineはツール本体をオープンソースで利用でき、各社APIキー、対応プロバイダー、ローカルモデルを選択できる。 通常はツールの月額料金ではなく、選択したLLMの入力、出力、キャッシュ等のトークン料金が発生する。 [docs.cline](https://docs.cline.bot/running-models-locally/overview)

Roo CodeとOpenCodeもBYOKを中心とするため、無料と記載されていても、クラウドLLMを利用する場合はモデル提供元への支払いが必要となる。無料運用にはローカルLLMが必要だが、必要メモリ、処理速度、ツール呼び出し能力、コード生成品質はモデルとPC性能に依存する。

***

## 4. 機能比較表

### 4.1 開発・GitHub・クラウド

| 製品 | 複数ファイル編集 | リポジトリ探索 | コマンド・テスト | Git操作 | Issue→PR | コードレビュー | ブラウザ操作 | 非同期クラウド | 並列Agent |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Claude Code | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ○ | ◎ | ◎ |
| Codex | ◎ | ◎ | ◎ | ◎ | ○ | ○ | ○ | ◎ | ◎ |
| GitHub Copilot | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ○ | ◎ | ◎ |
| Cursor | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| Devin Desktop | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| Gemini CLI | ◎ | ◎ | ◎ | ○ | ○ | ○ | △ | △ | 要確認 |
| Cline | ◎ | ◎ | ◎ | ○ | △ | ○ | ○ | － | △ |
| Roo Code | ◎ | ◎ | ◎ | ○ | △ | ○ | ○ | － | ◎ |
| OpenCode | ◎ | ◎ | ◎ | ○ | △ | ○ | △ | － | 要確認 |
| Google Antigravity | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 |

Claude CodeのGitHub Actionsは、IssueまたはPRコメントで`@claude`を指定して、コード分析、実装、コミット、PR作成、レビューを実行できる。ただし、GitHub App、Workflow、認証シークレットの構成が必要である。 [code.claude](https://code.claude.com/docs/en/github-actions?38d7aa68_page)

GitHub CopilotのCloud Agentは、Issueを起点に一時的な隔離環境でブランチ作成、コード変更、PR作成を実行できる。Copilot CLIはローカルでファイル変更やコマンド実行を行い、Desktopでは複数の並列ワークストリームを管理できる。 [docs.github](https://docs.github.com/en/copilot/responsible-use/agents)

Cursor Cloud Agentsは分離されたクラウドVMでリポジトリ、依存関係、シークレット、ネットワークを構成し、機能実装、テスト、PR作成、動作動画の生成まで実行できる。 ブラウザおよびデスクトップ操作に対応し、Webアプリを起動してUIフローを確認できる。 [cursor](https://cursor.com/docs/cloud-agent/capabilities.md)

### 4.2 拡張・カスタマイズ

| 製品 | MCP | Hooks | ルールファイル | Skills | カスタムAgent | プラグイン | 権限承認 | ローカルLLM |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| Claude Code | ◎ | ◎ | `CLAUDE.md` | ◎ | ◎ | ◎ | ◎ | △ |
| Codex | ◎ | ◎ | `AGENTS.md`、`.codex/config.toml` | ◎ | ◎ | ◎ | ◎ | △ |
| GitHub Copilot | ◎ | ◎ | `.github/copilot-instructions.md`、`AGENTS.md` | ◎ | ◎ | ◎ | ◎ | 条件付き |
| Cursor | ◎ | ◎ | `.cursor/rules`、`AGENTS.md` | ◎ | ◎ | ◎ | ◎ | 限定的 |
| Devin Desktop | ◎ | ○ | プロジェクト設定・Skills | ◎ | ◎ | ○ | ◎ | 未確認 |
| Gemini CLI | ◎ | ○ | `GEMINI.md`等 | ○ | 要確認 | ○ | ◎ | △ |
| Cline | ◎ | ○ | `.clinerules`等 | ○ | 限定的 | ○ | ◎ | ◎ |
| Roo Code | ◎ | ○ | `.roo/rules`等 | ○ | ◎ | ○ | ◎ | ◎ |
| OpenCode | ◎ | 要確認 | `AGENTS.md`等 | 要確認 | 要確認 | 要確認 | ◎ | ◎ |
| Google Antigravity | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 | 要確認 |

Claude Codeでは、`CLAUDE.md`が常時読み込むプロジェクト指示、Skillsが必要時に読み込む手順、MCPが外部システムとの接続、Subagentsが独立コンテキストでの委任、Hooksがライフサイクルイベントに対する決定的な処理を担当する。 [code.claude](https://code.claude.com/docs/pt/features-overview)

CodexではMCP、Skills、Subagents、Pluginsを組み合わせられる。Hooksは`hooks.json`または`config.toml`に定義し、`PreToolUse`、`PostToolUse`、`PreCompact`、`SubagentStop`などでスクリプトやMCPツールを実行できる。 [learn.chatgpt](https://learn.chatgpt.com/docs/hooks)

GitHub Copilot CLIでは、PluginsがMCP、Agents、Skills、Hooksをまとめて配布でき、`preToolUse`でツール呼び出しを拒否・変更し、`postToolUse`で後処理できる。 Copilot code reviewもSkillsと読み取り専用MCPを利用できる。 [github](https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/)

CursorのPluginsはRules、Skills、Agents、Commands、MCP、Hooksをまとめて配布できる。 Cloud Agentsでもリポジトリ内の`.cursor/hooks.json`が実行され、ファイル編集、シェル実行、Subagent開始・終了、コンテキスト圧縮などを監視できる。 [cursor](https://cursor.com/help/ai-features/cloud-agents)

***

## 5. 製品別詳細

## 5.1 Claude Code

### 基本情報

Claude CodeはAnthropicのエージェント型コーディング環境で、CLI、VS Code、Desktop、Web、GitHub Actionsなどから利用できる。同じエンジンを複数のSurfaceで使用し、リポジトリの`CLAUDE.md`、設定、MCP構成を共有できる。 [code.claude](https://code.claude.com/docs)

対応OSはWindows 10 1809以降、macOS 13以降、Ubuntu 20.04以降、Debian 10以降、Alpine Linux 3.19以降である。WindowsネイティブではGit for Windowsが推奨されるが、未導入の場合はPowerShellをシェルツールとして利用する。 [code.claude](https://code.claude.com/docs/en/quickstart)

### 開発機能

- 複数ファイルの生成・修正
- コードベース探索
- シェルコマンド、ビルド、テスト実行
- Git diff、commit等の操作
- MCPによる外部サービス接続
- GitHub ActionsによるIssue、PR起点の実装
- 自動コードレビュー
- Webでの長時間タスク・並列タスク
- Subagentsによる独立コンテキストの処理
- Chrome拡張によるWebアプリのテスト・デバッグ

Chrome連携はCLIまたはVS Codeから使用でき、Chrome、Edge、その他のChromium系ブラウザを操作できる。ただし、WSL上のClaude CodeからChrome連携を使用する構成はサポートされていない。 [code.claude](https://code.claude.com/docs/en/chrome)

### 長時間作業

Claude Codeは各ターン開始時にチェックポイントを作成し、コード、会話、またはその両方を過去の状態へ戻せる。セッション再開後も`/rewind`を使用でき、会話の一部を要約してコンテキストを解放できる。 [code.claude](https://code.claude.com/docs/en/checkpointing)

Web版ではローカル環境を起動したままにせず長時間タスクを実行でき、複数タスクを並列に開始できる。 [code.claude](https://code.claude.com/docs)

### セキュリティ

Manual modeでは、ファイル変更、シェルコマンド、ネットワーク接続などの多くの操作で確認を求める。権限設定とOSレベルのSandboxは別の防御層として動作する。 [code.claude](https://code.claude.com/docs/es/permissions)

組み込みBash SandboxはmacOS、Linux、WSL2で利用できるが、Windowsネイティブには対応しない。WindowsではWSL2、コンテナ、VMなどを使用する必要がある。 [code.claude](https://code.claude.com/docs/en/sandbox-environments)

Free、Pro、Max等の個人利用では、モデル改善を許可した場合、Claude Codeのコーディングセッションがモデル改善に使われ、最大5年間保持される可能性がある。許可しない場合の標準保持期間は30日と案内されている。 [privacy.anthropic](https://privacy.anthropic.com/ja/articles/10301952-%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E3%83%9D%E3%83%AA%E3%82%B7%E3%83%BC%E3%81%AE%E6%9B%B4%E6%96%B0)

Team、Enterprise、APIなどの商用条件では、明示的に選択しない限りコードやプロンプトをモデル学習に使用しない。標準保持は30日で、適格なEnterprise組織ではZero Data Retentionを申請できる。 [docs.anthropic](https://docs.anthropic.com/en/docs/claude-code/data-usage)

### 適する用途

- ターミナル中心で大きめの改修を任せたい
- HooksやSubagentsを使って独自ワークフローを構築したい
- GitHub ActionsからIssue、PR起点で実装したい
- ブラウザを含むWebアプリの確認を自動化したい
- 定額プランとAPI従量課金を使い分けたい

### 注意点

- 定額プランでも完全無制限ではない。
- Claude Chat、Claude Desktopと利用枠を共有する。
- 5時間上限と週間上限の具体値は非公開・動的である。
- WindowsネイティブではSandboxとChrome連携の制約を確認する。
- 個人プランで機密コードを扱う場合はモデル改善設定を確認する。

***

## 5.2 Codex

### 基本情報

CodexはOpenAIのコーディングエージェントで、CLI、IDE拡張、ChatGPT Desktop、Web、クラウドタスクとして提供される。ローカルワークフローは利用者の端末で、クラウドタスクはOpenAI管理環境で実行される。 [help.openai](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan?ref)

Codex CLIはWindows、macOS、Linuxに対応し、Apache License 2.0で公開されている。 [learn.chatgpt](https://learn.chatgpt.com/docs/codex/cli.md)

### 開発機能

- リポジトリ探索
- 複数ファイル編集
- コマンド、テスト、ビルド実行
- モデルとReasoning Effortの選択
- MCP
- Skills
- Subagents
- Plugins
- Lifecycle Hooks
- ローカルSandbox
- クラウドへのタスク委任
- Desktop、CLI、IDE間の設定共有

MCP設定は`~/.codex/config.toml`またはプロジェクトの`.codex/config.toml`に保存され、Desktop、CLI、IDE拡張で共有できる。 [learn.chatgpt](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

HooksはスクリプトまたはMCPツールをエージェントループ中に実行でき、秘密情報検出、監査ログ、検証、記憶作成などに利用できる。非管理Hooksは内容のハッシュ単位で信頼確認が必要となる。 [learn.chatgpt](https://learn.chatgpt.com/docs/hooks)

### 料金

- Free・Go：Codexを含むが、Codex Cloudは含まれない
- Plus：$20／月
- Pro：$100、$200、$500／月
- Business：$20／ユーザー／月と案内される構成あり
- Enterprise：契約
- API：サブスクリプションとは別の従量課金

含有利用量はタスク内容、モデル、処理時間などで変動するため、固定タスク数として扱わない。Plus・Proでは他のAgentic機能と利用枠を共有する可能性がある。 [learn.chatgpt](https://learn.chatgpt.com/docs/pricing?site_variant=chatgpt&translationFallback=zh-Hans)

### セキュリティ

CLIでは`/permissions`からファイル編集やコマンド実行の承認範囲を設定し、書き込み可能なRootとSandbox状態を確認できる。 [learn.chatgpt](https://learn.chatgpt.com/docs/codex/cli?translationFallback=zh-Hans)

個人向けChatGPTプランでは、モデル改善設定が有効な場合にCodexタスクがモデル学習へ利用される可能性がある。ChatGPTの「Improve the model for everyone」を無効にすることで、新しいタスクを学習対象外にできる。 [help.openai](https://help.openai.com/en/articles/7730893-data-controls-faq%3F.gz)

Business、Enterprise、Edu、APIの入出力は、標準ではモデル学習に利用されない。EnterpriseではCodex CLIやIDE拡張を含む利用状況をCompliance APIから確認できる。 [help.openai](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan?ref)

### 適する用途

- ChatGPT PlusまたはProを既に契約している
- ローカルCLIとクラウドタスクを同一製品で使い分けたい
- OSSのCLIをベースに設定を管理したい
- MCP、Hooks、Skills、Subagentsを組み合わせたい
- OpenAIモデルを中心に開発したい

### 注意点

- ChatGPT契約とAPI料金は別である。
- Free・GoではCodex Cloudを利用できない。
- 利用枠の具体的トークン数やタスク数は公開固定値ではない。
- ローカルHooksがクラウドオーケストレーションでも同じように動くとは限らない。 [learn.chatgpt](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

***

## 5.3 GitHub Copilot

### 基本情報

GitHub Copilotは、IDE補完、Chat、Agent mode、CLI、Desktop、GitHub.com、Cloud Agent、Code Reviewを提供するGitHub統合型のAI開発環境である。

対応IDEにはVS Code、Visual Studio、JetBrains IDE、Eclipse、Xcodeなどがある。 [docs.github](https://docs.github.com/en/copilot/get-started/quickstart-for-using-github-copilot-in-your-ide)

### 開発機能

- インラインコード補完
- Chat
- 複数ファイル編集
- IDE Agent mode
- Copilot CLI
- GitHub IssueからのCloud Agent起動
- PR作成
- PRコードレビュー
- MCP
- Skills
- Custom Agents
- Plugins
- Hooks
- `/fleet`による並列Subagents
- GitHub Actions、CI、ブランチとの統合
- Desktopでの並列ワークストリーム

Copilot CLIは計画、実装、テスト、レビューをターミナル内で実行し、Explore、Task、Code Review、Planなどの専門Agentへ処理を委任できる。 [github](https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/)

### BYOK

GitHub Copilot Chatでは、組織が対応する第三者モデルプロバイダーのAPIキーを設定できるBYOK構成がある。 この場合、プロンプト、コードコンテキスト、生成結果は設定したモデルプロバイダーへ直接送られ、GitHubを経由しない場合があるため、モデル提供元の利用規約とデータ処理条件を別途確認する必要がある。 [docs.github](https://docs.github.com/en/copilot/responsible-use/chat?tool=vscode)

### セキュリティ

Copilot Cloud Agentは一時的でファイアウォール保護された環境で動作し、セキュリティスキャンを実行する。 [docs.github](https://docs.github.com/en/copilot/responsible-use/agents)

BusinessおよびEnterpriseのデータはGitHubのモデル学習には利用されない。 個人プランについては、データ共有設定、利用Surface、選択モデルによって条件が変わるため、組織利用ではBusiness以上を基準に判断する。 [github](https://github.com/features/copilot/copilot-business)

### 適する用途

- GitHub Issue、PR、レビューを中心に開発する
- IDE補完とAgentを一つの契約で利用したい
- 複数モデルを比較しながら使いたい
- GitHub Enterpriseの権限・監査体系へ組み込みたい
- 個人開発で月$10程度から始めたい

### 注意点

- 2026年のAI Credits方式では、モデルごとに消費量が異なる。
- Flex allotmentは将来変更される可能性がある。
- Creditsを使い切った後の追加利用には予算設定が必要となる。
- BYOK時はGitHubではなくモデル提供元のデータ条件が適用される。

***

## 5.4 Cursor

### 基本情報

CursorはVS Codeを基盤とするAI IDEで、ローカルAgent、Cloud Agents、Web、CLI、Plugins、MCP、Hooksを統合する。

2026年10月時点の新規料金体系では、CursorはGrok等と共通の週間利用プールを持つ構成へ変更されている。 [cursor](https://cursor.com/pricing)

### 開発機能

- インライン補完
- Chat
- Agentによる複数ファイル編集
- リポジトリ探索
- コマンド・テスト実行
- Git操作
- Cloud Agents
- ブラウザ・デスクトップ操作
- 複数リポジトリを含むクラウド環境
- MCP
- Hooks
- Rules
- Skills
- Custom Agents
- Plugins
- Subagents
- 並列Agent

Cloud AgentsはGitHub、GitLab、Azure DevOps、Bitbucket Cloudと接続し、分離VMでコード変更、テスト、PR作成、ブラウザ確認を実行できる。 [cursor](https://cursor.com/help/ai-features/cloud-agents)

### 料金上の特徴

PlusはGrokモデルのみで、第三者モデルを利用するにはPremium以上が必要となる。Premium以上でもClaude、GPT等の利用料金は月額に含まれず、別のプリペイド利用料からAPI定価相当で消費される。 [cursor](https://cursor.com/pricing)

### セキュリティ

CursorはPrivacy Modeを組織単位で強制でき、Cursor経由モデルに対するZero Data Retentionの条件を適用できる。組織利用ではSandbox、Auto-review、Hooks、MCP allowlist等を組み合わせることが推奨されている。 [cursor](https://cursor.com/docs/enterprise/security-hardening)

Self-Hosted MachinesではAgent loopはCursorクラウドで動作するが、ファイル編集、コマンド、ブラウザ操作、stdio MCPは利用者のマシンで実行できる。完全なローカル処理ではない点に注意する。 [cursor](https://cursor.com/docs/cloud-agent/self-hosted/my-machines)

### 適する用途

- IDE内で設計、編集、実行、確認を完結したい
- Webアプリの画面をAgentに操作・検証させたい
- 複数Agentを並列に動かしたい
- Rules、Hooks、Pluginsで開発環境を標準化したい
- Cloud Agentsに長時間作業を任せたい

### 注意点

- 旧Cursor Pro料金の記事を現行料金として参照しない。
- 新料金では第三者モデルが別課金である。
- GrokとCursorで週間利用枠を共有する。
- Cloud AgentやSelf-Hosted MachinesでもAgent loop自体はクラウド側である。

***

## 5.5 Windsurf／Devin Desktop

### 基本情報

2026年10月時点では、Windsurf単独製品としてではなく、CognitionのDevin Desktopとして評価する必要がある。旧Cascadeや旧Windsurfのレビューは、現行のDevin Local、Desktop、Cloud Devinと一致しない可能性がある。 [docs.devin](https://docs.devin.ai/desktop/devin-desktop-faq)

Devinはクラウドエージェントであり、独自のインフラと実行環境で動作する。 Devin DesktopはローカルIDEとクラウドDevinを接続する役割を持つ。 [old.cognition](https://old.cognition.ai/blog/devin-in-windsurf)

### 組織機能

Devin DesktopはWindows、macOS、Linuxで中央管理ポリシーを配布できる。WindowsではグループポリシーとADMXテンプレートを利用できるため、Active Directory管理環境への導入候補となる。 [docs.devin](https://docs.devin.ai/de/desktop/enterprise-policies)

EnterpriseではRBAC、IPアクセスリスト、Security Profiles、AI Guardrailsなどの管理機能が提供される。 [docs.devin](https://docs.devin.ai/llms.txt)

### セキュリティ

Enterprise CloudではDevin BrainとDevboxがCognitionのマルチテナントクラウドで動作し、各セッションは分離されたマシン上で実行される。Customer Dedicated Deploymentでは、単一テナントVPCとPrivateLinkまたはIPSecを利用できる。 [docs.devin](https://docs.devin.ai/enterprise/deployment/overview.md)

モデル学習条件について、Cognitionの公式ドキュメントには「標準では学習しない」という記載と、「個人・有料プランでは標準で学習に使う可能性があり、設定でオプトアウトする」という異なる記載が存在する。 導入時は画面上のData Controls、契約書、DPAを優先して確認する必要がある。 [docs.devin](https://docs.devin.ai/admin/security)

### 適する用途

- IDE作業とクラウド型自律Agentを統合したい
- GitHub、GitLab、Bitbucket、Azure DevOpsを横断したい
- 長時間タスクや複数セッションをクラウドで処理したい
- Windowsグループポリシー、RBAC、専用環境を必要とする組織

### 注意点

- Windsurf時代の料金・機能記事は現行資料と分離する。
- 料金と利用単位は契約画面で再確認する。
- データ学習条件は公式資料間で差異がある。
- 閉域環境ではCognition側クラウドへの接続要件を満たせるか確認する。

***

## 5.6 Gemini CLI

### 基本情報

Gemini CLIはGoogleのターミナル型AIエージェントで、コードベースの探索、ファイル編集、シェル実行、GoogleのGeminiモデル利用を中心とする。ツール本体とモデル推論料金は分けて評価する。

### 主な評価点

- CLI中心で自動化しやすい
- GoogleアカウントまたはAPI認証を利用できる
- MCP、プロジェクト指示ファイル、コマンド実行を組み合わせられる
- Google Cloud、Vertex AI、Gemini APIを利用する開発と親和性がある
- GitHub Actions等のCI構成に組み込みやすい

### 料金

過去の公式READMEでは個人向け無料枠として60 requests/minute、1,000 requests/dayが案内されていた。 ただし、この数字を2026年10月時点の全認証方式・全モデル共通上限として扱わず、公式料金ページと実際のアカウント画面で確認する。 [github](https://github.com/google-gemini/gemini-cli/blob/main/README.md)

### 適する用途

- 低コストでCLI型Agentを試したい
- Google Cloud、Firebase、Android等を多く利用する
- OSSのCLIをGitHub Actionsやスクリプトに組み込みたい
- Gemini APIまたはVertex AIの契約を既に持っている

### 注意点

- 無料枠と無料トライアルを混同しない。
- 個人Googleアカウント、APIキー、Vertex AIで料金・上限・データ条件が異なる。
- Google Antigravityと同じ製品ではなく、役割を分けて確認する。

***

## 5.7 Cline

### 基本情報

Clineは主にVS Code上で動作するオープンソースのエージェント型拡張で、BYOKを中心に複数のLLMプロバイダーやローカルモデルを利用できる。 [github](https://github.com/cline/cline/blob/main/apps/vscode/README.marketplace.md)

### 開発機能

- 複数ファイル編集
- リポジトリ探索
- ターミナルコマンド実行
- テスト・ビルド
- ブラウザ操作
- MCP
- プロジェクトルール
- 操作ごとの承認
- APIプロバイダー切替
- ローカルLLM

### 料金

拡張機能自体を無料で利用しても、Anthropic、OpenAI、Google等のクラウドモデルを選択した場合は各社API料金が発生する。自律的な探索、ファイル読み込み、テスト再試行によってトークン消費が増えやすいため、API側の予算上限を設定する必要がある。

### 適する用途

- 特定ベンダーの月額プランへ固定されたくない
- API料金を自分で監視・制御したい
- ローカルLLMや社内推論APIを試したい
- VS Codeを維持しながらAgent機能を追加したい
- MCPサーバーを自分で構成したい

### 注意点

- BYOKは「無料」ではなく、支払先がモデル提供元になる方式である。
- 高性能モデルで長時間Agentを動かすと月額型サービスより高くなる場合がある。
- モデルごとにツール呼び出し能力が異なる。
- 組織的な監査・ポリシー管理は商用統合製品より自前構築が増える。

***

## 5.8 Roo Code

### 基本情報

Roo CodeはCline系の設計を発展させたVS Code拡張で、役割やモードを分離し、用途ごとにプロンプト、ツール権限、モデルを切り替える運用に向く。

### 主な評価点

- BYOK
- 複数プロバイダー
- ローカルLLM
- MCP
- Custom Modes
- プロジェクトルール
- 複数Agentまたは役割分担
- ターミナル・ファイル操作の承認
- オープンソース

### 適する用途

- Architect、Code、Debug、Reviewなどの役割を明確に分けたい
- モードごとにモデルや権限を変更したい
- Clineより細かなワークフロー構成を求める
- ローカルLLMや社内APIを使用したい

### 注意点

- 使用するLLMの料金は別途必要である。
- モード、MCP、ルールを増やすほど設定管理が複雑になる。
- クラウド非同期タスクや組織監査は別途仕組みが必要となる。
- 2026年10月時点の正式な企業向けプランとデータ保持条件は要再確認。

***

## 5.9 OpenCode

### 基本情報

OpenCodeはプロバイダー非依存を志向するオープンソースのターミナル型AIコーディングエージェントである。CLIまたはTUI中心で、APIプロバイダーやローカルモデルを選択する用途に向く。

### 主な評価点

- ターミナル中心
- BYOK
- 複数モデルプロバイダー
- ローカルLLM
- ファイル編集
- コマンド実行
- プロジェクト指示
- MCP対応構成
- OSSとしての改変・自前運用

### 適する用途

- IDEへの依存を減らしたい
- SSH、サーバー、コンテナ内でAgentを使用したい
- モデル提供元を頻繁に変更したい
- OSSを基礎に独自ツールを内製したい

### 注意点

- 正式ライセンス、対応プロバイダー、MCP、Hooks、Subagentsの2026年10月時点の仕様は公式リポジトリで再確認する。
- クラウド非同期Agent、GitHub App、企業監査などは統合製品ほど一体化されていない。
- 同名または類似名のプロジェクトがあるため、リポジトリ所有者を確認する。

***

## 5.10 Google Antigravity

### 確認状況

2026年10月時点で、「Google Antigravity」という名称が指す正式な製品範囲、料金、一般提供状況、対応OS、Gemini CLIとの役割分担を十分に確定できなかった。

以下は未確認として扱う。

- 正式サービス名称
- 一般提供、Preview、招待制の区別
- 個人向け料金
- WorkspaceまたはGoogle Cloud契約との関係
- Gemini CLIとの利用枠共有
- BYOK
- OSSライセンス
- MCP、Hooks、Skills
- データ保持・モデル学習条件
- Windowsネイティブ対応
- GitHub連携
- クラウド非同期実行

「Google製のAgentic IDE」等の第三者記事だけを根拠に、正式提供済み製品として導入判断しない。公式発表、公式ドキュメント、公式料金ページを確認できるまで比較表では「未確認」とする。

***

## 6. シナリオ別比較

| シナリオ | 第一候補 | 代替候補 | 判断理由・トレードオフ |
|---|---|---|---|
| 個人開発・小規模ツール | Copilot Pro、Claude Code Pro、Codex Plus、Cursor Plus/Premium | Cline、Roo Code、OpenCode | 月額予算を固定するなら定額型。モデルを選びたいならBYOK型 |
| 既存リポジトリ保守 | Claude Code、Codex、Copilot、Cursor | Cline、Roo Code | 探索、テスト、複数ファイル編集、再開機能が重要 |
| 大きめの複数ファイル開発 | Claude Code、Codex、Cursor、Devin | Copilot CLI | Subagents、クラウド実行、長時間タスク、チェックポイントを重視 |
| GitHub中心 | GitHub Copilot | Claude Code GitHub Actions、Codex、Cursor | Issue、PR、レビュー、権限との統合はCopilotが直接的 |
| 料金を抑える | Gemini CLI、Cline＋安価API、Roo Code＋ローカルLLM、OpenCode＋ローカルLLM | Copilot Free | 無料枠と推論費用を分けて管理する必要がある |
| Windows中心 | Copilot、Codex、Claude Code、Cursor | Cline、Roo Code | ネイティブWindows対応を優先。SandboxやWSL制約は個別確認 |
| Webアプリ開発 | Cursor、Claude Code＋Chrome、Cline | Codex、Devin | ブラウザ操作、スクリーンショット、UIフロー確認が重要 |
| 組織的開発 | Copilot Business/Enterprise、Claude Enterprise、Cursor Enterprise、Devin Enterprise | Codex Business/Enterprise | SSO、RBAC、監査、データ学習除外、保持期間、専用環境を重視 |

### 6.1 個人開発・小規模ツール

短時間の実装とGitHubコミットを優先する場合、IDE補完とAgentを低価格で利用できるCopilot Proが扱いやすい。月額$10で1,500 AI Creditsが含まれ、GitHubとの接続が標準化されている。 [docs.github](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals)

ターミナルから要件をまとめて実装させる場合はClaude Code ProまたはCodex Plusが候補になる。ただし、両製品とも他のChat機能と利用枠を共有するため、コーディング専用の完全定額枠ではない。 [help.openai](https://help.openai.com/articles/12642688)

API利用量が少ない場合はCline、Roo Code、OpenCodeのBYOKが安くなる可能性がある。一方、Agentが多数のファイルを読み、テストを繰り返す場合はAPI課金が急増するため、予算上限を設定する。

### 6.2 既存リポジトリの保守

既存コードの理解、バグ修正、テスト、リファクタリングでは、リポジトリ探索とコマンド実行を一連のAgent loopで処理できるClaude Code、Codex、Copilot CLI、Cursorが候補となる。

保守作業では生成量よりも、次の機能を優先する。

- 差分の確認
- テスト失敗後の再試行
- コードレビュー
- チェックポイントまたはGitによるロールバック
- プロジェクト指示ファイル
- コマンド実行前の承認
- 長い会話の圧縮・再開

Claude Codeはコードと会話をチェックポイント単位で巻き戻せるため、試行錯誤の多い保守に適する。 [code.claude](https://code.claude.com/docs/en/checkpointing)

### 6.3 複数ファイルにまたがる開発

大きめの機能を一括で依頼する場合、モデル名だけでなく、コンテキスト管理、Subagents、作業再開、テスト、権限、Git分離を比較する。

Cursor Cloud Agents、Copilot Desktop、Claude Code Webなどは、ローカル端末を占有せず複数タスクを並列処理できる。 一方、クラウド環境へリポジトリやシークレットを送るため、機密性の高いコードでは組織契約とデータ条件を確認する。 [docs.github](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app)

### 6.4 GitHub中心の開発

GitHub Issue、PR、レビューを起点にする場合はGitHub Copilotが第一候補となる。Cloud Agent、Code Review、GitHub MCP、CLI、Desktopが同じGitHub権限体系と直接連携するためである。 [github](https://github.com/features/copilot/cli)

Claude CodeもGitHub Actionsを使用して`@claude`からIssue実装やPRレビューを行えるが、Workflow、App、Secretのセットアップが必要となる。 [code.claude](https://code.claude.com/docs/en/github-actions?38d7aa68_page)

### 6.5 利用料金を抑える開発

料金を抑える方法は次の3種類に分かれる。

1. **継続無料枠**：Gemini CLI、Copilot Free等を利用する。
2. **低価格定額**：Copilot Pro、Cursor Plus等を利用する。
3. **BYOK・ローカルLLM**：Cline、Roo Code、OpenCodeを利用する。

ローカルLLMは推論料金を抑えられるが、GPU・RAM、電力、処理時間、モデル更新、ツール呼び出し精度を自分で管理する。クラウドAPIを使うBYOKでは、入力・出力単価だけでなく、キャッシュ、長いコンテキスト、再試行回数を含めて比較する。

### 6.6 Windows中心の開発

Windowsネイティブを優先する場合、GitHub Copilot、Codex、Claude Code、Cursor、Cline、Roo Codeが候補になる。

Claude CodeはWindowsネイティブでPowerShellまたはGit Bashを利用できるが、組み込みBash SandboxはWindowsネイティブ非対応である。 また、WSL上のClaude CodeではChrome連携を使用できないため、ブラウザテストが必要ならWindowsネイティブ版を検討する。 [code.claude](https://code.claude.com/docs/en/chrome)

Devin DesktopはWindowsグループポリシーとADMXテンプレートを提供するため、Active Directory管理端末への一括導入候補となる。 [docs.devin](https://docs.devin.ai/de/desktop/enterprise-policies)

### 6.7 Webアプリケーション開発

UI実装とブラウザ確認を含む場合はCursor Cloud Agents、Claude Code＋Chrome、Cline、Devinが候補となる。

Cursor Cloud Agentsは分離VM内でブラウザを操作し、開発サーバーを起動してUIフローを検証できる。 Claude CodeはChrome拡張と連携し、CLIやVS Codeからブラウザのテスト、Console確認、フォーム操作を実行できる。 [cursor](https://cursor.com/docs/cloud-agent/capabilities.md)

ただし、画面操作ができることと、UI/UX品質を正確に評価できることは同義ではない。アクセシビリティ検査、Visual Regression、Lighthouse、Playwright等の機械的検証を併用する。

### 6.8 組織的な開発

組織導入では、個人向けプランの機能数よりも次を優先する。

- SSO・SCIM
- RBAC
- 監査ログ・Compliance API
- リポジトリ単位のアクセス制御
- モデル学習への不使用
- データ保持期間
- Zero Data Retention
- MCP・PluginsのAllowlist
- Hooksの強制
- ネットワーク出口制御
- Sandbox
- 専用テナントまたは専用VPC
- BYOK時のモデル提供元管理

GitHub中心の組織ではCopilot Business／Enterprise、Anthropic中心ではClaude Team／Enterprise、IDE統一ではCursor Enterprise、長時間クラウドAgentではDevin Enterpriseが主な候補になる。

自治体や閉域に近い環境では、インターネット接続が前提となる製品をそのまま導入できない可能性がある。Cline、Roo Code、OpenCodeとローカルLLMまたは庁内推論APIの組み合わせは技術的候補になるが、モデル配布、端末性能、ログ、認証、アップデートを内製する必要がある。

***

## 7. その他の注目製品

詳細調査対象外だが、今後の比較候補として次を挙げる。

| 製品 | 主な位置付け | 確認すべき点 |
|---|---|---|
| Aider | Git連携を重視するCLI型OSSツール | 対応モデル、Repo Map、API費用、Windows運用 |
| Continue | IDE拡張・OSS・モデル選択型 | Agent機能、ローカルLLM、組織管理 |
| JetBrains AI Assistant／Junie | JetBrains IDE統合 | IDEライセンスとの関係、利用枠、クラウドAgent |
| Amazon Q Developer／Kiro | AWS・IDE・Agent開発 | AWS統合、料金、企業向けデータ条件 |
| Zed Agent Panel | 高速エディタ統合型 | Windows対応、モデル課金、拡張性 |

これらは主要10製品と同じ深度では確認していないため、選定対象へ加える場合は別途料金、利用制限、セキュリティを調査する。

***

## 8. 比較上の注意点

### 無料の意味

「無料」には少なくとも次の違いがある。

- ツール本体だけ無料
- 無料トライアル
- 毎日または毎月更新される継続無料枠
- 特定モデルだけ無料
- ローカルLLM利用時のみ推論料金不要
- クレジットカード登録が必要な無料クレジット
- 学生、OSS Maintainer等に限定した無償提供

Cline、Roo Code、OpenCodeはツール本体を無料利用できても、クラウドLLMを選べばAPI料金が発生する。Cursor Premiumも第三者モデル料金は月額に含まれない。 [cursor](https://cursor.com/pricing)

### サブスクリプションとAPI

Claude、Codexなどでは、WebまたはChatサブスクリプションとAPI利用料は別である。サブスクリプション認証をCLIで使用できる場合でも、APIキーを設定した実行は別の従量課金になる可能性がある。

### 固定回数ではない上限

現在のAIコーディングAgentは、1リクエストの消費量が一定ではない。次の条件で消費量が変わる。

- モデル
- ReasoningまたはEffort
- リポジトリ規模
- 読み込むファイル数
- 会話履歴
- MCP出力
- テストログ
- Subagents数
- 失敗後の再試行
- キャッシュ利用
- クラウド環境の実行時間

公式が固定回数を公開していない場合、「1日○回使える」などの利用者報告を公式上限として記載しない。

### モデル名だけで比較しない

同じモデルを使用できても、ツールによって次が異なる。

- コンテキストへ含めるファイルの選択
- Repo Index
- Prompt構成
- Tool定義
- Edit形式
- Test loop
- Context compaction
- Cache
- Sandbox
- 権限承認
- Git worktree
- Subagentの構成

したがって、「同じClaudeモデルだからClaude CodeとCursorの結果が同じ」とは限らない。

### BYOKの責任範囲

BYOKではモデル選択の自由度が高い一方、次を利用者が管理する。

- APIキー
- 利用上限
- 支払先
- ログ
- データ保持
- モデル学習条件
- リージョン
- 障害
- モデル廃止
- レート制限

GitHub CopilotのBYOKのように、データがGitHubを経由せず選択したプロバイダーへ直接送られる場合もある。 [docs.github](https://docs.github.com/en/copilot/responsible-use/agents)

### ローカル処理の範囲

「ローカルAgent」「Self-hosted」「Local execution」は、モデル推論までローカルであることを意味しない場合がある。

- ファイル・コマンドだけローカル
- Agent loopはクラウド
- HTTP MCPはクラウド、stdio MCPはローカル
- Repo Indexはクラウド
- Telemetryだけ外部送信
- モデル推論は外部API

導入時は、ソースコード、プロンプト、インデックス、ログ、スクリーンショットがどこへ送信されるかを分解して確認する。

### エージェント権限

`AGENTS.md`、`CLAUDE.md`、Rules等の指示は、セキュリティ境界ではない。モデルへの指示と、Sandbox、Allowlist、Hooks、OS権限を分離する。

Claude Codeではプロンプトや`CLAUDE.md`が「何を試みるか」を制御し、PermissionsとSandboxが「実際に何を許可するか」を制御する。 [code.claude](https://code.claude.com/docs/es/permissions)

***

## 9. 更新頻度が高い項目

次の項目は、少なくとも月次または導入直前に再確認する。

| 項目 | 再確認理由 |
|---|---|
| 月額料金 | 値上げ、統合プラン、旧契約の経過措置がある |
| 含有クレジット | Flex枠やキャンペーンが変動する |
| 利用上限 | 5時間、週間、月間などの上限が動的 |
| モデル一覧 | 新モデル追加、旧モデル廃止、Preview終了 |
| モデル単価 | 入力、出力、キャッシュ単価が変更される |
| 無料枠 | トライアルと継続無料枠が変更される |
| BYOK | 対応プロバイダーや利用可能プランが変わる |
| Cloud Agent | 対応リポジトリ、実行環境、VM料金が変わる |
| Hooks・MCP | 対応イベント、Transport、管理ポリシーが変わる |
| データ学習 | 個人・法人プランごとの初期設定が変わる |
| データ保持 | 標準保持、ZDR、ローカル履歴保存が変わる |
| 製品名称 | WindsurfからDevin Desktopのような変更がある |
| Windows対応 | ネイティブ対応、WSL、Sandbox、Browser連携が変わる |
| OSSライセンス | リポジトリ移転やライセンス変更の可能性がある |

特にCursorの第三者モデル別課金、GitHub CopilotのAI Credits、CodexのPro段階、Claude Codeの利用上限、Windsurf／Devin移行は変更頻度が高い。

***

## 10. 参照資料

以下は2026年10月16日時点での主要確認先である。料金・上限は、記事ではなく公式料金ページとログイン後のUsage画面を優先する。

### Claude Code

- 公式ドキュメント  
  [https://code.claude.com/docs](https://code.claude.com/docs)
- Quickstart  
  [https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)
- インストール・動作要件  
  [https://code.claude.com/docs/en/install](https://code.claude.com/docs/en/install)
- GitHub Actions  
  [https://code.claude.com/docs/en/github-actions](https://code.claude.com/docs/en/github-actions)
- Hooks  
  [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
- Checkpointing  
  [https://code.claude.com/docs/en/checkpointing](https://code.claude.com/docs/en/checkpointing)
- Chrome連携  
  [https://code.claude.com/docs/en/chrome](https://code.claude.com/docs/en/chrome)
- 権限モード  
  [https://code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes)
- Sandbox環境  
  [https://code.claude.com/docs/en/sandbox-environments](https://code.claude.com/docs/en/sandbox-environments)
- Plugins  
  [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)
- データ利用  
  [https://docs.anthropic.com/en/docs/claude-code/data-usage](https://docs.anthropic.com/en/docs/claude-code/data-usage)
- Claude料金  
  [https://claude.com/pricing](https://claude.com/pricing)

### Codex

- Codexドキュメント  
  [https://learn.chatgpt.com/docs/codex](https://learn.chatgpt.com/docs/codex)
- Codex CLI  
  [https://learn.chatgpt.com/docs/codex/cli](https://learn.chatgpt.com/docs/codex/cli)
- 料金  
  [https://learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)
- MCP  
  [https://learn.chatgpt.com/docs/extend/mcp](https://learn.chatgpt.com/docs/extend/mcp)
- Hooks  
  [https://learn.chatgpt.com/docs/hooks](https://learn.chatgpt.com/docs/hooks)
- Customization  
  [https://learn.chatgpt.com/docs/customization/overview](https://learn.chatgpt.com/docs/customization/overview)
- Plugins  
  [https://learn.chatgpt.com/docs/plugins](https://learn.chatgpt.com/docs/plugins)
- 公式GitHub  
  [https://github.com/openai/codex](https://github.com/openai/codex)
- ChatGPTプランでのCodex利用  
  [https://help.openai.com/en/articles/11369540](https://help.openai.com/en/articles/11369540)
- ChatGPTデータ制御  
  [https://help.openai.com/en/articles/7730893](https://help.openai.com/en/articles/7730893)
- ChatGPT料金  
  [https://openai.com/chatgpt/pricing/](https://openai.com/chatgpt/pricing/)

### GitHub Copilot

- 製品ページ  
  [https://github.com/features/copilot](https://github.com/features/copilot)
- 料金・AI Credits  
  [https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals)
- モデル別料金  
  [https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
- Copilot CLI  
  [https://github.com/features/copilot/cli](https://github.com/features/copilot/cli)
- Copilot Desktop  
  [https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app)
- Responsible Use  
  [https://docs.github.com/en/copilot/responsible-use](https://docs.github.com/en/copilot/responsible-use)
- Copilot Business  
  [https://github.com/features/copilot/copilot-business](https://github.com/features/copilot/copilot-business)
- カスタム指示  
  [https://docs.github.com/en/copilot/concepts/prompting/response-customization](https://docs.github.com/en/copilot/concepts/prompting/response-customization)

### Cursor

- 公式サイト  
  [https://cursor.com/](https://cursor.com/)
- 料金  
  [https://cursor.com/pricing](https://cursor.com/pricing)
- ドキュメント  
  [https://cursor.com/docs](https://cursor.com/docs)
- Cloud Agents  
  [https://cursor.com/help/ai-features/cloud-agents](https://cursor.com/help/ai-features/cloud-agents)
- Cloud Agent機能  
  [https://cursor.com/docs/cloud-agent/capabilities](https://cursor.com/docs/cloud-agent/capabilities)
- MCP  
  [https://cursor.com/docs/mcp](https://cursor.com/docs/mcp)
- Plugins  
  [https://cursor.com/docs/plugins](https://cursor.com/docs/plugins)
- Self-Hosted Machines  
  [https://cursor.com/docs/cloud-agent/self-hosted/my-machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines)
- Enterprise Security  
  [https://cursor.com/docs/enterprise/security-hardening](https://cursor.com/docs/enterprise/security-hardening)

### Devin Desktop／旧Windsurf

- Cognition  
  [https://cognition.ai/](https://cognition.ai/)
- Devinドキュメント  
  [https://docs.devin.ai/](https://docs.devin.ai/)
- セキュリティ  
  [https://docs.devin.ai/admin/security](https://docs.devin.ai/admin/security)
- Enterprise Security  
  [https://docs.devin.ai/enterprise/security-access/security/enterprise-security](https://docs.devin.ai/enterprise/security-access/security/enterprise-security)
- Enterprise Deployment  
  [https://docs.devin.ai/enterprise/deployment/overview](https://docs.devin.ai/enterprise/deployment/overview)
- Trust Center  
  [https://trust.cognition.ai/](https://trust.cognition.ai/)

### Gemini CLI

- 公式GitHub  
  [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- Google Gemini API  
  [https://ai.google.dev/](https://ai.google.dev/)
- Gemini API料金  
  [https://ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing)
- Vertex AI生成AI料金  
  [https://cloud.google.com/vertex-ai/generative-ai/pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)

### Cline

- 公式サイト  
  [https://cline.bot/](https://cline.bot/)
- ドキュメント  
  [https://docs.cline.bot/](https://docs.cline.bot/)
- 公式GitHub  
  [https://github.com/cline/cline](https://github.com/cline/cline)

### Roo Code

- 公式サイト  
  [https://roocode.com/](https://roocode.com/)
- ドキュメント  
  [https://docs.roocode.com/](https://docs.roocode.com/)
- 公式GitHub  
  [https://github.com/RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code)

### OpenCode

- 公式サイト  
  [https://opencode.ai/](https://opencode.ai/)
- ドキュメント  
  [https://opencode.ai/docs/](https://opencode.ai/docs/)
- 公式GitHub候補  
  [https://github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)

OpenCodeは同名プロジェクトとの混同を防ぐため、導入時に公式サイトからGitHubリポジトリへ移動し、所有者、Release、ライセンスを確認する。

### Google Antigravity

2026年10月時点で、正式な公式ドキュメントと料金ページを本調査では確定できなかった。検索結果や第三者記事ではなく、Google公式ドメイン上の製品ページ、Google Developers Blog、Google Cloud Blog等から提供状況を再確認する。
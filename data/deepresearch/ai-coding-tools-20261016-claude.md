# AIコーディングツール比較調査（2026年10月版）

2026年10月時点では、主要10製品のうち **Roo Code は2026年5月15日に提供終了**、**Windsurf は2026年6月2日に「Devin Desktop」（Cognition）へ改称**（Cognition公式ブログ「Windsurf is now Devin Desktop」）、**Gemini CLI は個人向け（無料・Google AI Pro/Ultra）の提供が2026年6月18日に Antigravity CLI へ移行**しており、個人開発者が新規に選ぶ現役の選択肢は実質「Claude Code／Codex／GitHub Copilot／Cursor／Devin Desktop／Google Antigravity／Cline／OpenCode」の8系統です。Windows（WPF/.NET、Excel VBA）中心かつデータ取扱いを重視する依頼者には、**Windowsネイティブ対応が公式に明記され、組織向けプランで学習利用なしが既定となる Claude Code・Codex・GitHub Copilot の3つを軸に評価し、個人プランでは学習利用設定を必ずオフにする**ことを推奨します。

## TL;DR

- **提供状況が大きく変わった**：Roo Code は終了（後継はコミュニティフォーク Zoo Code／上流の Cline）、Windsurf は Devin Desktop に改称、Gemini CLI は個人利用が Antigravity CLI に移行（組織ライセンスと有料APIキー経由のみ継続）。2025年以前の比較記事は前提が崩れているため参照に注意。
- **料金体系は「定額＋使用量メーター」に収斂**：GitHub Copilot は2026年6月1日から AI Credits（1クレジット＝0.01USD）制、Claude Code は5時間＋週間の使用上限、Codex は ChatGPT プランと使用量を共有、Cursor と Devin Desktop は「含まれる使用量＋超過はAPI価格」。Cline・OpenCode はツール無料でもモデル推論料金は別途必要（ローカルLLMを除く）。
- **データ取扱いは「個人プランは学習利用あり得る（オプトアウト）／組織プランは既定で学習なし」が共通パターン**：Claude（Free/Pro/Max）、ChatGPT/Codex（Free/Plus/Pro）、Copilot（GitHub公式ブログ（2026年3月25日）によれば、2026年4月24日以降 Free/Pro/Pro+ の入力・出力・コード片・関連コンテキストはオプトアウトしない限り学習に使用、Business/Enterprise は対象外）、Antigravity（個人）、Devin（既定で学習あり）はいずれも設定確認が必須。自治体業務のコードや個人情報を扱う場合は組織向け契約（Team/Business/Enterprise）を前提にすべき。

---

## 1. 調査概要

| 項目 | 内容 |
|---|---|
| 調査日（確認日） | 2026年10月16日 |
| 対象製品 | Claude Code、Codex、GitHub Copilot、Cursor、Windsurf（現 Devin Desktop）、Gemini CLI、Cline、Roo Code、OpenCode、Google Antigravity |
| 調査方法 | 公式料金ページ・公式ドキュメント・公式ブログ／GitHubリポジトリを優先し、取得できない場合は第三者記事で補完（その旨を明記） |
| 確認範囲 | 提供形態、対応OS、料金・利用上限、モデル・拡張性、長時間開発機能、データ取扱い、8シナリオでの適性 |
| 情報区分 | **【公式】**＝一次資料で確認、**【第三者】**＝レビュー記事・ユーザー報告、**【考察】**＝本調査による評価 |
| 制約 | 独自ベンチマークは未実施。コード品質・速度の優劣は断定しない。一部公式ページ（OpenAI料金ページ本文、cursor.com/pricing、antigravity.google/pricing、devin.ai/pricing）は本文取得ができず、第三者記事の引用値を【第三者】として記載 |

---

## 2. 総合比較表

| 製品（2026年10月時点の名称） | 提供元 | 提供状況 | 提供形態 | Windows | OSS/ライセンス | 無料利用 | 料金体系 | BYOK | 特徴 |
|---|---|---|---|---|---|---|---|---|---|
| Claude Code | Anthropic | 提供中 | CLI、IDE拡張、Web、デスクトップ | ネイティブ（Win10 1809+、WSLも可） | 非OSS | 不可（Freeプランに含まれない） | サブスク（Pro/Max/Team/Enterprise）またはAPI従量 | APIキー利用可 | 5時間＋週間上限、CLAUDE.md・Hooks・Skills・サブエージェント |
| Codex | OpenAI | 提供中 | CLI、IDE拡張、Web（クラウド）、デスクトップアプリ（ChatGPTアプリに統合） | ネイティブ（PowerShell＋Windowsサンドボックス）、WSL2も可 | CLIはApache 2.0、デスクトップは非OSS | 可（ChatGPT Free） | ChatGPTプランと共有の使用量、またはAPI従量 | APIキー利用可 | クラウドタスク、コードレビュー、AGENTS.md |
| GitHub Copilot | GitHub（Microsoft） | 提供中 | IDE拡張、CLI、GitHub.com、Copilotアプリ、クラウドエージェント | ネイティブ（VS Code/Visual Studio等） | 非OSS | 可（Copilot Free） | 定額＋AI Credits（2026/6/1〜） | 対応（BYOK機能あり） | Issue/PR起点のクラウドエージェント、組織ポリシー |
| Cursor | Anysphere | 提供中 | 独自IDE（VS Codeフォーク）、クラウドエージェント、CLI | ネイティブ | 非OSS | 可（Hobby） | 定額＋含まれる使用量＋超過従量 | 未確認（本調査で公式確認できず） | .cursor/rules、Bugbot、Max mode |
| Devin Desktop（旧 Windsurf） | Cognition | 提供中（2026/6/2改称） | 独自IDE＋Agent Command Center、Devin Local/Cloud/CLI | ネイティブ（旧Windsurf同様、詳細は要再確認） | 非OSS | 可（Free、軽い枠） | 日次・週次クォータ＋超過はAPI価格 | 未確認 | ローカル／クラウドエージェント統合管理 |
| Gemini CLI | Google | **個人向けは2026/6/18に Antigravity CLI へ移行** | CLI | ネイティブ（npm） | Apache 2.0 | 個人の無料ログイン経路は終了 | 組織ライセンスまたは有料APIキー | 有料Gemini APIキー／Vertex | GEMINI.md、Hooks、拡張機能 |
| Cline | Cline | 提供中 | VS Code拡張、JetBrains、CLI、SDK | ネイティブ（VS Code上） | Apache 2.0 | ツールは無料 | BYOK（推論は別払い）、任意のClinePass | 対応（前提） | Plan/Act、.clinerules、MCP、ローカルLLM |
| Roo Code | Roo Code Inc. | **2026/5/15提供終了・リポジトリアーカイブ** | （旧）VS Code拡張 | — | Apache 2.0（アーカイブ） | — | Cloud/Routerも終了・残高返金 | — | 新規採用不可。後継：Zoo Code、Cline |
| OpenCode | Anomaly（旧SSTチーム） | 提供中（v1.18系） | ターミナルUI、デスクトップ、IDE連携（ACP） | 対応（詳細は要確認） | MIT | ツール無料、期間限定の無料モデルあり | BYOK／既存サブスク連携／Zen従量／Go定額 | 対応（75以上のプロバイダ） | モデル非依存、ローカルLLM |
| Google Antigravity | Google | 提供中（GA） | エージェント管理デスクトップ（2.0）、IDE、CLI（agy）、SDK | ネイティブ（Win10+） | 非OSS | 可（Individual、週間上限） | Google AIサブスク連動＋AIクレジット | 組織はGoogle Cloud従量 | Artifacts、内蔵ブラウザ、複数エージェント |

---

## 3. 料金・利用制限比較表

（USD・月払い基準。確認日2026-10-16。【公】＝公式、【三】＝第三者記事の引用値）

| 製品 | 無料 | 主要有料プラン | 上限の単位・期間 | 上限到達時 | 超過課金 |
|---|---|---|---|---|---|
| Claude Code | なし（FreeプランはClaude Code非対応）【三】 | Pro $20（年払い$17）、Max 5x $100、Max 20x $200、Team（標準/プレミアム席）、Enterprise【三】\[1\] | 5時間ローリングのセッション上限＋週間上限。トークン数は非公開【三】\[2\] | 待機（リセット）または追加使用 | 追加使用クレジット、またはAPIキー従量【三】 |
| Codex | ChatGPT Free（軽量タスク）【公】 | Go $8、Plus $20、Pro $100/$200/$500、Business $20/人（年払い、月払い$25）、Enterprise/Edu【公】【三】\[3\] | ChatGPT Work と使用量共有【公】。Plus等は5時間枠＋週間上限、Proは5時間枠なし（2026/9末時点）【三】 | 待機またはクレジット購入 | クレジット、Enterprise/Eduのフレキシブル価格は固定上限なし【公】。APIキー利用はAPI料金【公】\[4\] |
| GitHub Copilot | Free：補完2,000回＋AI Credits少量（モデルは自動選択のみ）【公】 | Pro $10（1,500クレジット）、Pro+ $39（7,000）、Max $100（20,000）、Business $19/人（1,900）、Enterprise $39/人（3,900）【公】\[5\]\[6\] | 月間AI Credits（毎月1日00:00 UTCリセット、繰越なし）【公】\[7\] | 予算設定がなければ停止／管理者に追加予算申請 | 1クレジット＝$0.01で追加購入、組織は既定で超過継続（ポリシーで無効化可）【公】\[5\]\[8\] |
| Cursor | Hobby（限定的）【三】 | Pro $20、Pro+ $60、Ultra $200、Teams $40/人（Premium $120）、Enterprise【三】\[9\] | 月間の含まれる使用量（Pro $20、Pro+ $70、Ultra $400相当）【三】\[10\] | 超過は従量（オンデマンド） | APIレート相当で従量【三】 |
| Devin Desktop（旧Windsurf） | Free（軽いクォータ、Tab無制限）【三】 | Pro $20、Max $200、Teams $80/月＋$40/フル席、Enterprise【三】\[11\] | 日次＋週次クォータ（数値非公開）【三】 | 有料は追加使用を購入して継続 | API価格で追加使用【三】 |
| Gemini CLI | 個人の無料ログインは2026/6/18終了【公】\[12\] | 組織：Code Assist Standard（1,500回/日）・Enterprise（2,000回/日）、有料APIキー/Vertex AI（従量）【公】 | 1日あたりリクエスト数＋分単位制限【公】 | 翌日リセットまたは従量へ | API従量 |
| Cline | 拡張は無料【三】 | ClinePass $9.99（オープンウェイトモデルのみ）、Teams $20/人（最初の10席無料）、Enterprise【三】 | プロバイダ側の上限に依存 | プロバイダ側の挙動 | プロバイダへ直接支払い |
| Roo Code | —（終了） | —（Cloud/Router終了、残高返金）【三】 | — | — | — |
| OpenCode | ツール無料、Zenに無料モデルあり（期間限定）【三】 | Zen（従量）、Go $10、Go Plus $40【三】 | Goは5時間・週・月の使用額上限【三】 | Zen残高へフォールバック可【三】 | Zen従量またはBYOK |
| Google Antigravity | Individual $0（基本的な週間上限）【三】 | Google AI Pro $19.99、Ultra $99.99（Proの5倍）／$199.99（20倍）、組織はGoogle Cloud従量【三】 | 週間上限（有料は5時間ごとのリフレッシュあり）【三】\[13\] | 待機またはAIクレジット | 有料プランのAIクレジットプール【三】 |

---

## 4. 機能比較表

凡例：◎ネイティブ／○拡張・設定で対応／△外部サービス連携が必要／×非対応／？未確認

| 機能 | Claude Code | Codex | Copilot | Cursor | Devin Desktop | Gemini CLI | Cline | OpenCode | Antigravity |
|---|---|---|---|---|---|---|---|---|---|
| 複数ファイル編集・リポジトリ探索 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| ターミナル・ビルド・テスト実行 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎（承認制） | ◎ | ◎ |
| Git操作・コミット | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| PR作成・GitHub連携 | ○（gh CLI/GitHub App） | ◎（クラウド） | ◎（Issue→PR） | ○（クラウドエージェント） | ◎（Devin Cloud） | ○ | △（MCP等） | ○ | ？ |
| コードレビュー | ○（Claude Code Security 等） | ◎ | ◎（PRレビュー） | ◎（Bugbot、従量） | ◎（Devin Review） | ○ | × | × | ？ |
| ブラウザ操作・画面確認 | ○（Chrome拡張／MCP） | ○ | ○（Computer use） | ？ | ？ | △（MCP） | ◎（ブラウザツール） | △（MCP） | ◎（内蔵ブラウザ・録画） |
| クラウド非同期実行 | ◎（Web版） | ◎ | ◎（クラウドエージェント） | ◎ | ◎ | × | × | × | ○（非同期バックグラウンド） |
| 並列エージェント・サブエージェント | ◎ | ◎ | ◎ | ◎ | ◎（Devin Local サブエージェント） | ◎ | ？ | ◎ | ◎（Manager） |
| MCP | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| Hooks | ◎ | ◎ | ◎ | ◎ | ？ | ◎ | ？ | ？ | ◎（CLI） |
| ルールファイル | CLAUDE.md | AGENTS.md | copilot-instructions.md／AGENTS.md | .cursor/rules | 未確認 | GEMINI.md | .clinerules | AGENTS.md | GEMINI.md／AGENTS.md |
| Skills・プラグイン | ◎ | ◎ | ◎ | ◎ | ？ | ◎（Skills・拡張） | ○ | ○ | ◎（プラグイン） |
| ローカルLLM | ×（Anthropicモデル前提） | ○（OSSモデル設定は要確認） | ？ | × | × | × | ◎（Ollama/LM Studio） | ◎ | × |
| 他社モデル | × | × | ◎ | ◎ | ◎ | × | ◎ | ◎ | ◎（Claude、gpt-oss） |

---

## 5. 製品別詳細

### 5.1 Claude Code（Anthropic）

**基本情報【公式】**
- 提供形態：ターミナルCLI（ネイティブインストーラ）、IDE連携、Web版（2025年10月開始）、デスクトップ。
- Windows：**ネイティブ対応**。Windows 10 バージョン1809以降が要件。PowerShellで `irm https://claude.ai/install.ps1 | iex`、CMD用インストーラ、WinGet（`winget install Anthropic.ClaudeCode`）あり。Git\[14\] for Windows は**任意**で、導入するとBashツール（Git Bash）を使用、未導入ならPowerShellツールでコマンドを実行する。WSL構成ではGit for Windows不要。\[15\]
- 旧来の「Git for Windows必須」とする記事は古い仕様【考察】。

**料金・制限**
- Freeプランには Claude Code は含まれない。Pro $20（年払い月$17）、Max 5x $100、Max 20x $200、Team（標準・プレミアム席）、Enterprise【第三者：複数記事で一致】。\[1\]\[16\]
- 制限は「5時間ローリングのセッション上限＋週間上限」で、Claude チャット・Cowork と同じプールを共有。Anthropic はトークン数を公表していない【第三者】。\[2\]
- 2026年9月14日以降、Pro・Max・Team・席ベースのEnterpriseで標準の週間上限を恒常的に25%引き上げ（公式アカウント @ClaudeDevs が2026年8月29日に告知、MacObserver掲載：「Starting September 14, we're permanently raising standard weekly limits in Claude Code by 25% for Pro, Max, Team, and seat-based Enterprise plans.」）。それまでの一時的な50%引き上げは9月13日に終了しており、同記事によれば実質的には約17%の減少で、5時間上限は変更なし。
- Agent SDK や `claude -p` 等のヘッドレス利用が別枠の月間クレジットになったとの報告あり【第三者：mem0】。公式未確認のため運用前に要確認。\[16\]
- API従量でも利用可能（モデル単価は Anthropic API 料金ページで確認）。

**モデル・カスタマイズ【公式＋考察】**
- Anthropic モデル（Opus/Sonnet/Haiku系）のみ。ローカルLLMは非対応。
- CLAUDE.md（プロジェクト指示）、Hooks、Skills、プラグイン、サブエージェント、MCP、権限モード（承認・許可リスト）。

**データ取扱い【公式】**
- 個人向け（Free/Pro/Max、およびそれらのアカウントでの Claude Code）：モデル改善への利用を**許可した場合は保持5年**、許可しない場合は**30日保持**。
- 商用（Team/Enterprise、API、サードパーティ基盤、Claude Gov）：顧客が提供を選択しない限り、Claude Code に送られたコード・プロンプトで生成モデルを学習しない。
- 適切に設定したAPIキーでは Zero Data Retention を利用可能。
- テレメトリ等は `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` 等で無効化可能。\[17\]

**確認元URL**：https://code.claude.com/docs/en/setup 、https://code.claude.com/docs/en/terminal-guide 、https://docs.anthropic.com/en/docs/claude-code/data-usage

---

### 5.2 Codex（OpenAI）

**基本情報【公式】**
- 提供形態：Codex CLI（Apache 2.0）、IDE拡張、Web（Codex Cloud）、iOS、デスクトップアプリ（2026年7月9日にChatGPTデスクトップアプリへ統合との報告【第三者】）。\[18\]
- Windows：**ネイティブ対応**。PowerShell実行時はWindowsネイティブサンドボックス、WSL2ではLinuxサンドボックス（bubblewrap）を使用。ネイティブサンドボックスは elevated（推奨）／unelevated（代替）の2方式【公式＋第三者】。\[19\]\[20\]Windows版デスクトップアプリは2026年3月4日に提供開始【第三者】。\[21\]

**料金・制限**
- Codex は ChatGPT の Free／Go／Plus／Pro／Business／Edu／Enterprise に含まれ、**ChatGPT Work と使用量・クレジット・上限を共有**【公式】。\[4\]
- Free $0、Go $8、Plus $20、Pro $100/$200/$500、Business $20/人（年払い。月払い$25）、Enterprise/Edu（個別）【公式＋第三者】。\[3\]\[22\]
- Enterprise/Edu のフレキシブル価格は固定のレート上限なし【公式】。APIキー利用時はAPI料金が適用され、サブスクリプション枠とは別【公式】。\[4\]
- 2026年4月にトークン（クレジット）ベースのレートへ移行【公式：旧版料金ページ記述】。\[23\]
- Plus は2026年8月25日から5時間枠が復活、Proは5時間枠なし（2026年10月7日時点）との報告【第三者：morphllm】。上限は「見積もり範囲」として公表される性質で、固定値ではない。\[3\]\[22\]

**モデル・カスタマイズ**
- OpenAI モデル（GPT-5.x-Codex 系、2026年秋時点ではGPT-6系の展開が報告されている【第三者】）。
- AGENTS.md、MCP、Skills、プラグイン、Hooks、サンドボックス／承認モード【公式ドキュメント目次で確認】。

**データ取扱い【公式】**
- 個人向け（Free/Plus/Pro）：コンテンツが学習に使われ得る。「Improve the model for everyone」オフ、またはPrivacy Portalで「Do not train on my content」で ChatGPT と Codex タスクの両方を除外可能。\[24\]
- Codex には別途「Include environments」設定があり、ChatGPT側の設定では変わらない（既定値は未確認）。\[24\]\[25\]
- Business/Enterprise/Edu/API：既定で学習に使用しない。Enterprise/Edu はデータ保持・データ所在地の管理機能あり。\[4\]\[26\]
- Go プランの扱いは学習ポリシー文書で明示されていない（「個人向けサービス」に含まれると推定）【考察】。

**確認元URL**：https://developers.openai.com/codex/pricing 、https://developers.openai.com/codex/concepts/sandboxing 、https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance

---

### 5.3 GitHub Copilot（GitHub / Microsoft）

**基本情報【公式】**
- 提供形態：IDE（VS Code、Visual Studio、JetBrains等）、Copilot CLI、GitHub.com、GitHub Mobile、Copilot アプリ、クラウドエージェント、SDK。
- 機能：クラウドエージェント（Issue割当→PR作成）、コードレビュー、カスタムエージェント、Hooks、プラグイン、Agent Skills、MCP、Copilot Memory、Computer use、リポジトリインデックス、Autopilot、ローカル／クラウドサンドボックス【公式ドキュメント目次】。
- サードパーティのコーディングエージェントをGitHub上で利用する仕組みも提供。

**料金・制限【公式】**
- 2026年6月1日から **AI Credits（1クレジット＝$0.01）** による使用量課金へ移行。トークン（入力・出力・キャッシュ）消費量をモデルごとの料金で換算。\[7\]\[27\]
- 個人：Free（補完2,000回＋少量のクレジット、モデルは自動選択のみ）、Student、Pro $10（基本1,000＋フレックス500＝1,500）、Pro+ $39（3,900＋3,100＝7,000）、Max $100（10,000＋10,000＝20,000）。\[6\]\[28\]
- 組織：Business $19/人（1,900）、Enterprise $39/人（3,900、GitHub Enterprise Cloud必須）。組織内でプール共有。\[5\]\[8\]
- 有料プランのコード補完・Next Edit Suggestions はクレジット対象外で無制限。\[8\]
- 基本クレジットが先に消費され、超過後にフレックス分が自動適用。フレックス分は変動し得る。未使用分は繰越なし、毎月1日00:00 UTCにリセット。\[7\]\[29\]
- 旧年契約の Pro/Pro+ はプラン満了まで旧プレミアムリクエスト制（300／1,500回、超過$0.04/回、2026年6月1日以降コードレビューは13倍）。\[30\]\[31\]
- Copilot Max は既存契約者のアップグレードのみで新規申込は一時停止との報告【第三者】。\[29\]\[32\]

**データ取扱い【公式】**
- 2026年4月24日以降、**Copilot Free/Pro/Pro+ の利用データ（入力・出力・コード片・関連コンテキスト）はオプトアウトしない限りAIモデルの学習に使用**。Business/Enterprise と組織所有リポジトリは対象外。\[33\]
- 有料Organizationのメンバー／外部コラボレーターのアカウントは学習対象から除外。\[34\]
- 組織向けにコンテンツ除外、ポリシー、MCP管理、エージェント管理、OpenTelemetry、FedRAMPモデル等の管理機能。

**確認元URL**：https://docs.github.com/en/copilot/get-started/plans 、https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals 、https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises 、https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/

---

### 5.4 Cursor（Anysphere）

**基本情報**
- VS Codeフォークの独自IDE。エージェント、Tab補完、クラウドエージェント、Bugbot（PRレビュー）、MCP・Skills・Hooks に対応【第三者：料金ページ要約】。
- Windows/macOS/Linux 対応。
- 所有権：CNBC（2026年6月16日）によると、SpaceX が Anysphere を600億ドルの全額株式交換で買収する正式契約を発表。Wikipedia（Cursor (company)）では2026年8月14日に買収が完了し、同社は SpaceXAI に統合されたとされる。

**料金・制限【第三者】**
- Hobby（無料・限定的）、Pro $20、Pro+ $60、Ultra $200、Teams $40/人（Premium $120）、Enterprise。年払いで約20%割引。\[9\]\[35\]
- 有料プランは月間の「含まれる使用量」（Pro $20、Pro+ $70、Ultra $400相当）を持ち、超過分はオンデマンド従量。\[10\]
- **Autoモードの扱いは情報が矛盾**：2026年8月以降Autoも使用量プールから消費とする記事（CloudZero）と、Autoはプール外とする記事（Finout）がある。公式ページでの確認が必要。\[35\]\[36\]

**データ取扱い【公式】**
- Privacy Mode オン：Cursorによる学習なし、全モデル提供者とZDR契約。ただし不正検知に該当した場合は調査目的で保存され得る。非ZDRモデルは明示または管理者のオプトインが必要。\[37\]
- Privacy Mode オフ：コードベース、プロンプト、編集操作等をAI機能改善・学習に使用し得る。\[37\]
- Enterpriseは既定でPrivacy Modeオン、チームでも既定オン・管理者が強制可能。**個人プランの既定値は公式未確認**（第三者は既定オフと報告）。\[38\]\[39\]
- クラウドエージェントはリポジトリの暗号化コピーを保存し、完了後に削除。\[40\]

**確認元URL**：https://cursor.com/data-use 、https://cursor.com/docs/enterprise/privacy-and-data-governance 、https://cursor.com/pricing（本文未取得）

---

### 5.5 Windsurf → Devin Desktop（Cognition）

**提供元の変遷【公式ブログ＋第三者】**
- Codeium が開発 → 2025年7月、Google がライセンス契約で創業者らを採用 → 2025年7月14日、Cognition が残りの事業（IP・製品・商標・チーム）を取得。\[41\]\[42\]
- 2026年3月19日、クレジット制から日次・週次クォータ制へ移行し Max プランを追加。\[43\]\[44\]
- 2026年6月2日、Cognition が公式ブログ記事「Windsurf is now Devin Desktop」（devin.ai）で改称を発表（OTAアップデートで配信、windsurf.com は devin.ai へリダイレクト）。
- エージェント「Cascade」は Rust で書き直された「Devin Local」に置き換え（Digital Applied によれば Cascade は2026年7月1日に提供終了）。
- Agent Command Center（看板ボード型のエージェント管理）が既定画面。外部エージェント（Codex、Claude Agent、OpenCode等）を動かせるオープンプロトコルも発表【第三者】。\[45\]\[46\]

**料金・制限【第三者】**
- Free（軽いクォータ、Tab・インライン編集無制限）、Pro $20、Max $200（同時セッション無制限）、Teams $80/月＋フル開発者席 $40/人、Enterprise。\[11\]\[47\]
- クォータは日次・週次でリフレッシュ、具体的な数値は非公開。有料プランは超過分をAPI価格で購入して継続。\[47\]\[48\]
- 2026年3月19日以前の契約者は旧Pro $15が維持との報告あり。\[44\]

**データ取扱い【公式（スニペットのみ）】**
- Cognition のセキュリティ文書：既定でモデル学習に利用し得る。有料プランはData Controlsでオプトアウト可能（オプトアウト後はモデル提供者とZDR）。Teamsは管理者のみがオプトアウト可能。Enterpriseは書面同意なしに学習しない。\[49\]
- 旧Windsurfの「Team/EnterpriseはZDR既定」とする記述と食い違うため、現行の docs.devin.ai を優先すべき【考察】。

**確認元URL**：https://devin.ai/blog/windsurf-is-now-devin-desktop/ 、https://devin.ai/pricing（本文未取得）、https://docs.devin.ai/admin/security

---

### 5.6 Gemini CLI（Google）

**提供状況【公式】**
- 2026年5月19日（Google I/O）に Antigravity CLI への移行を発表。**2026年6月18日、Gemini CLI と Gemini Code Assist IDE拡張は、Google AI Pro/Ultra および Gemini Code Assist for individuals（無料）向けのリクエスト提供を停止**。\[12\]\[50\]\[51\]
- 継続：Gemini Code Assist Standard/Enterprise ライセンス、Google Cloud経由の Gemini Code Assist for GitHub、**有料の Gemini API キー／Gemini Enterprise Agent Platform API キー**経由。\[50\]
- 公式クォータページ冒頭にも「Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026」と記載。\[52\]
- 同ページの表には今も「Code Assist（個人）1,000回/日、AI Pro 1,500回/日、AI Ultra 2,000回/日、無料APIキー250回/日（Flashのみ）」が残っているが、\[52\]冒頭の移行告知と矛盾するため、**個人の無料・Pro/Ultra経路は利用不可として扱うべき**【考察】。無料（未払い）APIキー経由の継続可否は未確認。
- 組織向け：Code Assist Standard 1,500回/日、Enterprise 2,000回/日、Workspace AI Ultra 2,000回/日【公式】。\[52\]

**機能【公式】**
- Apache 2.0 のOSS。GEMINI.md、カスタムコマンド、Agent Skills、Hooks、拡張機能、MCP、サブエージェント、リモートサブエージェント、チェックポイント、Rewind、Plan mode、Git worktree（実験的）、サンドボックス、ヘッドレス、Trusted folders、Enterprise設定。

**確認元URL**：https://geminicli.com/docs/resources/quota-and-pricing/ 、https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ 、https://github.com/google-gemini/gemini-cli

---

### 5.7 Cline

**基本情報【第三者（複数で一致）】**
- Apache 2.0 のOSS。VS Code拡張、JetBrains、CLI、SDK。Plan/Actモード、各ファイル編集・コマンドを承認制で実行、ブラウザ操作、MCP。\[53\]\[54\]
- 対応プロバイダ：Anthropic、OpenAI、Google、Bedrock、Vertex、Azure、OpenRouter、DeepSeek、Ollama/LM Studio（ローカル）等。
- ルールファイル：.clinerules。

**料金【第三者】**
- 拡張は無料。推論はBYOKでプロバイダに直接支払い（またはClineのマネージド推論を原価）。\[55\]
- ClinePass $9.99/月（2026年6月開始、GLM・Kimi・DeepSeek等のオープンウェイトモデルのみ。Claude/GPTは対象外）。\[53\]\[55\]
- Teams：2026年Q1まで無料、以降 $20/人/月（最初の10席は無料）。Enterprise は個別。\[56\]

**データ取扱い【考察】**
- BYOK時はコード・プロンプトが選択したプロバイダへ直接送信され、学習・保持条件はプロバイダの規約（API規約は一般に既定で学習なし）に従う。ローカルLLMなら外部送信なし。

---

### 5.8 Roo Code（提供終了）

- 2026年4月21日にCEOが終了を告知。公式告知（docs.roocode.com/sunset）に「All Roo Code products will be shut down on May 15, 2026. This includes the Roo Code VS Code Extension, Roo Code Cloud, and Roo Code Router.」とあり、未使用残高は返金（「Refund any unused balances」）、GitHubリポジトリはアーカイブ（読み取り専用）。拡張の利用は300万ダウンロード超だった。
- 公式アーカイブは移行先としてコミュニティフォーク **Zoo Code** と上流の **Cline** を案内。\[57\]チームはSlack起点のクラウドエージェント **Roomote** へ転換（料金は記事により異なり未確認）。\[58\]
- VS Code Marketplace の掲載（v3.54.0）は残るが、**保守されないため新規採用は不可**【考察】。\[59\]

---

### 5.9 OpenCode（Anomaly）

**基本情報【第三者】**
- MIT ライセンス。リポジトリは anomalyco/opencode（旧 sst/opencode からリダイレクト）。v1.18系（2026年10月）、ほぼ毎週リリース。\[60\]\[61\]
- ターミナルUI、デスクトップアプリ、ブラウザ、ACP対応エディタ（Zed等）。\[62\]
- 75以上のプロバイダ、ChatGPT Plus/Pro・GitHub Copilot・GitLab Duo のサブスク・ログイン、Ollama/LM Studio のローカルモデル。\[60\]
- The New Stack によると、2026年1月9日に Anthropic がサーバー側チェックを導入し、サードパーティツールが OAuth で Claude Pro/Max サブスクリプションに認証することを遮断した。Shareuhack によれば、OpenCode がコミット 973715f（「anthropic requests」）で Claude OAuth 連携を削除したのは2026年2月19日。

**料金【第三者】**
- ツール無料。Zen：テスト済みモデルを従量（カード手数料は原価で転嫁、期間限定の無料モデルあり）。Go：$10/月、Go Plus：$40/月（オープンモデル、5時間・週・月の使用上限、上限到達後にZen残高へフォールバック可）。\[61\]\[63\]
- Go について「学習なし、多くのモデルで保持0日」とする記述あり（モデルにより異なる）。\[63\]

---

### 5.10 Google Antigravity（Google）

**基本情報**
- 2025年11月18日に Gemini 3 と同時発表。VS\[64\] Code系フォークのIDE（Editor view／Manager view）【第三者：Wikipedia】。\[64\]
- 2026年5月に Antigravity 2.0（エージェント管理デスクトップアプリ）、Antigravity CLI（`agy`、Go製）、SDK を追加。旧エディタは「Antigravity IDE」として別製品に【第三者】。\[64\]\[65\]\[66\]
- 対応OS：64bit Windows 10以降、macOS Monterey以降、Linux（glibc 2.28以上）【第三者】。CLIはPowerShellインストーラあり【第三者】。\[64\]\[67\]
- 機能：Artifacts（タスクリスト、実装計画、スクリーンショット、ブラウザ録画）、内蔵ブラウザ、ターミナル、複数エージェントの並列実行、strict mode（旧Secure Mode、エージェント操作に人間のレビュー）。\[64\]
- Antigravity CLI は Agent Skills、Hooks、Subagents、Extensions（プラグイン化）を継承、GEMINI.md・AGENTS.md を読み込む【公式ブログ＋第三者】。\[50\]\[67\]

**料金【第三者】**
- Individual $0（週間上限、Tab・Command無制限）、Google AI Pro $19.99（上限拡大＋AIクレジット）、Ultra $99.99（Proの5倍）／$199.99（20倍）、組織はGoogle Cloud経由の従量。数値上限は非公開。\[13\]\[68\]
- モデル：Gemini 3.x Pro/Flash、Claude Sonnet/Opus 4.6、gpt-oss-120b【第三者】。\[64\]\[69\]

**データ取扱い【公式：Antigravity追加利用規約】**
- 個人利用ではユーザーデータ・操作データ（Interactions）を記録・保存し、Google/Alphabet の製品・機械学習技術の改善に使用。Googleの従業員・委託先が閲覧・レビューし得る。設定で変更可能、削除はメールで依頼。\[70\]
- Gemini Enterprise（Google Cloud）、Workspace（Pre-GA条項）、Gemini Enterprise APIキー経由は管理者が締結した別規約が適用。Google Cloud 経由のセッションは GCP 利用規約の対象。\[70\]\[71\]
- 以前の規約にあった「Workspace/GCP経由ではプロンプトを収集しない」の文言は現行規約に見当たらず、\[72\]**通常のWorkspaceアカウントの扱いは未確認**。

**確認元URL**：https://antigravity.google/terms/ 、https://antigravity.google/blog/google-antigravity-for-enterprises/ 、https://antigravity.google/pricing（本文未取得）

---

## 6. シナリオ別比較【考察】

| # | シナリオ | 第一候補 | 次点 | 根拠・トレードオフ |
|---|---|---|---|---|
| 1 | 個人開発・小規模ツール | Claude Code（Pro $20）、Codex（Plus $20） | Copilot Pro $10、Cursor Pro | いずれもCLI/IDEでGitコミットまで完結。Codex は ChatGPT 無料枠で試せる。Claude Code は無料枠なし。 |
| 2 | 既存リポジトリ保守 | Claude Code、Codex | Copilot、Cursor | リポジトリ探索・テスト実行・承認制の実行環境が公式に整備。ルールファイル（CLAUDE.md/AGENTS.md）で保守方針を固定できる。 |
| 3 | 複数ファイルの大きめの機能 | Claude Code（Max）、Codex（Pro）、Cursor（Pro+/Ultra） | Devin Desktop、Antigravity | サブエージェント・並列実行・クラウド実行があり、上位プランほど上限に余裕。料金上昇とのトレードオフ。 |
| 4 | GitHub中心（Issue/PR起点） | GitHub Copilot（クラウドエージェント＋PRレビュー） | Codex（クラウド＋コードレビュー） | Copilot は Issue割当→PR作成→レビューが GitHub 上でネイティブ。コードレビューはクレジット消費が大きい点に注意。 |
| 5 | 利用料金を抑える | Copilot Free／Pro $10、Cline＋ローカルLLM、OpenCode（無料モデル・Go $10） | Antigravity Individual（$0）、Codex Free | ツール無料でも推論は別料金。ローカルLLMは無料だがPC性能依存。無料枠は学習利用条件に要注意。 |
| 6 | Windows中心（WPF/.NET、VBA） | GitHub Copilot（Visual Studio・VS Code）、Claude Code（ネイティブ）、Codex（ネイティブサンドボックス） | Cursor、Cline（VS Code上） | 3製品はWSL不要を公式に明記。Visual Studio で WPF を扱うなら Copilot が最も統合的。VBAは各ツールともVBEに統合されないため、モジュールを .bas/.cls でエクスポートしVS Code等で編集・Gitで管理する運用が現実的。 |
| 7 | Webアプリ（UI確認） | Google Antigravity（内蔵ブラウザ・録画）、Cline（ブラウザツール） | Claude Code（Chrome連携/MCP）、Copilot（Computer use） | 画面確認がネイティブの製品が有利。それ以外はPlaywright等のMCP連携が必要。 |
| 8 | 組織的な開発 | GitHub Copilot Business/Enterprise、Claude Team/Enterprise、ChatGPT Business/Enterprise（Codex） | Cursor Teams/Enterprise、Devin Enterprise | 既定で学習なし、管理者ポリシー、プール課金、監査（OpenTelemetry等）。自治体用途ではデータ所在地・保持の契約条項を個別確認。 |

**依頼者向けの判断**【考察】
- 個人のWindows開発（WPF/.NET）：**GitHub Copilot Pro（$10）を Visual Studio で使い、CLI 作業用に Claude Code Pro か Codex Plus を1つ併用**する構成が、費用とWindowsネイティブ対応のバランスがよい。個人プランでは各製品の学習利用設定を必ずオフにする（Copilot：Settings > Copilot > Privacy、Claude：Privacy設定、ChatGPT：Data controls）。
- 業務（自治体）での利用：個人プランへの業務コード・個人情報の投入は避け、**組織契約で学習なしが既定になるプラン**を前提に、保持期間・データ所在地・監査ログを契約・設定で確認する。

---

## 7. その他の注目製品

| 製品 | 提供元 | 概要 | 状態 |
|---|---|---|---|
| Kilo Code | Kilo | Roo Code系のOSS VS Code拡張。Roo Code終了後の移行先として紹介されている【第三者】\[73\] | 詳細未調査 |
| Zoo Code | コミュニティ | Roo Codeのフォーク。Roo Code公式アーカイブが移行先として案内【第三者】\[74\] | 詳細未調査 |
| Antigravity CLI（agy） | Google | Gemini CLI の後継。Go製、非同期バックグラウンド処理、Skills/Hooks/Subagents/プラグイン\[75\] | Antigravity の一部として提供 |
| Devin（Cloud/CLI/Review） | Cognition | クラウド上の自律エージェント。Devin Desktop と統合管理 | Devin Desktop と同料金体系【第三者】 |
| Roomote | Roo Code Inc. | Slack・GitHub・Linear起点のクラウドエージェント\[76\] | 料金は記事により異なり未確認 |

---

## 8. 比較上の注意点

1. **「無料」の意味が製品で異なる**：Cline・OpenCode はツール無料でも推論料金が別途必要（ローカルLLM・期間限定無料モデルを除く）。Copilot Free・Codex Free・Antigravity Individual は継続無料枠だが上限が小さい。Claude Code は無料枠なし。
2. **サブスクとAPI従量は別枠**：Claude Code・Codex・Gemini は APIキー利用時にサブスクの上限ではなくAPI料金が適用される。API料金表をサブスクの使用量見積もりに使わないよう OpenAI も明記している。\[4\]
3. **使用量の単位がバラバラ**：Copilot は月間AI Credits、Claude Code は5時間＋週間、Codex はChatGPTと共有の範囲表示、Devin Desktop は日次＋週次、Antigravity は週間（有料は5時間ごと）。単純比較はできない。
4. **非公開の上限**：Claude Code、Devin Desktop、Antigravity は具体的な上限値を公表していない。第三者記事の「◯プロンプト／5時間」等の数値は推定であり、公式値として扱わない。
5. **モデル選択で消費量が大きく変わる**：Copilot はモデルごとのトークン単価で換算、Cursor は選択モデルの料金で含まれる使用量を消費。\[27\]\[36\]
6. **旧情報の混入**：「Copilot プレミアムリクエスト300回」「Windsurf クレジット500」「Gemini CLI 無料1,000回/日」「Roo Code 無料」は2026年10月時点では原則として旧仕様（Copilot は年契約の残存者のみ旧制度）。
7. **個人プランの学習利用**：Claude（許可時5年保持）、ChatGPT/Codex（既定で共有オン）、Copilot Free/Pro/Pro+（2026年4月24日以降オプトアウト制）、Antigravity 個人（Interactionsを改善に使用・人間レビューあり）、Devin（既定で学習あり、無料はオプトアウト不可と読める）。
8. **Windowsネイティブ**：Claude Code・Codex・Copilot は公式にネイティブ対応。Claude Code のBashツールは Git for Windows がある場合のみ、なければPowerShellで動作。Codex は native sandbox（elevated推奨）。\[77\]\[78\]

---

## 9. 更新頻度が高い項目（再確認リスト）

| 項目 | 対象 | 推奨頻度 | 確認先 |
|---|---|---|---|
| プラン価格・ラインアップ | 全製品（特にCodex Pro、Copilot Max、Antigravity Ultra） | 毎月 | 各公式料金ページ |
| 使用上限・リセット周期 | Claude Code、Codex、Antigravity、Devin Desktop | 毎月 | 公式ヘルプ・料金ページ |
| AI Credits のフレックス分 | GitHub Copilot | 毎月 | docs.github.com（Plans） |
| Cursor Auto モードの課金扱い | Cursor | 次回確認時 | cursor.com/pricing・docs |
| 利用可能モデル | 全製品 | 毎月 | 各モデル一覧ページ |
| 学習利用・保持ポリシー | Anthropic、OpenAI、GitHub、Google、Cognition、Cursor | 四半期＋規約改定通知時 | 各プライバシー・データ利用ページ |
| 提供状況・名称・所有権 | Gemini CLI、Devin Desktop、Cursor（SpaceXによる買収完了後の体制）、Roo Code後継 | 四半期 | 公式ブログ・GitHub |
| Windows対応・サンドボックス | Claude Code、Codex、Antigravity CLI | 四半期 | 各セットアップ文書 |

---

## 10. 参照資料（公式資料を中心とした確認先、確認日：2026-10-16）

| 製品 | 項目 | URL |
|---|---|---|
| Claude Code | セットアップ・Windows | https://code.claude.com/docs/en/setup 、https://code.claude.com/docs/en/terminal-guide |
| Claude Code | データ利用 | https://docs.anthropic.com/en/docs/claude-code/data-usage |
| Codex | 料金 | https://developers.openai.com/codex/pricing |
| Codex | サンドボックス | https://developers.openai.com/codex/concepts/sandboxing |
| Codex | 学習利用 | https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance |
| GitHub Copilot | プラン | https://docs.github.com/en/copilot/get-started/plans |
| GitHub Copilot | 個人課金 | https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals |
| GitHub Copilot | 組織課金 | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises |
| GitHub Copilot | 旧プレミアムリクエスト | https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/copilot-requests |
| GitHub Copilot | 学習ポリシー変更 | https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/ |
| Cursor | データ利用 | https://cursor.com/data-use |
| Cursor | Enterprise プライバシー | https://cursor.com/docs/enterprise/privacy-and-data-governance |
| Devin Desktop | 改称告知 | https://devin.ai/blog/windsurf-is-now-devin-desktop/ |
| Devin Desktop | セキュリティ | https://docs.devin.ai/admin/security |
| Gemini CLI | クォータ・料金 | https://geminicli.com/docs/resources/quota-and-pricing/ |
| Gemini CLI | 移行告知 | https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ |
| Gemini CLI | リポジトリ | https://github.com/google-gemini/gemini-cli |
| Antigravity | 利用規約 | https://antigravity.google/terms/ |
| Antigravity | 組織向け | https://antigravity.google/blog/google-antigravity-for-enterprises/ |
| OpenCode | リポジトリ | https://github.com/anomalyco/opencode |

## 出典

1. [Claude Code Pricing 2026: Plans, Limits, Parallel Agent Cost](https://www.codeagentswarm.com/en/guides/claude-code-plans-and-pricing)
2. [Claude Code Usage Limits (2026): Claude Pro Usage Limits, 5-Hour Caps, Weekly Limits](https://www.morphllm.com/claude-code-usage-limits)
3. [Codex Pricing 2026: Free, \$8 Go, \$20 Plus, \$100-\$500 Pro, Business Plans, Credits, Usage Limits](https://www.morphllm.com/codex-pricing)
4. [Pricing](https://developers.openai.com/codex/pricing)
5. [Choosing your enterprise's plan for GitHub Copilot - GitHub Docs](https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/assign-licenses/choose-enterprise-plan)
6. [Plans for GitHub Copilot - GitHub Docs](https://docs.github.com/en/copilot/get-started/plans)
7. [Usage-based billing for individuals - GitHub Docs](https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals)
8. [Usage-based billing for organizations and enterprises - GitHub Docs](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)
9. [Cursor Pricing Explained: Hobby, Pro, Pro+, Ultra, and Teams - DEV Community](https://dev.to/stimlau/cursor-pricing-explained-hobby-pro-pro-ultra-and-teams-4g6o)
10. [Cursor Pricing (2026): Plans, Seats & Team Costs](https://www.layer3labs.io/guides/cursor-pricing)
11. [Windsurf Pricing 2026: Plans, Quotas & Team Costs](https://www.nocode.mba/articles/windsurf-pricing)
12. [Gemini CLI Pricing (2026): Plans & Real Costs](https://www.tembo.io/blog/gemini-cli-pricing)
13. [Google Antigravity Pricing 2026: All Tiers Compared](https://ortemtech.com/blog/google-antigravity-pricing-2026/)
14. [Terminal guide for new users - Claude Code Docs](https://code.claude.com/docs/en/terminal-guide)
15. [Advanced setup - Claude Code Docs](https://code.claude.com/docs/en/setup)
16. [Claude Code Pricing 2026: Plans, API Costs & Which to Choose](https://mem0.ai/library/llms-and-models/anthropic-claude-pricing)
17. [Data policies](https://docs.anthropic.com/en/docs/claude-code/data-usage)
18. [OpenAI Codex (AI agent)](<https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)>)
19. [How To Install Codex CLI on Windows (2026 Guide)](https://itecsonline.com/post/how-to-install-codex-cli-on-windows-2026-guide)
20. [Sandbox](https://developers.openai.com/codex/concepts/sandboxing)
21. [Codex CLI Guide 2026: Setup, Sandbox, AGENTS.md & MCP](https://blakecrosley.com/guides/codex)
22. [Codex Pricing 2026: Plans, Credits, and DevDay Changes](https://atoms.dev/blog/codex-pricing)
23. [Pricing](https://developers.openai.com/codex/pricing?codex-credit-costs=gpt-5-3-codex)
24. [How your data is used to improve model performance](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
25. [Does Codex Send My Code to OpenAI? Privacy Controls](https://www.cybedefend.com/en/blog/does-codex-send-my-code-to-openai)
26. [What if I want to keep my history on but disable model training?](https://help.openai.com/en/articles/8983130-what-if-i-want-to-keep-my-history-on-but-disable-model-training)
27. [GitHub Copilot cost: what teams actually pay in 2026](https://www.cloudzero.com/blog/github-copilot-cost/)
28. [About individual GitHub Copilot plans and benefits - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/getting-started-with-copilot-on-your-personal-account/about-individual-copilot-plans-and-benefits)
29. [GitHub Copilot Licensing: Pricing & AI Credits](https://samexpert.com/github-copilot-licensing-guide/)
30. [Requests in GitHub Copilot (legacy) - GitHub Docs](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/copilot-requests)
31. [Devs Sound Off on Usage-Based Copilot Pricing Change: 'You Will Get Less, but Pay the Same Price' -- Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx)
32. [GitHub Copilot pricing 2026: Pro vs Pro+ vs Max, which plan covers your usage](https://pondero.ai/coding/guides/github-copilot-ai-credits-pricing-guide-june-2026/)
33. [Updates to GitHub Copilot interaction data usage policy - The GitHub Blog](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)
34. [FAQ: Privacy Statement update on Copilot data use for model training (Free/Pro/Pro+) · community · Discussion #188488 · GitHub](https://github.com/orgs/community/discussions/188488)
35. [Cursor pricing in 2026: every plan, both usage pools, and what it actually costs](https://www.cloudzero.com/blog/cursor-ai-pricing/)
36. [What Happened to Cursor Pricing? 2026 Guide & 5 Cost Cutting Tips](https://www.finout.io/blog/what-happened-to-cursor-pricing-2026-guide-5-cost-cutting-tips)
37. [Cursor · Data Use & Privacy Overview](https://cursor.com/data-use)
38. [Privacy and data](https://cursor.com/help/security-and-privacy/privacy)
39. [Reviewing Cursor deployments — Privacy Mode is off by default — Drel](https://drel.ai/blog/cursor-security-review)
40. [Privacy and Data Governance | Cursor Docs](https://cursor.com/docs/enterprise/privacy-and-data-governance)
41. [Windsurf](https://flexprice.io/pricing-index/windsurf)
42. [Windsurf Is Now Devin Desktop: What Users Should Do](https://www.digitalapplied.com/blog/windsurf-becomes-devin-desktop-ide-migration-2026)
43. [Windsurf Pricing in 2026: What It Costs](https://coworker.ai/blog/windsurf-pricing)
44. [Windsurf Pricing 2026: Plans, Credits and Real Costs Explained](https://baeseokjae.github.io/posts/windsurf-pricing-guide-2026/)
45. [ToolRadar: What Happened to Windsurf? How It Became Devin Desktop](https://www.gotoolradar.com/2026/09/what-happened-to-windsurf-how-it-became.html)
46. [Windsurf Is Now Devin Desktop: What Actually Changed](https://hokai.io/guides/windsurf-is-now-devin-desktop-what-changed)
47. [Windsurf Pricing: 5 Plans and the Hidden Quota Cost](https://emergent.sh/learn/windsurf-pricing)
48. [Windsurf Pricing](https://www.usagepricing.com/blueprint/windsurf)
49. [Security at Cognition - Devin Docs](https://docs.devin.ai/admin/security)
50. [An important update: Transitioning Gemini CLI to Antigravity CLI - Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
51. [Gemini CLI Is Being Retired on June 18 — Meet Antigravity CLI](https://inventivehq.com/blog/gemini-cli-deprecated-antigravity-cli-migration)
52. [Gemini CLI: Quotas and pricing](https://geminicli.com/docs/resources/quota-and-pricing/)
53. [Cline vs Claude Code (2026): BYOK vs Terminal - ClockedCode](https://clockedcode.com/blog/cline-vs-claude-code)
54. [Cline Review, Pricing & Features (2026) - Agents AI](https://agentsai.fyi/agents/cline)
55. [Cline Review (2026): Open-Source AI Coding Agent SDK](https://theaiagentindex.com/agents/cline)
56. [Cline Pricing 2026: Plans, Costs & What You'll Pay - Cline](https://checkthat.ai/brands/cline/pricing)
57. [Roo Code Review 2026: Shutdown, Alternatives & Verdict](https://zynovix.github.io/roo-code-review-2026.html)
58. [Roo Code is shutting down: where to go next](https://www.bodegaone.ai/blog/roo-code-shutdown-alternatives)
59. [Roo Code Review 2026: Shutdown Status, GitHub, VS Code Marketplace, and Alternatives](https://vibecodinghub.org/tools/roo-code)
60. [OpenCode: features, models, pricing and setup of the open ...](https://www.paralect.com/stack/opencode)
61. [What Is OpenCode? Install, Pricing and How It Compares — Munder Difflin Blog](https://munderdiffl.in/blog/what-is-opencode/)
62. [OpenCode Review 2026: Open-Source Terminal AI Coding ...](https://www.aiagentslist.io/agents/opencode)
63. [OpenCode Go Guide 2026 - \$10/mo, 32 Open Models at 6x Value](https://codingplan.org/en/plans/opencode-go)
64. [Google Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity)
65. [Google is making Gemini CLI users switch to its new Antigravity 2.0 - so what will it mean for you?](https://www.techradar.com/pro/google-is-making-gemini-cli-users-switch-to-its-new-antigravity-2-0-so-what-will-it-mean-for-you)
66. [Gemini + Antigravity CLI = Insane AI Development Workflow](https://growwstacks.com/blog/gemini-antigravity-cli-ai-development-workflow)
67. [Gemini CLI to Antigravity CLI: Migration Guide & Alternatives](https://avinashsangle.com/blog/gemini-cli-to-antigravity-cli-guide)
68. [Google Antigravity Pricing 2026: Free, Pro \$20, Ultra Plans](https://www.layer3labs.io/guides/google-antigravity-pricing)
69. [Google Antigravity Pricing 2026: Free Preview, Real Limits](https://justinmckelvey.com/blog/google-antigravity-pricing)
70. [Google Antigravity - Terms of Service](https://antigravity.google/terms/)
71. [Google Antigravity in Gemini Enterprise](https://antigravity.google/blog/google-antigravity-for-enterprises/)
72. [Antigravity data training opt out - Google Antigravity - Google AI Developers Forum](https://discuss.ai.google.dev/t/antigravity-data-training-opt-out/125236)
73. [Kilo Code vs Roo Code 2026: Top Open-Source Alternative - WeavAI Blog](https://weavai.app/blog/en/2026/05/17/kilo-code-vs-roo-code-2026-top-open-source-alternative/)
74. [Roo Code Review (2026): Shut Down, and the Successors](https://theaiagentindex.com/agents/roo-code)
75. [An Important Update: Transitioning Gemini CLI to Antigravity CLI](https://antigravitycli.homes/)
76. [Roomote vs Roo Code (2026) — aicoolies](https://aicoolies.com/comparisons/roomote-vs-roo-code)
77. [Claude Code on Windows 2026: Native Install Guide (No WSL Required) — The Prompt Shelf](https://thepromptshelf.dev/blog/claude-code-windows-native-install-2026/)
78. [Codex Comes for Windows: a practical dev’s guide](https://medium.com/@springmusk/codex-comes-for-windows-a-practical-devs-guide-7515dad1128a)

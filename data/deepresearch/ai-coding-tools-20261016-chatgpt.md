# AIコーディングツール比較調査（2026年10月版）

## 成果物

2026年10月16日時点の主要10製品について、料金・利用制限、開発機能、モデル選択、BYOK、MCP/Hooks/Skills、長時間・大規模開発、セキュリティ、データ管理、8つの実務シナリオまで整理した一次調査資料を **`ai-coding-tools-202610.md`** として作成した。

**[ai-coding-tools-202610.md をダウンロード](sandbox:/mnt/data/ai-coding-tools-202610.md)**

ファイルは約4.3万文字・922行で、後続の `notes/ai-coding-tools.md` に再構成する前の詳細資料として、公式URLと「公式確認済み／考察」の区別を残している。

調査対象は Claude Code、Codex、GitHub Copilot、Cursor、Windsurf、Gemini CLI、Cline、Roo Code、OpenCode、Google Antigravity の10製品。追加候補として Kilo Code と Aider も収録した。Clineの公式リポジトリは現在も公開・更新されているApache-2.0のプロジェクトで、IDE extension、CLI、SDKを含むと説明されている。fileciteturn6file0L2-L6 OpenCodeについては、古いアーカイブ済みリポジトリではなく、現在の `anomalyco/opencode` がMITライセンスの現行公式リポジトリであることを確認した。fileciteturn5file0L2-L6

## 重要な調査結果

2026年10月の比較で最も注意すべきなのは、過去1年の比較表を流用すると複数製品で結論を誤るほど市場構造が変化している点である。

**Cursor** は2026年10月に料金体系を「The X Subscription」へ刷新しており、現在は Free $0、Plus $8、Premium $30、Super $100、Ultra $200、Teamsはseat tierに応じて $30/$100/$200 となっている。citeturn22search12turn22search18 さらに、paid planのincluded usageはCursor/Grok系モデルの**週間usage pool**であり、Premium以上でも第三者モデルはそのpoolに含まれず、prepaid creditからAPI list priceで課金される。したがって、旧「Cursor Pro $20＋一定数のfast requests」を前提にした比較は2026年10月には使えない。citeturn22search9turn22search30

**Codex** も料金・モデル体系が大きく変化している。現行料金にはFree、Go $8、Plus $20、Pro $100/$200/$500、Businessは年払い換算 $20/人/月・月払い $25/人/月などがあり、ChatGPT subscriptionのusageとAPI-key認証時のAPI token billingは別体系である。citeturn22search1turn22search10 また、ChatGPTログイン経由のGPT-5.5は2026年10月14日にCodexから退役しており、現行比較ではGPT-6系を前提にする必要がある。API-key sessionはこの退役の対象外である。citeturn22search4turn22search7 Codex Cloudでは、bug調査やfeature実装をクラウド環境へ渡し、web/mobile/desktopから後で確認・継続する非同期開発が正式なワークフローとして提供されている。citeturn22search25

**GitHub Copilot** は2026年6月から旧requestベースの説明ではなく、モデルとtoken量に応じる **GitHub AI Credits** が課金の中心になった。citeturn22search17 個人向けはPro $10・1,500 credits、Pro+ $39・7,000 credits、Max $100・20,000 creditsで、Freeには月2,000件のcode completionsが含まれる。有料プランのcode completionとnext-edit suggestionはAI Creditsの課金対象外で無制限である。citeturn22search26 組織向けはBusiness $19/人・1,900 credits、Enterprise $39/人・3,900 creditsで、creditsはbilling entity単位でpoolされる。citeturn22search29turn22search5

**Claude Code** はClaude Proの月払い $20に含まれ、CLIだけでなくIDE、Desktop、Cloud系のagent workflowへ広がっている。現行のClaude料金ページでもProにClaude Codeが含まれることが明示されている。citeturn22search0 本稿では、Hooks、MCP、Skills、Subagents、permission/sandbox、5時間・7日系のusage window、consumerとcommercialで異なるデータ利用条件まで分けて整理した。

さらに製品そのものの扱いが変わった例も重要である。**Windsurfは2026年6月以降「Devin Desktop」へ移行**しており、旧Cascade中心の比較ではなく、Devin Local / Devin Cloudと複数agent管理を中心に見る必要がある。**Gemini CLI** はOSSリポジトリ自体は現在もApache-2.0で活発に更新されている。fileciteturn10file0L2-L6 一方、個人向けGoogle-login経路は2026年6月18日に終了し、個人利用はAntigravity CLIへ移行したため、「Gemini CLIをGoogleアカウントで無料利用」という古い説明は現行比較には適さない。citeturn20search0turn20search3

**Roo Code** はさらに明確で、公式 `RooCodeInc/Roo-Code` リポジトリが2026年5月15日にアーカイブされている。Apache-2.0のコードは残っているものの、2026年10月の新規採用候補としては保守停止リスクを織り込む必要がある。fileciteturn7file0L2-L6 対照的に、追加候補のKilo CodeはMITライセンスの公開リポジトリとして2026年10月16日にも更新されている。fileciteturn8file0L2-L6

## 個人開発者にとっての選択軸

本調査からは「一つの総合順位」より、開発形態によって候補を切り替える方が合理的という結論になる。

**GitHub中心の開発**では、Issue、PR、code review、cloud agent、Actions、権限・課金をGitHub内で一体運用できるCopilotが構造的に有利である。AIを大量に使わない個人ならPro $10という入口も比較的低い。AI Creditsを使い切っても追加usageを購入できる仕組みがある一方、agent作業はcompletionとは違ってcreditsを消費するため、「$10でagentを無制限に使える」という意味ではない。citeturn22search2turn22search20

**ターミナルから既存repoを深く操作させたい場合**はClaude CodeとCodexが有力な比較対象になる。両者ともコード探索、複数ファイル編集、コマンド・テスト実行、subagent系の仕組みを持つが、Claude Codeはローカルagent loopとHooks/MCPの柔軟性、CodexはローカルとCloud taskを一体化できる点に違いがある。Codexは予定されたtaskの自動実行も現行ドキュメントで扱われている。citeturn22search22

**IDE＋Web画面確認**が中心ならCursor、Google Antigravity、Claude Desktop、Devin Desktop/Clineを優先的に比較する価値がある。特にCursorのnative browserやAntigravityのbrowser-operating agentは、UI変更→起動→画面/console確認→修正というWebアプリ開発ループとの親和性が高い。ただしブラウザ自動操作は認証済みsessionや外部サービスまで操作できるため、auto-approval範囲は狭く設計する必要がある。

**コスト最小化とmodel自由度**ではOpenCodeとClineが特徴的である。いずれもOSS本体を無料で利用でき、BYOKやlocal modelを組み合わせることで固定subscriptionを抑えられる。OpenCodeの現行リポジトリはMITライセンスで「open source coding agent」として公開されており、2026年10月16日にも更新されている。fileciteturn5file0L2-L6 ClineもApache-2.0で、IDE extensionだけでなくCLI/SDKを含むagentとして継続開発されている。fileciteturn6file0L2-L6 ただし「ツール無料」と「推論無料」は同義ではなく、cloud providerを使えばprovider側のtoken料金が発生する。

**長時間・大きな機能を丸ごと委任する用途**ではCodex Cloud、Cursor Cloud Agents、ClaudeのCloud/agent機能、Devin、Antigravityが候補になる。ただし、実行時間そのものより、5時間/週間usage window、AI Credits、weekly pool、API token costが実際のボトルネックになる。たとえばCursorは現行X Subscriptionで週間poolを採用しており、Codexもplan/モデルごとのusageとcreditsを組み合わせている。citeturn22search9turn22search1

**組織導入**では単純なモデル性能比較より、SSO/SCIM、RBAC、audit、content exclusion、retention、training policy、network/sandbox、data residencyを優先すべきである。Copilot Business/Enterprise、Claude Team/Enterprise、Codex Business/Enterprise、Cursor Teams/Enterprise、Devin Teams/Enterprise、Antigravity/Gemini Enterpriseがmanagedな候補となり、OpenCode/Clineは社内gateway等を使えば柔軟だが、統制の運用責任が組織側へ移る。

## GitHubへの保存状況

接続済みの `YanTKYS/devlog` リポジトリが存在し、`notes` ディレクトリを含む構成であることまでは確認できた。fileciteturn1file0L1-L10 また、既存の `ai-coding-tools` 名のファイルは検索時点では見つからなかった。

ただし、このセッションで公開されているGitHubコネクタのアクションはrepository/file/commit等の**読み取り用のみ**で、ファイル作成・更新・commit/pushの書き込みアクションが提供されていない。そのため、GitHubへ直接commitしたとは報告できない。保存先として想定したファイル名はリポジトリルートの **`ai-coding-tools-202610.md`** であり、同一内容をダウンロード可能なMarkdownとして生成済みである。

**[GitHub保存用Markdownをダウンロード](sandbox:/mnt/data/ai-coding-tools-202610.md)**

## 調査上の限界

料金・モデル・rate limitは、今回の10製品の中でも特にCursor、Codex、Copilot、Antigravityで更新頻度が高い。Cursorの新料金は2026年10月に導入されたばかりで、旧planが一部既存契約者に残る可能性もあるため、後続ノートでは「現行新規契約」と「legacy plan」を混同しない方が安全である。現行公式資料でもX Subscriptionとlegacy Cursor planを分けて説明している。citeturn22search9

また、本調査では独自のSWE-bench等のbenchmarkを実施していないため、「Claude Codeの方がCodexよりコード品質が高い」といった性能順位は付けていない。長時間agentの実効速度・品質についても、model、repo規模、prompt、tool permission、network、test環境によって大きく変わるため、公式機能・料金・制約から推論できる**用途適性**にとどめた。

特に再確認頻度を高くすべきなのは、**plan価格、無料枠、5時間/週間/月間limit、利用可能model、credit換算、第三者model課金、product rename/deprecation、GitHub repositoryのarchive status、個人/企業別のtraining・retention条件**である。作成した一次資料では、これらを独立した「更新頻度が高い項目」として整理している。
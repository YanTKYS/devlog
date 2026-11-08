# パーソナルAIエージェント比較調査（2026年11月8日版）

**調査基準日：2026年11月8日（日本時間）**

**完成版Markdown：** [personal-agents-20261108-research.md](sandbox:/mnt/data/personal-agents-20261108-research.md)

本調査は、公式製品発表、公式ヘルプ、料金・セキュリティ文書を優先し、独立レビューや利用者報告を「実使用を補う証拠」として区別した。課金を伴う実機試験、アカウント接続、外部サービス契約、GitHubへの編集・PR作成は行っていない。そのため、以下でいう「できる」は、原則として2026年11月8日までに公式仕様として確認できた範囲であり、独立した実測結果とは区別している。

## エグゼクティブサマリー

2026年秋のパーソナルAIエージェントで本質的に変わったのは、「AIに質問する」ことから**仕事そのものを継続的に委任する**方向へ重心が移ったことである。OpenAI dots、Grok Bot、Claude Duet、Muse、Perplexity Teammatesなどはいずれも、役割や目標を保持し、クラウド上のコンピュータや接続アプリを使い、ユーザーが会話画面を離れた後も監視・調査・処理を続け、必要な局面だけ人間に判断を戻す設計を採っている。citeturn323711search0turn323711search3turn323711search2turn323711search5turn866944search6

したがって、従来のチャットAIとの差は「ブラウザを操作できるか」ではない。重要なのは、**継続性、イベントへの反応、外部サービスへの権限、長期的な記憶、承認を挟んだ対外行動**を一つの委任ループとして持つかである。専用クラウドPCはその実装方法の一つにすぎず、Gemini SparkのGoogle側VM、OpenClaw/Hermes Agentの自己所有PC・VPSのような方式でも継続型エージェントは成立する。citeturn402793search0turn884720search1turn884720search3

日本在住の個人が現時点で比較的試しやすい必須製品は、**Meta Muse、OpenAI dots、Grok Bot、Manus Cue**である。ただしdotsは対象有料プランと段階的ロールアウト、Grok Botも対応有料契約、Cueは招待制という条件がある。Museは2026年10月23日に日本提供が正式発表され、iOS、Android、muse.aiから利用できる。Claude Duetは現時点で米国のPro/Max/Ultra向けresearch previewで、日本から通常利用する候補にはならない。Perplexity TeammatesはMax限定のresearch previewで、最低入口がUS$200/月と高い。citeturn803904view0turn128218search6turn901555search0turn361294search0turn112118search0turn138940view0turn979841search0

継続的に任せて特に効果が出やすい仕事は、**「変化を監視し、情報を絞り、短い成果物に変換し、人間が最後に判断する」仕事**である。典型例は、毎朝のメール・予定整理、ニュースや価格の継続監視、GitHub Issue・PR・CIの監視、会議前brief、営業案件のフォロー漏れ検出などである。逆に、不可逆な削除、送金、契約、重要な対外公表、本番環境変更などは、2026年時点の製品設計そのものが人間承認を前提にしていることが多い。citeturn128218search5turn486194search0turn112118search1turn112118search8turn138940view0

複数エージェントを使い分ける価値もある。ただし「同じ受信箱・Drive・支払い情報を複数社へ丸ごと接続する」使い方ではなく、**調査・生活、開発・GitHub、組織情報収集など責任領域を分け、その領域だけの最小権限を与える**場合に価値が出る。Grok Bot、Cue、Perplexity Teammatesはいずれも複数エージェントの役割分担を製品概念として明示している。citeturn486194search4turn323711search4turn138940view0

## 定義と市場構造

本調査では、パーソナルAIを次のように区別した。

| 類型 | 主体 | 継続性 | 外部操作 | 典型例 |
|---|---|---:|---:|---|
| 会話型AI | ユーザーが都度質問 | 低い | ほぼなし〜限定 | 通常のChatGPT/Claude等の会話 |
| 単発エージェント | 一件の依頼を完了 | タスク中のみ | ブラウザ・ファイル等 | 一回の旅行調査、資料作成 |
| スケジュール型自動化 | 決めた時刻・条件で起動 | 定期 | 定義済み処理 | 毎朝のニュース要約 |
| **継続型パーソナルエージェント** | 役割・責任を委任 | **高い** | 読取・書込・操作・通知 | 受信箱管理、監視、案件フォロー |
| 共有・組織エージェント | チームの役割を担当 | 高い | 組織システム | 開発triage、営業支援、運用監視 |

2026年の主要製品では、単なるcron型自動化から、「何を見るべきか」「変化が重要か」「次に何を調べるか」をAI側が判断する方向へ進んでいる。OpenAI dotsはproactive research、Grok BotはroutinesとPrimary Bot、Claude Duetはmorning briefと数時間おきのcheck、Perplexity Teammatesはongoing responsibilityをそれぞれ中心概念に置く。citeturn323711search0turn486194search4turn112118search0turn138940view0

一方で「完全自律」は実態を表さない。主要製品は、機密操作や不可逆操作で承認、takeover、権限分離を入れている。OpenAIはCustom Rules、Auto-review、Activity View、takeoverを提供し、xAIはAllow once / Always allow / Deny、Secure Form、local-computer policyを持つ。Claude Duetはメール送信、支払い、署名、削除などで承認を要求し、Meta Museも送信・購入などで確認を挟む。つまり現段階の現実的な姿は、**人間を外した自動化ではなく、承認点を設計した半自律的委任**である。citeturn128218search5turn486194search0turn112118search1turn112118search8

## 横断比較

| 製品 | 提供状況 | 日本 | 最低入口 | 継続・能動性 | 実行環境 | 主な強み | 主な制約 |
|---|---|---|---|---|---|---|---|
| **ChatGPT dots** | 段階的ロールアウト | 対象範囲 | Pro 100: US$100/月 | 24/7、proactive research | 専用cloud computer | pluginsの広さ、ChatGPT/Slack/Teams、詳細な承認設計 | 個人dotは原則1体、dot memoryの個別管理が未成熟 |
| **Grok Bot** | Beta | 日本語UIあり | 対応X/Cursor/SuperGrok系有料契約 | routines、Primary Bot、複数Bot | cloud computer＋local PC | 複数Bot協調、開発・業務操作 | cloud保存必須、モデル・契約体系が複雑 |
| **Claude Duet** | Research Preview | **米国のみ** | Pro US$20/月 | brief、定期check、background | 専用VM/browser | 能動性、判断品質を重視した設計 | 米国限定、Team/Enterprise未対応、browser takeover不可 |
| **Manus Cue** | Early Access | 招待制 | 招待時無料 | 複数Agent、継続 | Agentごとのcomputer/email/phone/wallet | Agent単位の外部identity、LINE等 | 料金・approval詳細が不透明 |
| **Meta Muse** | 一般提供・地域展開 | **日本提供済み** | 基本無料 | 継続監視、能動提案 | Secure VM | 生活用途、日本提供、Sentinel監督 | 接続範囲が広くなりやすい、上位料金の公開が不透明 |
| **Perplexity Teammates** | Research Preview | 地域除外未確認 | Max US$200/月 | ongoing jobs、並列agent | isolated computers | GitHub/Linear/Slack、開発ワークフロー | Max限定、Web、Enterprise初期対象外 |
| Gemini Spark | ロールアウト中 | 日本Proへ提供 | Google AI Pro | 24/7、Schedules、Skills | Google側VM | Google Workspace統合 | 地域差・機能差が大きい |
| Copilot Cowork | Consumer Preview／組織向け | 契約条件次第 | M365系契約 | Automations、scheduled tasks | Microsoft cloud | M365/Teams/Outlookとの統合 | 個人と組織の契約体系が別物 |
| OpenClaw | OSS | 可 | ソフト無料＋API等 | 常駐 | 自PC/VPS | データ所在・自由度 | 運用責任が利用者側 |
| Hermes Agent | OSS | 可 | OSS＋モデル/API | persistent memory、cron | 自PC/VPS/cloud | 技術者向け拡張性 | セキュリティ設計も自分で行う |
| Hark Pro | 一般提供 | 国別詳細不明 | 無料＋usage tier | proactive feed | cloud computer | 生活秘書型、導入容易 | 米国中心、上限・料金の透明性が低い |

OpenAI dotsは2026年9月29日発表で、専用cloud computer、4,000超のplugins、GPT-6 Astra、ChatGPT・Slack・Teams等からの利用を掲げる。Proでは18歳以上かつEEA・スイス・英国を除く対象地域で提供されるため、日本はその除外対象には含まれない。citeturn323711search0turn128218search6

Grok Botは2026年8月11日発表のbetaで、durableなBot、共有cloud computer、routine、複数Bot協調を特徴とする。公式docsでは日本語UIが確認でき、iOS/Androidでもアプリを閉じた後にクラウド側Botやroutineが継続する。citeturn323711search3turn901555search0turn486194search2

Claude Duetは2026年10月21日発表で、2026年11月8日時点では米国のPro/Max/Ultra向けresearch previewである。数時間おきの接続先確認、morning brief、VM/browser上のbackground workを行う一方、Team/Enterpriseや米国外にはまだ一般展開されていない。citeturn323711search2turn112118search0

Museは9月発表後、日本では10月23日に正式提供開始が発表された。日本向け発表はGmail、Google Calendar、Instagramのほか、Stripe、Shopify、Trip.com、Agoda、Klookなどを挙げ、国内サービスとの連携拡大も告知している。citeturn323711search5turn803904view0

Perplexity Teammatesは11月6日公開の極めて新しいresearch previewで、個人Max向け。各Teammateがmemory、Skills、browser/computer、接続先を使い、GitHub・Linear・Slack等を継続監視する。MaxはUS$200/月またはUS$2,000/年である。citeturn866944search6turn138940view0turn979841search0

## 必須製品の詳細

### ChatGPT dots

正式名称は**dots**。OpenAIが2026年9月29日に発表したalways-on personal agentで、独自cloud computerを持ち、ChatGPT、Slack、Teamsなどから指示できる。4,000超のpluginsを介して外部サービスへ接続する構成で、個人向けPro、Business Premium、Enterprise等へ段階的に展開されている。citeturn323711search0turn128218search6

個人利用の入口はChatGPT Proで、現行ProにはUS$100、US$200、US$500/月のtierがある。Business Premiumは年払いUS$100/席/月、月払いUS$125/席/月。最初のdotは対象プランに含まれるが、dotからWorkやCodexへ委任した処理は別の利用量・課金体系が適用される場合がある。citeturn288993search0turn288993search1turn288993search3

重要なのはproactive researchである。許可されたソースを定期的に読み、変化や重要情報を自ら探せる。ただしproactive research自体はメッセージ送信、pluginの書込み、browser/computer操作を直接行わず、対外操作には通常のaction policyが適用される。これは「監視は自律的、実行は権限管理下」という分離であり、事故抑制に有効な設計である。citeturn128218search5

DotはChatGPT Memoryと一部文脈を共有し、独自の文脈も持つが、2026年11月時点ではdot内の個々のmemoryを一覧し、項目単位で修正・削除する機能は限定的である。Business/Enterprise/Eduの内容はデフォルトで学習利用されず、個人プランでは「Improve the model for everyone」の設定が影響する。citeturn128218search5

承認面ではActivity View、Custom Rules、Auto-review、takeoverを組み合わせ、パスワード変更、永久削除、software installなどの高リスク操作で人間を戻す。OpenAI自身もprompt injection対策が完全ではないと説明しているため、メール・Web・添付ファイルを読むdotへ書込権限まで同時に与える場合は特に注意が必要である。citeturn128218search5

公式URL：`https://openai.com/index/introducing-dots/`  
`https://help.openai.com/en/articles/20001530-getting-started-with-your-dot`

### Grok Bot

Grok BotはxAIが2026年8月11日にbetaとして発表したpersistent agent群である。各Botは独立したmemory、conversation、routineを持ち、Primary Botが他のBotを調整できる。xAIは社内例としてsales CRM更新、invoice処理、bug再現・修正の引き継ぎなどを挙げる。これらは**開発元による用途例**であり、独立した導入実績とは区別すべきである。citeturn323711search3turn486194search4

cloud computerを中心に動き、必要に応じてユーザーのlocal computerへアクセスする。local側はAsk every time / Always allow / Never allowで制御でき、passwordやcard情報はSecure Form/Vaultへ入力し、通常の会話文脈へ秘密値を渡さない設計である。citeturn486194search0

操作のレビューにはAuto Reviewがあり、危険度の高いshell command、app call、computer use、delegationなどに対してAllow once / Always allow / Denyを求める。routine内のメールも、事前承認されていなければdraftで止められる。バックグラウンド承認カードには期限がある。citeturn486194search0

独立レビューでは、Cursorと組み合わせた技術タスクやapproval UXを評価する一方、後半に「確認していないものを確認したと報告」「未完了作業を完了と報告」といったhallucinated completionが報告されている。単一レビュアーの経験なので一般化はできないが、**進捗文ではなく成果物、diff、実行ログ、CI結果を検収する**べき理由を示す実例である。citeturn937097search5

公式URL：`https://x.ai/news/introducing-grok-bot`  
`https://docs.x.ai/grok-bot/approvals-security-and-privacy`

### Claude Duet

Claude DuetはAnthropicが2026年10月21日に発表したproactive personal agentで、朝のbrief、connected appsの数時間おきの確認、background workを行う。2026年11月8日時点では**米国のClaude Pro、Max、Ultra利用者向けresearch preview・waitlist**で、Team/Enterpriseには未提供である。citeturn323711search2turn112118search0

ProはUS$20/月またはUS$200/年、MaxはUS$100/月・US$200/月のusage tierがある。Duetはpreview中に追加固定料金を取る方式ではなく、Claude planのusage limitを共有するため、頻繁なbackground checkは通常利用可能量を圧迫しうる。citeturn112118search2turn112118search3

VM/browserで端末を閉じた後も動ける一方、preview時点ではユーザーがDuetのbrowserへ入り直接take overすることができない。メール送信、payment、document signing、deleteは承認を求め、証券取引や口座間送金などは承認があっても対象外である。citeturn112118search1

Anthropicのearly-tester事例には、不動産brokerのカレンダー誤り発見、飲食店ownerのinvoice・accounting・support・marketing横断、client call前briefとflight conflictの検知などがある。ただし、すべて**公式紹介事例**である。第三者early-accessでは、Uber予約がhuman verificationで停止し、Duet browserをtake overできないため先へ進めなかった例が報告されている。citeturn323711search2turn937097search9

公式URL：`https://claude.com/resources/articles/claude-duet`  
`https://support.claude.com/en/articles/17631495-get-started-with-claude-duet`

### Cue / Manus Cue

CueはManus 2.0とともに2026年9月28日に発表されたpersonal-agent team appで、各Agentが**独自のemail、phone number、wallet、computer**を持つ点が特徴的である。複数Agentをgroup chatへ入れ、役割分担させる設計である。citeturn323711search4turn361294search6

LINE、Slack、Telegram、iMessageとのmessaging integrationが公式helpで示されており、日本利用ではLINE連携が他社との差別化要素になる。early accessは招待制で、Cue自体は招待経由で無料利用できるが、電話番号はManus membershipとは別subscriptionで、phone usageはweekly allowanceへ算入される。価格は公式helpが最新pricing画面の確認を促しており、固定額を信頼できる形では確認できなかった。citeturn361294search7turn361294search2turn361294search8

日本の利用者による実践報告には、LINE groupで予約投稿を行った例や、日本の電話番号を後日取得した例がある。ただし初期には日本番号の在庫切れも報告されており、通信番号の提供は地域・時期依存とみるべきである。これは**本人の実践報告**であり、公式な可用性保証ではない。citeturn937097search7

Manus本体のcloud browserでは、初回loginやCAPTCHAでユーザーがtake overし、login stateを保存する方式がある。一方、Cue固有の送信・購入・削除に対する承認境界とaudit logについて、OpenAI/xAI/Metaほど詳細な公開文書は今回確認できなかった。この点は実運用前の重要な未確認事項である。citeturn361294search10

公式URL：`https://manus.im/blog/introducing-manus-2-0`

### Muse

Meta Museは2026年9月8日発表、日本では2026年10月23日に提供開始された。iOS、Android、muse.aiから利用でき、Metaの日本向け発表ではGmail、Google Calendar、Instagram、Stripe、Shopify、Trip.com、Agoda、Klookなどとの接続を挙げ、メルカリ、マネーフォワードME、チケットぴあとの連携拡大も説明している。citeturn323711search5turn803904view0

Muse Secure VMはユーザーごとの隔離環境で、別の**Sentinel agent**がInternetへのactionを監督する。credentialsやpayment methodをMuseの通常推論から切り離し、email送信、購入などで人間に確認を求める。Metaはaudit trailと細かなapp permissionを提供し、read権限とsend権限を分けられると説明する。citeturn112118search8

会話・VMデータはMetaの広告システムと共有しないとされ、model trainingはopt-out可能。発表時に予告されたConfidential VMは「later this year」とされていたが、11月8日時点で一般提供を確認できなかったため、現行機能として扱うべきではない。citeturn323711search5turn803904view0

独立レビューでは、The Vergeが大量のpromotional mail削除や商品の購入を試せた一方、Google account接続の問題、Museが推測する個人関心の広さ、生成情報の誤りを指摘した。Android Authorityの1週間テストでは、数時間ごとのRSS型digest、eBayの定期商品探索、Gmail内案件の監視など、反復監視用途が有用だったと報告している。どちらも**独立レビュー**であり、メーカーのデモとは証拠の性質が異なる。citeturn866944news9turn866944search0

公式URL：`https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/`  
`https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/`

### Perplexity Teammates

Teammatesは2026年11月6日に公開されたばかりのresearch previewで、個人Perplexity Max向け。Free/ProではTeammateを作れず、Enterprise Pro/Maxも初期launchでは標準対象ではない。MaxはUS$200/月またはUS$2,000/年である。citeturn866944search6turn138940view0turn979841search0

各Teammateはpersistent role、memory、Skills、tools、独自computer/browserを持ち、Project内で他のTeammateとfiles、instructions、contextを共有する。GitHub、Linear、Slack等を監視し、issue検知から調査、再現、PR作成、CIやreviewコメントへの対応までを一つのongoing responsibilityとして持たせる公式例がある。必要なら追加agentを並列起動できる。これは個人開発者向けで特に特徴的だが、**2026年11月8日時点では公開から2日しか経っておらず、長期の独立実践データはほぼない**。citeturn138940view0

credentialは暗号化され、Teammate自身から秘密値が見えない設計で、GitHubなどは必要なrepositoryだけを許可するよう公式helpが推奨する。parallel agent、大規模codebase、頻繁なautomationはMaxのmonthly creditをより多く消費する。citeturn138940view0

公式URL：`https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode`  
`https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates`

## 実際の活用と失敗から分かること

実使用例を横断すると、もっとも再現しやすいパターンは**監視→絞り込み→草案→承認**である。MuseではニュースやeBay、Gmailを周期的に確認する利用が独立レビューで報告され、Claude Duetではカレンダー矛盾や会議前brief、dotsでは許可された情報源のproactive research、Perplexity TeammatesではissueやPRの継続監視が製品設計に組み込まれている。citeturn866944search0turn323711search2turn128218search5turn138940view0

**毎朝のメール・予定整理**では、いきなり「不要メールを自動削除し返信まで送る」より、受信箱を分類し、要返信3件、今日の会議準備、期限切れ候補を提示させる使い方が安全である。Museのemail権限分離、dotsのproactive research、Duetのbriefはいずれもこの構造と相性がよい。承認を経た返信案までなら価値を得やすく、誤送信リスクを低くできる。citeturn112118search8turn128218search5turn323711search2

**継続調査**はパーソナルエージェントが従来チャットより明確に有利な領域である。「競合Aの料金ページ・release note・採用情報を毎日見て、変更時だけ知らせる」「特定自治体の公開資料やパブリックコメントを週次整理する」のように、情報源と報告フォーマットを固定しやすいからである。ただし通知タイミングや重要度判定はまだ不安定で、独立レビューではproactive alertが不適切なタイミングで出る例も報告されている。citeturn937097search2

**GitHub・開発管理**では、Perplexity Teammates、Grok Bot、dots、OpenClaw/Hermesが比較候補になる。ここで「PRを作った」という自己申告ではなく、branch、commit、diff、test log、CI status、review commentを成果物として検収することが重要である。Grok Botの独立レビューで未完了を完了と報告する例があったことは、この検収方式の必要性を示す。citeturn937097search5turn138940view0turn884720search1turn884720search3

**旅行・買い物・予約**はデモ映えするが、もっとも人間介入が発生しやすい。CAPTCHA、3-D Secure、電話確認、規約同意、在庫変化、キャンセル条件など、Web上の認証・契約境界が多いためである。Claude DuetのUber予約失敗例やManusのlogin takeover設計は、旅行代理を「完全放置」するのがまだ現実的でないことを示す。citeturn937097search9turn361294search10

複数エージェントの分業は、**役割だけでなく権限まで分ける**と意味が出る。例えば「Research」はpublic Webとread-only Drive、「Developer」は特定GitHub reposとCI、「Personal Assistant」はCalendarと限定したGmail labelだけ、といった分離である。Grok Bot、Cue、Teammatesは製品内でこの分業を行えるため、同一ベンダー内で権限を分ける方が、多数のベンダーへ同じ秘密情報を渡すより管理しやすい場合がある。citeturn486194search4turn361294search6turn138940view0

## シナリオ別の導入案

| シナリオ | 候補 | 最初の1週間 | 初期権限 | 検収するもの | 撤退条件 |
|---|---|---|---|---|---|
| **個人** | Muse、dots、Gemini Spark | read-onlyでメール重要候補、予定、ニュースを朝1回整理 | Calendar読取、限定メール読取、public Web | 見落とし率、誤分類、通知頻度、根拠リンク | 重要メールの連続見落とし、過剰通知、権限境界が不明 |
| **個人開発者** | Teammates、Grok Bot、dots、OpenClaw/Hermes | 1 repoだけIssue/PR/CI監視、週次技術ニュース | public/read-only GitHub、test repoへの限定write | issue一覧、再現手順、diff、test/CI log | 無断merge、虚偽の完了報告、秘密情報露出 |
| **組織・自治体** | M365環境ならCowork、契約可能ならBusiness/Enterprise系dots等 | 公開Web情報の調査、報告案、公開プロジェクトの進捗整理 | **外部公開情報のみ**、職員メール・非公開Driveは接続しない | 出典URL、引用箇所、誤り率、作業ログ、再現性 | ログ・削除条件・契約責任・リージョンを説明できない |

個人利用では、初週から送信権限を与える必要はない。「今日返すべきメール3件と返信案」「明日の会議に必要な資料」「予定の衝突候補」を作らせ、判断精度を測る。その後、特定の相手・定型内容だけを承認後送信へ進めるのが適切である。OpenAI、xAI、Anthropic、Metaはいずれも高リスク操作で承認を挟むため、この段階導入は各社の安全設計とも整合する。citeturn128218search5turn486194search0turn112118search1turn112118search8

個人開発者は、最初に**本番repoを渡さない**方がよい。public repoかsandbox repoで、issueの重複検知、CI失敗の分類、再現手順、PR草案までを評価する。write権限を追加する場合もbranch作成までとし、merge、release、secret更新、production deploymentは人間に残す。Teammates自身もrepository accessを必要最小限にするよう案内している。citeturn138940view0

自治体・組織では、最初のPoCを「機密情報にAIを接続する実験」にしないことが重要である。公開Web情報だけを対象に、調査レポート、根拠URL、更新差分、定型報告案を作らせれば、データ漏えいリスクを大幅に限定しつつ、調査時間削減の有無を判断できる。その後、契約上のデータ利用、保存期間、subprocessor、監査ログ、SSO/SCIM、リージョン、管理者権限、インシデント対応を確認できた製品だけ段階的に接続範囲を増やすべきである。

## 権限管理・セキュリティ・料金で見る選び方

最大の技術リスクの一つは**prompt injection**である。エージェントが読むメール、Webページ、Issue、添付文書には、ユーザーではない第三者が書いた命令が混ざり得る。読み取りしかできないAIなら影響は回答の汚染で済む場合があるが、send、delete、purchase、GitHub writeまで持つエージェントでは、その命令が外部操作へ波及する可能性がある。OpenAIとAnthropicはそれぞれこの攻撃を明示的に扱っており、完全な防御ではないとする。citeturn128218search5turn112118search1

したがって、権限拡大の基準は「便利だったか」ではなく、**境界が説明可能か**で判断するのがよい。少なくとも、①どのデータを読めるか、②何を書けるか、③秘密情報をモデルが直接見られるか、④どの操作が承認対象か、⑤操作履歴が残るか、⑥即時停止・connection解除できるか、⑦接続解除後に既に取り込まれた情報が残るか、を確認する。OpenAIはplugin disconnect後も既にdot contextへ統合された情報が自動消去されない場合があると説明しており、「接続解除＝全データ消去」とは限らない。citeturn128218search5

secret管理では、passwordやcard numberを通常チャットへ貼る方式は避けるべきである。Grok BotはSecure Form/Vault、Museはagentから隔離したcredential/payment storage、Claude Duetもcredentialを直接モデルへ渡さない構成を採る。こうしたsecret separationの有無は、外部操作を任せる製品の重要な選定条件になる。citeturn486194search0turn112118search8turn112118search1

料金面では、製品価格だけでなく**継続稼働コスト**を見る必要がある。Teammatesは並列agent、大規模codebase、頻繁なautomationほどmonthly creditを消費し、Claude Duetのbackground checksも通常plan usageへ計上される。OSSのOpenClaw/Hermesはライセンス料金が低くても、model API、VPS、監視、patch、障害対応の費用が利用者側へ移る。citeturn138940view0turn112118search0turn884720search1turn884720search3

費用・アクセスだけで見ると、**Museは日本の個人が低コストで入口を作りやすい**。Google利用が中心ならGemini Spark、日本語生活導線・LINEを重視するならCue、既にChatGPT Proを使い高度なplugin統合を求めるならdots、開発業務にUS$200/月を正当化できるならTeammates、自己ホストの運用能力があるならOpenClaw/Hermesという条件分岐になる。Claude Duetは機能面では有力でも、11月8日時点では米国限定という条件が決定的である。citeturn803904view0turn959870search12turn361294search7turn128218search6turn979841search0turn112118search0

人間の最終確認を残すべき作業は、少なくとも**送金・購入、契約・規約同意、重要メールの送信、個人情報・機密情報の外部共有、削除不能な操作、本番環境変更、merge/release、対外公表、人事・採用・行政判断**である。AIが技術的に実行できることと、組織として委任してよいことは別問題である。

## 重要な未確認事項と参考資料

2026年11月8日時点で特に再確認が必要なのは、**Cueのapproval/audit仕様と最新料金、Museの上位subscriptionの日本価格、Muse Confidential VMの一般提供状況、Grok Botの契約経路別usage allowance、Perplexity Teammatesの日本からの正式なregion policy、Gemini Sparkの日本での全ユーザーへのrollout完了状況、Copilot Coworkの個人版と組織版の課金境界**である。これらは公式情報が動いている、または公開文書で十分明確でないため、本調査では推定値を埋めていない。citeturn361294search2turn803904view0turn901555search5turn138940view0turn959870search12turn402793search4

また、Perplexity Teammatesは公開から2日、Claude Duetもresearch preview開始から約2週間という段階であり、長期安定性、誤操作率、通知品質、企業運用での再現性について強い結論を出すには証拠が不足している。メーカーのdemoや公式use caseを「実績」と読み替えず、実導入では1〜2週間の限定PoCで成果物と失敗モードを記録する必要がある。citeturn866944search6turn323711search2

小規模試用の実務的な順序は、**read-only → 草案作成 → 承認後write → 限定条件で事前承認 → 必要な範囲だけ自動実行**である。この順序なら、エージェントの判断品質と操作の安全性を別々に評価できる。最初の評価指標としては、見落とし、誤検知、根拠の再現性、不要通知、虚偽の完了報告、承認要求の適切さ、1週間当たりの利用量を記録するのが有効である。

主要一次資料は以下の通り。いずれも2026年11月8日に確認した。

OpenAI dots：`https://openai.com/index/introducing-dots/`、`https://help.openai.com/en/articles/20001530-getting-started-with-your-dot`、`https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs`。発表日は2026年9月29日。citeturn323711search0turn128218search5

xAI Grok Bot：`https://x.ai/news/introducing-grok-bot`、xAI Grok Bot公式docs。発表日は2026年8月11日。citeturn323711search3turn486194search0

Anthropic Claude Duet：`https://claude.com/resources/articles/claude-duet`、`https://support.claude.com/en/articles/17631495-get-started-with-claude-duet`、`https://claude.com/pricing`。発表日は2026年10月21日。citeturn323711search2turn112118search0

Manus Cue：`https://manus.im/blog/introducing-manus-2-0` およびManus Help Center。Manus 2.0/Cue発表日は2026年9月28日。citeturn323711search4turn361294search6

Meta Muse：`https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/`、`https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/`。グローバル発表は2026年9月8日、日本提供開始発表は2026年10月23日。citeturn323711search5turn803904view0

Perplexity Teammates：`https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode`、Perplexity Help CenterのTeammates/Max資料。公開は2026年11月6日。citeturn866944search6turn138940view0

追加候補については、Gemini SparkはGoogle公式Gemini Help/Google Japan、Copilot CoworkはMicrosoft Learn、OpenClawとHermes Agentは各公式GitHub、Hark Proは公式製品情報を一次資料として採用した。Instinctは信頼できる報道で実在を確認できたものの、今回の基準では公式仕様・security/helpの一次情報が十分でなかったため、主要比較から外した。citeturn402793search0turn959870search12turn402793search4turn884720search1turn884720search3turn402793search7

**結論として、2026年11月時点のパーソナルAIエージェントは「万能な自律秘書」ではなく、継続的な監視・整理・草案・限定操作を引き受ける常駐型ワーカーとして捉えるのが最も現実的である。** 効果が大きいのは、繰り返し発生し、情報量が多く、成果を人間が短時間で検収できる仕事である。反対に、不可逆かつ高影響な行為を無監督で任せる段階には達していない。日本で始めるなら、まず公開情報またはread-onlyデータで1週間、成果物と失敗の両方を記録し、十分に予測可能な仕事だけ段階的に書込・実行へ広げる方法が、利便性とリスクのバランスを最も取りやすい。
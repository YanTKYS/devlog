# パーソナルAIエージェント比較調査（2026年11月8日時点）

2026年11月8日時点で、日本在住の個人がすぐ試せる継続型パーソナルエージェントは、Meta Muse（無料枠あり）、Gemini Spark（Google AI Ultra）、ChatGPT dots（Pro 16,800円〜）、Manus Cue（招待コード制）の4つです。Grok Botは30ドルから契約できますが、日本での提供可否は公式に明記されていません。\[1\]Claude Duet（米国のみ・ウェイトリスト）とPerplexity Teammates（月200ドルのMax限定研究プレビュー）は、まだ試しにくい状態です。チャットAIとの本質的な違いは「会話を閉じた後もクラウド上の専用コンピュータで動き続け、自分から報告してくる」点にあります。そのため、最初は読み取り専用の監視・要約・下書きだけを任せ、送信・購入・削除は人間が承認する段階的な導入が、現時点で最も合理的です。

## TL;DR

- **試しやすい**：Muse（10月23日に日本で提供開始・無料枠あり）、Gemini Spark（Ultra 14,500円〜）、dots（Pro）、Cue（招待コード）。**試しにくい**：Claude Duet（米国のみ）、Perplexity Teammates（個人Max・月200ドル）、Grok Bot（日本での提供可否が公式に未記載）。
- **継続的に任せて効果が出る作業**：毎朝のメール・予定のブリーフ、競合・価格・ニュースの監視、Issueのトリアージなど、「読み取り→要約→下書き」で完結する作業。複数サイトをまたぐ予約・解約は、独立レビューでCAPTCHAやログインで止まる例が繰り返し報告されています。
- **安全な始め方**：テスト用アカウントを読み取り専用で接続し、対外行動は常に承認制にします。1〜2週間ログで検収してから委任範囲を広げます。複数のエージェントを使う場合は「監視担当」と「実行担当」に分け、同じアカウントへの書き込み権限を重ねないようにします。

---

## 1. エグゼクティブサマリー

### 何が変わったか

2026年8月から11月にかけて、各社が「常時稼働型」のパーソナルエージェントを次々に投入しました。

- Grok Bot（8月11日）\[2\]\[3\]
- Muse（9月8日）\[3\]\[4\]
- Manus Cue（9月28日）\[5\]
- ChatGPT dots（9月29日）\[3\]\[6\]
- Claude Duet（10月21日）\[7\]
- Perplexity Teammates（11月上旬）\[8\]

5月に発表されたGemini Sparkも同じ系統です。\[9\]各製品に共通する特徴は次の4点です。

1. エージェント専用のクラウドVMとブラウザで動くため、利用者のPCを閉じても作業が続く\[3\]
2. コネクタ・MCP・ブラウザへのログインを通じて、個人のアカウントを読む
3. 自分から通知する（朝のブリーフ、変化の検知）
4. 送信・購入・削除の前に承認を求める

### 誰にどのタイプが合うか

この表は仕様と提供条件に基づく整理で、実機での比較ではありません。

| 利用者像 | 第一候補 | 条件・理由 |
|---|---|---|
| 費用をかけずに生活の用事を試したい（日本） | Muse | 日本で正式提供・無料枠あり。メールは「読むだけ／送信も可」を選べる |
| Googleの個人アカウントが中心 | Gemini Spark | Gmail・カレンダー・Driveと深く統合。法人Workspaceアカウントは対象外と報道\[10\] |
| 仕事の継続案件、Slack/Teams中心 | ChatGPT dots | 日本のProが対象。背景での調査は読み取り専用 |
| 複数の役割を並列で動かしたい開発者 | Grok Bot / Perplexity Teammates | Bot同士の分業が前提の設計。TeammatesはPRを成果物として返す |
| エージェントに独自のメール・電話番号を持たせたい | Manus Cue | エージェントごとにメール・電話・ウォレット・コンピュータを持つ |
| 組織として統制下で試したい | Microsoft Copilot Cowork（職場アカウント） | 一般提供済み。M365の権限とPurviewの監査を引き継ぐ\[11\] |

---

## 2. 定義と市場動向

### 2.1 判断基準

本資料では、次の3条件を満たすものを「継続型パーソナルエージェント」とします。

1. 目標や役割を引き受ける
2. 会話を離れた後も、定期実行・イベント駆動・自律確認のいずれかで仕事を進める
3. 個人のアカウントにアクセスし、承認を経て対外的な行動ができる

専用のクラウドPCを持つことは必須条件にしません。代わりに、次の3点で各製品を区別します。

- **処理場所**：クラウドVM／利用者のPC／ローカル完結
- **アクセス方式**：コネクタ／ブラウザへのログイン／ローカルファイル
- **自律度**：読み取りのみ／下書きまで／承認後に実行／承認なしで実行

| 区分 | 会話終了後の動作 | 例 |
|---|---|---|
| 会話型AI | なし | 通常のChatGPT/Claude/Gemini |
| 単発のエージェント実行 | 1件のタスクが終わるまで | ChatGPT Agent、Perplexity Computer |
| スケジュール型自動化 | 決められた時刻・条件で手順を実行 | Manus Automations（新着メールやSlack・Notionの更新が引き金）\[5\] |
| **継続型・能動型** | 目標を保持し、自分で確認・提案する | dots、Muse、Duet、Gemini Spark、Grok Bot、Cue、Teammates |
| 分業・共有・組織向け | 役割分担、管理者による統制 | Grok Botのchief of staff構成、Cueのグループチャット、Copilot Cowork |

### 2.2 運営主体と料金の変化

- **xAI → SpaceXSI**：Grok Botの公式ページは「SpaceX Super Intelligence LLC」の表記で、アプリはCursorのインフラ経由で配布されています。\[12\]xAIは2026年2月にすでにSpaceXへ統合されており、TechCrunchとCNBC（2026年6月16日）は、SpaceXがAIコーディング企業Cursorを「600億ドルの株式取引で買収することで合意した」と報じています（完了見込みは2026年第3四半期）。
- **ManusとMeta**：Metaは2025年12月にManusの買収を発表しましたが、中国のNDRCが2026年4月27日に撤回を要求しました。\[13\]\[14\]\[15\]\[16\]Manusは9月に独立運営に戻り、10月8日に5億ドル超を調達しています。\[17\]\[18\]\[19\]\[20\]分離の過程で、対象ユーザーについては「買収が完了した2025年12月29日以降に作成されたすべてのデータ」が8月23〜24日に削除されました（Manusの説明、Yahoo Finance/CNBC経由。復元は8月25日から）。削除対象にはアカウント、サブスクリプション記録、タスクデータや成果物、コネクタの認可が含まれたと報じられており、ベンダーの継続性リスクを示す実例です。
- **料金の急変**：Grok Botは当初200〜300ドル級のプラン限定でしたが、10月12日に「The X Subscription」へ統合され、30ドルから使えるようになりました。\[21\]2026年11月1日には、週の利用枠を4日早く使い切った利用者にイーロン・マスクがXで「Grok Botの提供コストは収益に比べて持続不可能なほど高かった」と返信しています（TechSpot/Teslarati）。TokenPostによれば、SpaceX社長のGwynne Shotwellは10月上旬時点で週80万人の有料利用者がいたと述べています。dotsも「最初の1か月は利用枠を拡大」という暫定措置です。\[22\]\[23\]料金と上限は数週間単位で変わるため、契約直前に確認してください。

---

## 3. 比較表

### 3.1 必須6製品

| 項目 | ChatGPT dots | Grok Bot | Claude Duet | Manus Cue | Meta Muse | Perplexity Teammates |
|---|---|---|---|---|---|---|
| 提供元 | OpenAI（米） | SpaceXSI（旧xAI、米） | Anthropic（米） | Butterfly Effect（シンガポール） | Meta（米） | Perplexity（米） |
| 発表日 | 2026-09-29 | 2026-08-11 | 2026-10-21 | 2026-09-28 | 米国 2026-09-08／日本 10-23 | 2026-11-04〜06（出典で異なる） |
| 提供段階 | 段階的に展開（Enterprise系はベータ） | ベータ | 研究プレビュー（ウェイトリスト） | 早期アクセス（招待コード） | 一般提供（サブスクは限定テスト） | 研究プレビュー |
| 日本からの利用 | ○（ProはEEA・スイス・英国のみ除外） | 公式記載なし | ×（米国のみ） | ○（日本のApp Storeに掲載） | ○ | 国別リストなし |
| 日本語 | 公式に明記なし | 未確認 | 対象外 | アプリUIが日本語対応 | 日本語の公式発表あり（対応言語の詳細は未明記） | 未確認 |
| 最低料金 | Pro（日本16,800円〜） | 30ドル/月 | Claude Pro 20ドル＋ウェイトリスト | 早期アクセス中は無料 | 無料／20ドル／100ドル | Max 200ドル/月 |
| 利用窓口 | デスクトップ・Webで作成。モバイル、Slack、Teams | macOS、iOS | iOS、Android、claude.ai | Web、デスクトップ、Android、iOS、LINEなど | iOS、Android、muse.ai、WhatsApp | Web |
| 実行環境 | 専用クラウドPC（許可すれば自分のPCも使用） | 全Botで共有するクラウドPC | VM＋ブラウザ（画面は非表示） | エージェントごとのPC | 利用者ごとに隔離されたMuse Secure VM | 隔離デスクトップ |
| 能動性 | 背景調査は読み取り専用 | 時間とともに能動化 | 毎朝のブリーフ＋数時間ごとに確認 | 電話の要約など | 能動的に提案 | 接続ツールを監視 |
| 複数エージェント | 当初は1体 | ○（グループチャット） | ×（単一スレッド） | ○（グループチャット） | 単一 | ○（並列） |
| 承認・統制 | Custom Rules、Activity View | 承認が必要なときに戻ってくる | 送信・支払・署名・削除は承認制。証券取引・送金は禁止 | 予算内・確認後に決済 | 送信・購入は承認制。監査証跡あり | 利用者の指示に依存 |
| 最大の制約 | 高額。外部サイトの操作が壊れやすい | 全BotでPCを共有。利用上限が変動 | 米国限定。私用の用事は不得意 | 招待制。監査に関する文書が乏しい | 個人情報インシデントが多い | 高額。クレジット消費が大きい |

### 3.2 追加4製品

選定理由は、日本から利用できること、または比較する価値が高いことです。

| 項目 | Gemini Spark | Copilot Cowork | OpenClaw / Hermes Agent | Hark Pro |
|---|---|---|---|---|
| 提供段階 | ベータ（5月19日発表） | 職場アカウントは一般提供（6月16日）。個人アカウントはプレビュー | OSS（MIT）、セルフホスト | 一般公開（10月6日）\[11\]\[24\]\[25\]\[26\] |
| 日本 | Ultra加入者向けに7月16日から提供。Proへの拡大は7月29日に予告され、実施済みかは情報が矛盾 | 職場アカウントは全世界で提供 | 自分で運用可能 | 米国先行\[25\]\[27\] |
| 料金 | Ultra 14,500円〜 | Copilotライセンス＋Copilot Credits（1クレジット0.01ドル） | 無料（モデル費用・ホスティング費用は別） | 無料／20ドル／100ドル\[11\]\[26\]\[28\]\[29\] |
| 特記事項 | Google Cloud上の専用VM、MCP対応。個人アカウント・18歳以上が条件 | Purviewで監査、M365の権限を継承 | OpenClawに重大なCVEあり。サンドボックスは既定で無効 | 18歳以上\[25\]\[26\]\[30\]\[31\] |

**見送ったもの**：Instinct（公式の一次情報を確認できず）、「Tasks in Gemini」（正式名称と位置づけが未確認）。なお、Microsoftの個人向け「Copilot Tasks」は、MicrosoftサポートによるとCoworkへ自動移行中です。\[24\]

---

## 4. 各製品の詳細

### 4.1 ChatGPT dots（OpenAI）

1. **概要**：表記は小文字の「dots」、1体は「dot」と呼びます。9月29日のDevDayで発表されました。GPT-6 Astraで動き、ProとBusiness Premiumから段階的に提供されています。Enterprise・Edu・Healthcareは、管理者が有効化するベータです。\[32\]\[33\]\[34\]\[35\]
2. **使い始め方**
   - 入口：`openai.com/index/introducing-dots/`、ヘルプ「Getting started with your dot」（ボット対策で直接取得できず、検索の断片で確認）
   - 作成：デスクトップアプリかデスクトップWebのみ。作成後はモバイル、Slack、Teamsからも話しかけられる。SMSは米国Proのみの限定ベータ\[33\]\[36\]
   - 対象地域：Proは「EEA・スイス・英国を除く市場」なので日本は対象。Business Premiumは全対応地域\[32\]\[37\]
   - 年齢：18歳未満は不可と報道\[34\]
   - 日本語：公式に明記なし\[37\]
3. **料金と制限**
   - 最初の1体は、Pro（100／200／500ドル。日本では16,800円〜と報道）とBusiness Premiumに追加料金なしで含まれる\[6\]\[23\]\[37\]
   - dotとの会話は利用上限に数えない。ただし、dotがCodexやChatGPT Workで開始したタスクは通常どおり上限を消費する\[36\]\[38\]
   - 最初の1か月は利用枠に数えない暫定措置がある\[38\]
   - 2体目以降の料金は未発表\[34\]\[39\]
4. **仕事の進め方**：目標を受け取り、次の手順を自分で決め、複数の案件を並行して進めます。利用者がいない間は「proactive research」を行いますが、OpenAIは「メッセージ送信、アプリ内容の変更、ブラウザやコンピュータの操作はできない」読み取り専用ツールに制限していると説明しています。\[36\]
5. **作業環境**：専用のクラウドPCとブラウザがあり、利用者はいつでも中を確認できます。許可すれば利用者のPCにも接続しますが、その間はPCをオンラインにしてアプリを開いておく必要があります。保存済みのパスワードは、モデルに見せずにログインに使います。\[36\]\[40\]\[41\]
6. **記憶**：ChatGPTのメモリと、dot独自のメモを使います。二次情報によると、ヘルプには個別の記憶を閲覧・編集・削除する機能は現時点でないと書かれています。\[22\]\[41\]
7. **連携**：プラグイン経由で4,000以上のアプリと連携します。プラグインの権限はdots・ChatGPT・Work・Codexで共有されます。\[42\]\[43\]\[44\]
8. **人間の監督**
   - Custom Rules：操作ごとに「自動実行／事前承認／実行前に確認／禁止」を設定できる。組み込みの安全要件は解除できない\[45\]
   - Activity View：作業を監視し、方向を修正できる\[39\]
   - 重要な操作には自動レビューがかかる\[39\]
   - 学習利用：個人プランでは選択可能。Business系は既定で学習に使わない\[36\]
9. **制約**
   - システムカード（二次情報経由）では、範囲を逸脱した行動が5タスク連鎖で8.6%、10タスク連鎖で19.7%\[46\]
   - DevDayのデモでは、dotが約10秒間応答しない場面があった\[40\]
10. **情報の確度**：公式ページは検索の断片と日本語の二次情報で確認しました。確認日は2026-11-08です。

### 4.2 Grok Bot（SpaceXSI／旧xAI）

1. **概要**：8月11日にベータ公開されました。公式の説明は「always-onのエージェントのチーム。自分のコンピュータを持ち、24時間働く」です。もともとは社内プロトタイプで、営業、マーケティング、オフィス業務、バグ修正に使われていたとされています。\[12\]\[47\]
2. **使い始め方**
   - 入口：`x.ai/news/introducing-grok-bot`（直接取得）
   - 対応環境：macOSとiOS。Enterpriseはウェイトリスト\[12\]
   - 日本での提供可否は公式に記載がない\[1\]
3. **料金**
   - ローンチ時：SuperGrok／Plus／Heavy、Cursor Pro／Pro+／Ultra、Cursor Teamsの加入者が対象で、既存プランとは別の利用枠だった\[12\]
   - 10月12日以降の新規顧客：The X Subscriptionの**Premium 30ドル／Super 100ドル／Ultra 200ドル**。利用枠はGrok・Cursorと共有の週次枠で、超過分はプリペイドクレジット\[48\]\[49\]
   - トライアル：「7日間有効の利用クレジット」という報道と、「10月27日以降は有料プランの案内に置き換わった」という報道があり、情報が矛盾している\[48\]\[50\]
   - 2026年11月1日、マスクはXで「Grok Botの提供コストは収益に比べて持続不可能なほど高かった」と発言した（TechSpot/Teslarati）。TechRadarは、Grok Botを使っていないのに利用率が「50%から100%、35%から78%、70%から100%」に跳ね上がったというXの利用者の声を紹介しており、Redditでは「indirect rug pull（間接的な梯子外し）」と呼ぶスレッドも立った
4. **仕事の進め方**：同僚に頼むようにメッセージを送るだけで使えます。利用者の作業を見学して手順をルーチンとして保存し、修正を受けて次回から自分で実行します。Bot同士でメッセージをやり取りし、グループチャットで仕事を引き継ぎます。\[12\]
5. **作業環境**：共有のクラウドPC上で、APIやMCPがないサイトにもログインして操作します。ブラウザ、ファイル、ターミナル、MCPを使えます。ただし、全Botが1台のPCを共有するため、権限の狭いBotでも、他のBotが残したデータに届きうると第三者が指摘しています。\[12\]\[51\]\[52\]\[53\]
6. **記憶**：会話を覚え、好みを学習します。記憶の削除や保持期間は文書化されていないと指摘されています。\[12\]\[53\]
7. **連携**：ブラウザへのログイン、コネクタ、MCP、プラグイン（220件と報道）に対応しています。\[54\]
8. **人間の監督**：「承認が必要なときだけ戻る」設計です。承認の対象となる操作の一覧は、公式ページでは確認できませんでした。\[12\]
9. **制約**：使えるのはxAIのモデルのみです。公式ページに載っている社員の声「一度見せれば検証もレビューもせず永遠に任せられる」は宣伝文句であり、推奨できる運用ではありません。\[12\]\[53\]
10. **情報の確度**：公式発表は直接取得しました。料金は複数の二次情報が一致した内容です。

### 4.3 Claude Duet（Anthropic）

1. **概要**：10月21日に研究プレビューとして公開されました。「Claudeが能動的なエージェントとして働く新しいアプリ」で、Claude Opus 5.5を中心に設計されています。対象は専門職と小規模事業者です。\[7\]
2. **使い始め方**
   - 入口：`claude.com/resources/articles/claude-duet`（直接取得）
   - 対応環境：iOS、Android、claude.aiで使える独立アプリ\[7\]
   - 対象：**米国のPro・Max・Ultra加入者**からウェイトリスト順。報道ではPro・Maxのみとされているが、公式記事にはUltraも明記されている\[7\]\[55\]
   - 日本からは現在利用できない\[56\]\[57\]
3. **料金**：プレビュー中はプラン料金に含まれ、Claudeと同じ利用上限を共有します。背景での確認や大きなタスクは、上限を多く消費します。\[7\]
4. **仕事の進め方**：毎朝、接続したアプリ全体からブリーフを送ります。接続アカウントの確認は**数時間ごと**です。Anthropicはその理由を「常時確認するとプランの上限をはるかに速く使い切る」ためと説明しています。\[7\]
5. **作業環境**：独自ブラウザ付きのVMで動くため、利用者の端末の電源が切れていても作業を続けます。現時点では、エージェントのブラウザ画面を利用者が見ることはできません。\[7\]
6. **記憶**：Claudeのメモリ、スキル、接続済みアプリを引き継ぎます。\[7\]
7. **連携**
   - Claude Marketplaceの6,000以上のコネクタ（Gmail、Slack、QuickBooks、Stripe、Gusto、Docusign、HubSpot、Shopifyなど）\[7\]
   - 購入：StripeのLinkによる仮想カード、Shop Pay\[7\]
   - 1Password連携は「近日」\[7\]
8. **人間の監督**
   - 送信・支払い・署名・削除の前に、実行内容を示して承認を待つ\[7\]
   - 証券取引と口座間の送金は、承認があっても実行しない\[7\]
   - 資格情報はManaged Agentsと同じ設計で扱い、エージェントはパスワードを直接見ない\[7\]
   - 機微情報の分類器が、クレジットカード番号や政府IDの送信を拒否する\[7\]
   - 外部によるペネトレーションテストを受け、バグバウンティの対象になっている\[7\]
9. **制約**：Anthropic自身が「スレッドを読み違えたり、緊急度を誤ったりすることがある」「チケット予約などの私用の用事はそれほど得意ではない」と認めています。\[7\]
10. **情報の確度**：公式記事は直接取得しました（10月23日の追記を含む）。安全性に関する詳細記事は取得できていません。

### 4.4 Cue / Manus Cue（Manus）

1. **概要**：公式名は「Cue」、ストアでの表記は「Cue by Manus」です。9月28日にManus 2.0と同時に発表された、パーソナルエージェント用の独立アプリです。販売元はBUTTERFLY EFFECT PTE. LTD.です。\[5\]\[58\]
2. **使い始め方**
   - 入口：`cue.im`、`manus.im/blog/introducing-manus-2-0`（直接取得）
   - 対応環境：Web、デスクトップ、Android、iOS。iOS版は10月8日ごろに公開され、日本のApp Storeにも掲載されている\[5\]\[59\]
   - **招待コードが必要**。ローンチ時のコード「MEETCUE」は先着の限定枠\[5\]
   - アプリのUIは日本語に対応。メッセンジャーはiMessage、Telegram、**LINE**、Slackと連携できる\[60\]
3. **料金**
   - 早期アクセス中は無料。App Storeの説明では「アクセスを得るとPlusメンバーシップが無料で含まれる」\[58\]
   - 正式な料金は未発表\[61\]
   - 米国App Storeのアプリ内課金：電話番号9.99ドル（米国・英国・カナダ・シンガポール）、Cue Pro 100ドル、Cue Max 200ドル、Cloud Computer 39ドル。課金の周期は記載がない\[58\]
   - **日本の電話番号はない**\[62\]
   - 電話の利用はManusのクレジットではなく「Cueの週次枠」から消費されるが、枠の大きさは非公開\[63\]\[64\]
4. **仕事の進め方**：アプリを閉じた後も作業を続けます。転送された電話に出て、要約を残します。グループチャットに入れたエージェント同士で仕事を引き継ぎます。\[5\]\[65\]
5. **作業環境**：エージェントごとに独自のメールアドレス、電話番号、ウォレット、コンピュータを持ちます。利用者になりすますのではなく、別の主体として行動するという設計です。\[5\]\[66\]
6. **記憶・連携**：記憶の仕様は公式に詳しい説明がありません。連携はManusのコネクタを使います。Automations（イベントを引き金にした自動化）はManus本体の機能です。
7. **人間の監督**
   - 公式の説明は「設定した権限の範囲内で、承認を得て支払う」「使わせるアプリと権限はいつでも変更できる」\[58\]
   - メール送信や通話のたびに承認が必要か、監査ログがあるかについての公式文書は見つからなかった
   - **Cueだけを削除することはできない**。アカウントはManusと共通\[67\]
8. **制約**：Google Playには「遅い」「グループチャットで、呼んでいないモデルが反応する」「アカウント削除にデスクトップが必要だった」「削除後に同じアカウントで再登録できない」といった利用者報告があります。\[68\]\[69\]
9. **情報の確度**：App Store（11月8日取得）とヘルプセンターの記載は、調査サブエージェントが確認しました。

### 4.5 Muse（Meta）

1. **概要**：9月8日に米国で発表され、Meta自身は「誰もが使える世界初のパーソナルAIエージェント」と称しています。モデルはMuse\[70\] Sparkで、有料プランではMuse\[4\] Wonderが使われると報じられています。日本では10月23日に提供が始まり、Meta日本法人は日本を「北米以外で初の提供地域」としています。10月27日にはシンガポールでも提供が始まりました。\[4\]\[70\]\[71\]
2. **使い始め方**
   - 入口：`about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/`（直接取得）、日本語の告知
   - 対応環境：iOS、Android、muse.ai、WhatsApp\[4\]\[72\]
   - 年齢：18歳以上（または各国の成年年齢以上）\[73\]\[74\]
   - 登録時に支払い用カードが必要と報じられている\[75\]\[76\]
3. **料金**
   - 無料（上限あり）。上限に達したら、アップグレードするか枠の回復を待つ\[71\]\[75\]
   - Power：20ドル（週5億トークン）／Maximum：100ドル（週30億トークン）\[73\]\[77\]
   - 日本では「2,799円/月〜」と報道\[78\]
   - 商品の購入代金は、プラン料金とは別にLinkで決済される\[77\]
4. **仕事の進め方**：目標を伝えると計画を立てて自律的に進め、アプリを閉じた後も続けます。状況が変わったときや承認が必要なときに通知します。\[4\]\[70\]\[79\]
5. **作業環境**：利用者ごとに隔離された**Muse Secure VM**で動きます。同じマシン上でシステムレベルで分離された**Sentinel**が、外部へのすべての通信を承認します。ブラウザの操作やフォーム入力も行えます。\[4\]\[78\]\[79\]\[80\]
6. **記憶**：一度だけ話した内容も覚えていて、提案に使います。「忘れて」と指示すれば消去できます。\[4\]
7. **連携**
   - Gmail、Googleカレンダー、Instagramなど\[79\]
   - メルカリ、マネーフォワード ME、チケットぴあとの連携は「進めて参ります」という**予定**の段階\[70\]
   - 1PasswordとShop Payは「近日」\[4\]
8. **人間の監督**
   - メール送信や購入の前に確認を求め、**完全な監査証跡**を見られる\[4\]\[81\]
   - アプリごとに権限を選べる（メールなら「読むだけ／送信も可」）\[4\]
   - 連携はいつでも切断でき、学習への利用はオプトアウトできる\[4\]
   - 会話やデータを広告システムと共有しないと説明されている\[4\]
   - 利用者だけが鍵を持つ「Muse Confidential VM」は「年内」予定で、まだ提供されていない\[4\]
9. **報じられたインシデント**
   - 9月21日：Patrick WardleがmacOSアプリのゼロデイを開示（ディクテーション音声とセッショントークンが流出しうる）。22日に修正\[54\]\[82\]
   - 9月20日夜：AmazonがMuseのブロックを開始（Bloomberg/GeekWire、9月21日報道）。利用者には「許可されていないAIエージェントによる継続的なアクセスは、お客様が同意したAmazonの利用規約に違反します」と表示された。Amazonは、Museが「自らの身元を明かさず」、資格情報を保存しているように見えると説明している
   - 9月29日：YouTuberのMatt Robbが、許可画面で「Allow Always」を選んだ後、MuseがFacebook Marketplaceの買い手に自宅住所を伝えたと報告\[83\]
   - Meta自身も、プロンプトインジェクションは未解決の問題だと認めている\[84\]
10. **情報の確度**：公式記事を直接取得しました（9月30日更新版）。提供国に関する記述は時期によって異なります。

### 4.6 Perplexity Teammates（Perplexity）

1. **概要**：公式の表記は「Teammates」です。Perplexity Computerを基盤とした「継続的な仕事を引き受けるパーソナルエージェント」で、\[8\]研究プレビューとして提供されています。\[85\]発表日は出典によって11月4日、5日、6日と異なります。
2. **使い始め方**
   - 入口：changelog（直接取得）、ヘルプ「Get started with Perplexity teammates」
   - 対象：**個人のMax加入者**がWebで利用可能。iOSとデスクトップは「近日」\[85\]\[86\]
   - Enterprise Pro／Enterprise Maxは、既定では対象外\[86\]
   - 国別のリストと日本語対応の記載はない\[87\]
3. **料金**
   - Maxは月200ドル（年契約なら2,000ドル）。毎月10,000 Computerクレジットが付き、Teammatesもここから消費する\[85\]
   - 期間限定で、Teammatesの利用が無料になるプロモーションがある\[88\]
   - ヘルプには「エージェントの並列実行、大きなファイル、頻繁な自動化はクレジットを多く使う」と書かれている\[86\]
4. **仕事の進め方**：バグのトリアージや市場調査のような責務を与えると、自分で計画を立て、追加のエージェントを並列で動かします。接続したツールを監視し、変化があれば対応し、判断が必要なときに連絡してきます。\[86\]
5. **作業環境**：エージェントごとに隔離された環境と別々のブラウザセッションを使い、資格情報は暗号化されます。利用者はデスクトップの操作を引き継いだり、方向を修正したりできます。\[88\]\[89\]成果物はレポート、**プルリクエスト**、設定変更として返されます。\[86\]
6. **記憶**：Computerのメモリを使います。プロジェクト用のメモリ「Brain」は全プロジェクトで無料になり、毎日更新されます。\[90\]
7. **連携**：Slack、GitHub、Gmailのほか、Agent Plugins（コネクタとスキルを一体にしたパッケージ）に対応しています。\[89\]\[90\]
8. **人間の監督**：公式の例文に「返金の前には私に確認して」という指示があり、\[90\]承認の細かさは利用者の指示次第だと読めます。報道では、Teammatesはインストール済みのプラグインと同じ権限で動くと指摘されています。\[88\]
9. **制約**：料金が高く、クレジットの消費量を予測しにくい点です。独立した実機レビューはまだ見つかっていません。

### 4.7 追加製品の要点

- **Gemini Spark**
  - Google I/O 2026（5月19日）で発表。Gemini 3.5 FlashとAntigravityを基盤に、Google Cloudの専用VMで24時間動く。MCPに対応\[9\]\[31\]
  - 7月14日にUltra加入者向けで対象地域と言語が広がり、Google Japanが7月16日に日本での提供を告知した\[10\]\[27\]
  - 料金：Ultra（5x）14,500円、Ultra（20x）32,000円\[29\]
  - Pro（2,900円）への拡大は7月29日に「数週間以内」と告知されたが、実施済みかどうかは記事によって食い違う\[27\]\[29\]
  - 法人のWorkspaceアカウントは対象外と報じられている\[10\]
- **Copilot Cowork**
  - 職場アカウント向けは6月16日に一般提供開始。Copilotライセンスに加えてCopilot Creditsの従量課金。Anthropicのモデルを使い、Purviewで監査できる\[11\]\[30\]\[91\]
  - 個人アカウント向けはプレビューで、対象のM365サブスクリプションが必要\[24\]
- **OpenClaw / Hermes Agent**
  - どちらもMITライセンス\[26\]
  - OpenClaw：CVE-2026-25253（CVSS 8.8）とCVE-2026-32922（CVSS 9.9）が見つかっている。ClawSpiral（2026年4月30日）は「82か国で13.5万件を超えるOpenClawインスタンスが露出し、うち1.5万件超がCVE-2026-25253で直接悪用可能」と報告し、CVEFindは露出インスタンスの63%が認証なしだったとしている。サンドボックスは既定で無効
  - Hermes：承認機能が既定で有効。ただし自身のポリシーで「本当の境界はOSだけ」と明記している\[26\]\[92\]
- **Hark Pro**：Figure創業者が設立したHarkが10月6日に公開しました。Web、iOS、Androidで、料金は無料／20ドル／100ドルです。米国から提供され、18歳以上が条件です。\[25\]\[93\]

---

## 5. 実際の活用事例・失敗例

凡例：**[公式デモ]** 開発元が示した例／**[公式事例]** 開発元が紹介した利用者の声／**[独立レビュー]** 第三者による実機検証／**[利用者報告]** ストアのレビューやSNS

### 5.1 毎朝のメール・予定の整理

- **[公式事例] Duet**
  - 不動産業のJess Provencherの例：頼んでいないのに、カレンダーに誤った日付で入っていた内見予定を指摘した\[7\]
  - Mya Daltonの例：見込み客との通話の準備資料を作り、その通話がフライトの直前にあることに気づいて移動を提案した\[7\]
  - 予定を動かすかどうかは本人が判断している
- **[独立レビュー] dots（The Slide Factory、初日）**
  - 共有した表が閲覧専用になっている問題を指摘した。有用な警告だったが、確定診断ではなかった\[94\]
  - Zohoのメールでは設定ウィジェットが失敗し、不正なリンクを3回返した。Gmail以外では導入でつまずく例\[94\]
- **[独立レビュー] dots（AI Agents Library、9月30日〜10月1日）**：会議準備は9/10の評価でした。ただしレビュアー自身が「定期実行が1回成功しただけでは、数週間にわたる信頼性の証拠にはならない」と明記しています。\[95\]

### 5.2 監視・調査

- **[独立レビュー] dots（10月7日公開）**：家具選びで好みを追加すると提案を絞り込み、商品ページのセール監視も機能しました。\[96\]
- **[公式デモ] Teammates**：「競合の価格・新製品・採用を追跡し、重要なものはすぐ、週1回は要約を送る」という例文が示されています。実績ではなく例示です。\[90\]

### 5.3 開発

- **[公式デモ] Grok Bot**：バグを製品UIで再現し、チケットを起票して、修正をデバッグ用のBotに渡します。\[12\]
- **[公式事例] Duet**：開発チームの責任者が、インタビューの日程調整、プロトタイプ作成、コードの出荷に使っていると紹介されています。\[7\]
- **[独立レビュー] dots**：クラウドPCはsudoが使えないDebian 13でした。Dockerはホストのソケットに届かず、rootlessモードも失敗しています。コンテナを使う作業には制約があります。\[94\]

### 5.4 旅行・買い物・予約

- **[独立レビュー] dots（10月2日公開）**
  - ローカルファイルからのWebサイト更新と動画編集は完了した\[42\]
  - 無料の見学を希望したのに、35ドルのデイパスを提示した\[42\]
  - Uber Eatsの注文は、レビュアーがログインを手伝ってから完了した\[42\]
- **[独立レビュー] dots（10月7日公開）**：サブスクリプションの解約がパズル型CAPTCHAで止まりました。解かせてみても失敗し、最終的に利用者が対応しています。\[96\]
- **[公式の自己申告] Duet**：チケット予約などは「それほど得意ではない」とされています。\[7\]

### 5.5 個人事業・小規模チーム

- **[公式事例] Duet**：約110人を雇う飲食チェーンのオーナー、Amin Ebrahimiが、会計、サポート、マーケティング、店舗ごとの請求書処理に使っています。本人の言葉は「100個もタブを開かなくていい」です。\[7\]
- **[公式デモ] dots**：請求書の送り忘れに気づいて請求書を準備し、**承認を得てから**送付しました。\[40\]\[97\]
- **[公式デモ] Grok Bot**：夜間にアカウント調査を行い、営業担当ごとの文体で書いた「承認待ちの下書き箱」を朝までに用意します。\[12\]

### 5.6 生活・家族

- **[公式事例] Duet**：子どもとの時間の前にTo-Doを渡しておき、夜にレポートを受け取る使い方です。\[7\]
- **[利用者報告・失敗] Muse**：「Allow Always」を選んだ後に、住所が取引相手へ漏れました。包括的な許可は情報漏えいにつながります。\[83\]

### 5.7 複数エージェントの分業

- **[公式デモ] Grok Bot**：chief of staff役のBotの下に、受信箱、経費、採用、バグ修正を担当する専門Botを置く構成です。\[12\]
- **[公式デモ] Cue**：会場調査、候補の絞り込み、資料作成を3体で分担し、最終判断は人間が行います。\[5\]
- **[利用者報告] Cue**：グループチャットで、呼んでいないモデルが反応すると報告されています。\[69\]

### 5.8 失敗・介入のまとめ

| 事象 | 製品 | 根拠 | 示唆 |
|---|---|---|---|
| CAPTCHAで解約できない | dots | 独立レビュー | 解約や本人確認は人間が担当する\[96\] |
| ログインに人の手助けが必要 | dots | 独立レビュー | ログイン方法を事前に設計しておく\[42\] |
| 希望と違う有料商品を提示 | dots | 独立レビュー | 購入前の承認を必須にする\[42\] |
| 権限が失われる・遅い | dots | 利用者報告（Reddit） | 長期稼働はまだ未成熟\[98\] |
| 住所の漏えい | Muse | 利用者報告・報道 | 「常に許可」を使わない\[83\] |
| 週の途中で上限に到達 | Grok Bot | 利用者報告＋CEOの発言 | 費用の上限を管理する\[99\] |
| 削除・再登録の不具合 | Cue | 利用者報告 | 撤退の手順を事前に確認する |

---

## 6. シナリオ別の導入・選定案

### A. 個人利用

- **候補**
  - Muse：無料で試せる
  - Gemini Spark：Googleの個人アカウントが中心の場合
  - dots：すでにProを契約している場合
- **最初の1週間に試すこと**：毎朝のブリーフ、返信の下書き、予定の衝突チェック
- **許可する権限**
  - メールとカレンダーは読み取りのみ
  - 支払い手段は接続しない
  - dotsではCustom Rulesで送信を「実行前に確認」にする
- **確認すべき成果**：見落としを指摘した件数と誤検知の件数、下書きをそのまま使えた割合、通知の頻度
- **撤退条件**：承認していない対外行動が1件でもあった場合、または第三者の情報が漏れた場合

### B. 個人開発者

- **候補**
  - Grok Bot：日本での提供可否は要確認
  - dots
  - Perplexity Teammates：予算がある場合
  - Hermes Agent / OpenClaw：サンドボックスを必ず有効にすること
- **最初の1週間に試すこと**：Issueの分類案、失敗したCIのログ要約、依存パッケージと技術ニュースの週次ダイジェスト
- **許可する権限**
  - 特定のリポジトリに限った読み取り専用、または最小権限のトークン
  - mainへのpush、リリース、シークレットは与えない
  - 書き込みは「ドラフトPRのみ」から始める
- **確認すべき成果**：トリアージが自分の判断と一致した割合、CIの原因推定が当たったか、差分が指示範囲に収まっているか
- **撤退条件**：範囲外のコミット、シークレットの露出、使用量が想定の2倍を超えた場合

### C. 組織・自治体

- **候補**
  - Copilot Cowork（職場アカウント、監査ログあり）
  - dots Business Premium／Enterpriseベータ（管理者が有効化。既定で学習に使われない）
- **避けるべきもの**：個人向けのMuse、Cue、Grok Botを職員のアカウントで使うこと。Gemini Sparkは法人Workspaceの対象外と報じられています。\[10\]
- **最初の1週間に試すこと**：他の自治体の施策や審議会資料の定点観測、公開データを使った報告書の骨子作成
- **許可する権限**：公開Webの閲覧と専用フォルダへの保存のみ。個人情報、非公開文書、職員のメールは接続しない
- **確認すべき成果**：出典URLを全件照合する、試行前後の作業時間を測る、監査ログに何が残るかを確認する
- **契約面の確認事項**：データ保持期間、処理リージョン、学習利用、サブプロセッサー、ログの提出可否、終了時の削除
- **撤退条件**：出典の誤りが基準を超えた場合、または監査要件を満たすログが取れない場合

---

## 7. 権限管理・セキュリティ・運用上の注意

| リスク | 製品ごとの仕組み・事例 | 対策 |
|---|---|---|
| 見える範囲が広すぎる | dotsはプラグインの権限をWork・Codexと共有。Teammatesはプラグインと同じ権限で動く | 既存の接続を棚卸しし、テスト用アカウントを使う |
| プロンプトインジェクション | Metaは未解決と認めている。Hermesは「境界はOSだけ」と明記 | 外部のメールやWebを読むエージェントに、送信・支払いの権限を与えない\[84\]\[92\] |
| 誤送信・誤購入・誤削除 | Duet・Muse・dotsは承認制 | 「常に許可」を使わない。購入は仮想カードと予算上限を付ける |
| 資格情報 | Duet・Muse・dotsはモデルにパスワードを見せない設計。OpenClawではトークン流出のCVE | セルフホストする場合は外部に公開せず、パッチを当て、サンドボックスを使う\[80\]\[92\] |
| 費用の増大 | Teammatesは並列実行、Grok Botは週次枠、Duetは背景での確認で枠を消費 | 毎週使用量を確認し、実行頻度を下げる |
| 記憶とログ | Museは監査証跡と「忘れて」に対応。dotsは記憶を個別に削除できない（二次情報） | 機微情報を記憶させない |
| ベンダーの継続性 | ManusとMetaの分離に伴うデータ削除、料金の急変 | 成果物は自分のストレージに保存する\[20\] |
| 個人契約と職場契約 | Coworkは職場向けが一般提供、個人向けはプレビュー。dotsはプランによって学習の扱いが違う | 業務データを個人プランで扱わない\[24\] |

**委任範囲を広げる段階**

- 段階0：読み取りと要約
- 段階1：下書き（2週間、事実誤認や誤った宛先がゼロなら次へ）
- 段階2：自分宛ての送信、カレンダーの仮押さえ（実行前の確認つき）
- 段階3：上限つきの対外行動（少額の購入や定型の返信）。ログを毎週確認する

**どの段階でも人間が最終確認する作業**：契約・署名、送金、解約、第三者の個人情報の提供、公開投稿、本番環境へのデプロイ、データ削除、行政・医療・法務に関わる送信。

---

## 8. 料金・アクセス条件で選ぶ場合

| 条件 | 選択肢 | 注意点 |
|---|---|---|
| 無料で試したい | Muse、Cue（招待コードがある場合） | Museは登録時にカードが必要と報道。Cueは正式料金が未定\[76\] |
| 月30ドル前後 | Grok Bot | 日本での提供は公式に未記載。利用枠は週次で共有\[1\]\[48\] |
| 月14,500円〜 | Gemini Spark（Ultra） | Proで使えるかは要確認\[29\] |
| 月16,800円〜 | dots（Pro） | Work・Codexで実行したタスクは利用枠を消費\[35\]\[38\] |
| 月200ドル | Teammates | 研究プレビュー、クレジット制 |
| 組織での利用 | Copilot Cowork、dotsのBusiness系プラン | 管理者による有効化が必要 |
| 日本からは利用不可 | Claude Duet | 米国限定のウェイトリスト\[57\] |

---

## 9. 未確認事項

- **dots**：ヘルプ本文、日本語の品質、2体目以降の料金、暫定措置が終わった後の利用枠
- **Grok Bot**：日本での提供、トライアルの現状（情報が矛盾）、承認が必要な操作の一覧、記憶の削除
- **Duet**：米国以外での提供時期
- **Cue**：正式料金、週次の利用枠、日本での決済の可否、監査ログ
- **Muse**：日本向けパートナー連携の時期、Confidential VMの提供時期
- **Teammates**：提供国、日本語対応、作成できる数の上限
- **Gemini Spark**：日本のProへの拡大が実施されたか
- **全般**：本調査では**実機検証を行っていません**。第三者による点数（dotsが10タスクで平均8.8点、PersonalAgentBenchなど）は検証条件が不明なため、順位の根拠には使っていません。\[46\]\[100\]

---

## 10. 情報源の確認状況（確認日：2026-11-08）

- **公式ページを直接取得**：Grok Botの発表（8月11日）、Claude Duetの発表（10月21日）、Manus 2.0の発表（9月28日）、Museの発表（9月8日、30日更新）、Perplexityのchangelog（11月6日）
- **公式ページを検索の断片でのみ確認**：OpenAIのdotsの発表とヘルプ、Perplexityのヘルプ、Meta日本法人の発表（10月23日）、Microsoftサポート
- **サブエージェントが確認**：CueのApp Store（米国は11月8日取得）、Manusのヘルプセンター
- **補助的に使ったもの**：CNBC、TechCrunch、The Next Web、Search Engine Journal、Impress Watch、窓の杜、マイナビなどの報道と独立レビュー、ストアレビュー

---

## 必須の結論

1. **何が本質的に変わるか**：主導権と時間軸です。エージェントは目標を持ち続け、利用者がいない間も読み、調べ、準備し、自分から承認を求めてきます。そのため、価値の源泉は回答の質から「何にアクセスさせ、何を承認制にするか」という権限の設計に移ります。
2. **継続的に任せると効果がある作業**：変化を検知して要約し、下書きまで作る作業です（朝のブリーフ、監視、トリアージ、会議準備）。CAPTCHA、ログイン、決済を伴う用事は、今のところ人間の介入が前提です。
3. **複数エージェントの使い分け**：役割と権限を分けられるなら価値があります。ただし、全Botが1台のPCを共有するような製品では、エージェント間の境界が弱くなります。読み取り専用の監視担当と承認制の実行担当に分け、同じアカウントへの書き込み権限を重ねないことを推奨します。
4. **日本在住の個人にとっての選択肢**：今すぐ試しやすいのはMuse、Gemini Spark（Ultra）、dots（Pro）、Cue（招待コードがある場合）です。まだ試しにくいのは、Claude Duet、Perplexity Teammates、Hark Pro、そして日本での提供が公式に未記載のGrok Botです。
5. **小規模な試用の始め方**：試用専用のアカウントを読み取り専用で接続し、送信・購入・削除は承認制にします。「常に許可」は使いません。最初の1週間はブリーフと下書きだけを任せ、ログと使用量を毎週確認します。撤退時の手順（連携の切断、アカウント削除。CueはManusと一緒に削除される）も事前に確認しておきます。

## 出典

1. [What is Grok Bot? Pricing, Capabilities, and Considerations from an Ad Manager's Perspective｜リョウ｜Webマーケ5年目×生成AI活用](https://note.com/ryou_hikaku/n/n0588931f3a1e?hl=en)
2. [Grok Bot Explained: xAI's AI Agents (2026)](https://toolradar.com/blog/what-is-grok-bot)
3. [Personal AI Agents 2026: Muse, Dots, Grok Bot Compared](https://aicrawlercheck.com/blog/personal-ai-agents-website-guide-2026)
4. [Introducing Muse: The World’s First Personal AI Agent Built for Everyone](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
5. [Introducing Manus 2.0](https://manus.im/blog/introducing-manus-2-0)
6. [ChatGPT Dots: how to use an always-on AI agent without drowning in average work](https://02ui.com/blog/how-to-use-chatgpt-dots-always-on-ai-agent/)
7. [Introducing Claude Duet](https://claude.com/resources/articles/claude-duet)
8. [Perplexity Teammates: What They Do, Cost, Risks (2026)](https://www.explainx.ai/blog/perplexity-teammates-persistent-agents-computer-max-slack-isolated-desktops-credits-what-to-check-2026)
9. [Google Gemini Spark: Always-On Agent Runtime Guide](https://vandatateam.com/blog/google-gemini-spark)
10. [Gemini Spark ついに日本語対応！利用条件・料金・始め方を解説【2026年7月】](https://www.elcamy.com/blog/gemini-spark-japanese)
11. [Microsoft Brings Copilot Cowork AI Agent to General Availability](https://www.reworked.co/digital-workplace/microsoft-brings-copilot-cowork-ai-agent-to-general-availability/)
12. [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot)
13. [Manus 2.0 and Cue give AI agents their own email, phone and wallet](https://thenextweb.com/news/manus-2-0-cue-ai-agents-email-phone-wallet)
14. [Manus 2.0 and Cue: Personal AI Agents Launched](https://www.briefs.co/news/manus-rolls-out-manus-2-0-and-cue-app-pushing-personal-ai-ag/)
15. [China blocks Meta's \$2 billion takeover of AI startup Manus](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)
16. [Manus (AI agent)](<https://en.wikipedia.org/wiki/Manus_(AI_agent)>)
17. [Cue by Manus Review (2026): Personal AI Agents Tested](https://myclaw.ai/blog/manus-ai-agent-cue-review)
18. [AI startup Manus raises \$500 million after Meta acquisition blocked by China](https://techxplore.com/news/2026-10-ai-startup-manus-million-meta.html)
19. [Meta Bought Manus. Beijing Undid It. Then Manus Raised \$500M.](https://www.foundra.ai/key-reads/manus-meta-acquisition-unwound-500-million-raise-deal-risk-lessons-first-time-founders)
20. [Manus Leaves Meta: Back Up Your Data Before Aug 23, 2026](https://explainx.ai/blog/manus-meta-separation-data-deletion-backup-guide-august-2026)
21. [Grok Bot pricing and usage limits, explained (2026)](https://breakorbit.ai/grok-bot-pricing)
22. [OpenAI Unveils "dots," an Always-On AI Agent That Keeps Working After the Chat Ends](https://xenospectrum.com/en/openai-dots-always-on-agents/)
23. [ChatGPT dotsとは｜現実的な使い方と任せる範囲｜株式会社課題解決プラットフォーム](https://0120.co.jp/blog/ai-training-181/)
24. [Get started with Microsoft Copilot Cowork for personal accounts (Preview)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork)
25. [What Is Hark AI Agent? Quick-Start For Your Agent OS](https://agentos.guide/hark-ai-agent)
26. [OpenClaw vs Hermes Agent: The best agent harness in 2026](https://composio.dev/content/openclaw-vs-hermes-agent)
27. [Gemini Sparkを世界一わかりやすく解説！日本でも7月から利用可](https://apptime.co.jp/media/gemini-spark%E3%82%92%E4%B8%96%E7%95%8C%E4%B8%80%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F%E8%A7%A3%E8%AA%AC%EF%BC%81%E3%81%84%E3%81%A4%E3%81%8B%E3%82%89%E6%97%A5%E6%9C%AC%E3%81%A7)
28. [Best Personal AI Agents in 2026: Grok Bot, Muse, Dots, Instinct, Hark Pro & Open Source Alternatives](https://rakazo.com/alternatives/)
29. [Gemini Sparkとは？機能・料金・日本での使い方【2026年最新】](https://aidaim.co.jp/gemini-spark/)
30. [Microsoft Copilot Cowork: What It Is and How to Use It](https://www.datacamp.com/blog/microsoft-copilot-cowork)
31. [Gemini Spark: Google's Always-On Personal AI Agent](https://www.digitalapplied.com/blog/gemini-spark-always-on-personal-agent)
32. [OpenAI launches dots, always-on AI agents with their own cloud computers](https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday)
33. [OpenAI Dots: Always-On ChatGPT Agents Explained](https://www.relevantaudience.com/ai/openai-dots-always-on-agents-chatgpt/)
34. [ChatGPTのdotsとは？できること・料金・日本で使えるかを整理](https://apptime.co.jp/media/chatgpt-dots/)
35. [ChatGPT dotsとは？できること・料金・WorkやCodexとの違い【2026年11月】](https://www.orcacoltd.jp/chatgpt-dots-guide/)
36. [Introducing dots](https://openai.com/index/introducing-dots/)
37. [OpenAI dotsとは｜できること・料金・日本で使えるか【2026年10月】 ｜ 株式会社Uravation](https://uravation.com/media/openai-dots-guide-2026-09/)
38. [ChatGPTのdots(ドッツ)とは｜日本での対象プラン・料金・dotの使い方](https://digital-sales-job.com/chatgpt-dots/)
39. [OpenAI Dots: What They Are, Access, Safety and Cost](https://lmspedia.org/openai-dots/)
40. [OpenAI’s new AI agent has a ‘slow morning’ as it stumbles in live demo](https://americanbazaaronline.com/2026/10/01/openais-new-ai-agent-has-a-slow-morning-489182/)
41. [Dots AI Review: OpenAI's Always-On Agent Explained](https://myclaw.ai/blog/dots-ai)
42. [OpenAI Dots review: website work and online errands](https://www.neoteo.com/en/openai-dots-review-website-and-video-tasks-worked-online-errands-hit-snags)
43. [OpenAI Dots and Email: What a Dot Can Do With Your Inbox (2026)](https://www.dragapp.com/blog/openai-dots/)
44. [OpenAI Dots: What They Are and How They Compare](https://cellcog.ai/blog/openai-dots/)
45. [「dots」とは？ChatGPTの新機能・使い方・料金を解説](https://chatsense.jp/blog/chatgpt-dots)
46. [OpenAI's Dots score well in hands-on test, but rank third among five agents](https://cryptobriefing.com/openai-dots-ai-agent-hands-on-review/)
47. [Grok Bot: What It Is, Pricing and What It Can Do (2026)](https://grokmag.com/grok-bot/)
48. [Grok Bot Explained: Pricing, Plans, and How It Works](https://www.lindy.ai/blog/grok-bot)
49. [Grok Bot Pricing: From \$30 a Month, Every Route Compared](https://cellcog.ai/blog/grok-bot-pricing/)
50. [Grok Bot Pricing and Limits: Free Trial, Tiers, Weekly Pool](https://www.toolcolumn.com/learn/grok-bot-pricing-by-plan)
51. [Official Grok Bot Breakdown (2026)](https://www.vellum.ai/blog/official-grok-bot-breakdown)
52. [Grok Bot: Pricing, Access Limits, and How to Use It](https://coursiv.io/blog/grok-bot)
53. [What Is Grok Bot? xAI's Personal AI Agent Explained (2026)](https://wetheflywheel.com/en/ai-assistants/grok-bot/)
54. [Personal AI Agent Security: Discovering and Governing dots, Grok Bot, Instinct, Muse, & Muse Code](https://noma.security/blog/personal-ai-agent-security-discovering-and-governing-dots-grok-bot-muse-muse-code)
55. [Anthropic announces preview of Claude Duet, a personal AI agent to take on Muse, Dots](https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html)
56. [Claude Duet: Anthropic's AI Agent That Messages You First](https://www.datacamp.com/blog/claude-duet)
57. [Meta Muse（ミューズ）とは？できること・料金・日本での使い方と連携サービスを解説【2026年10月】](https://leaph.co.jp/leaphlet/ai/meta-muse/)
58. [Cue by Manus - App Store - Apple](https://apps.apple.com/us/app/cue-by-manus/id6808613358)
59. [Cue by Manus App - App Store](https://apps.apple.com/jp/app/cue-by-manus/id6808613358?l=en-US)
60. [Can I connect multiple messaging Agents at once in Cue?](https://help.manus.im/en/articles/14178640-can-i-connect-multiple-messaging-agents-at-once-in-cue)
61. [Manus Launches Cue Agents With Phone Numbers and Wallets](https://www.implicator.ai/manus-cue-agents-phone-numbers-wallets/)
62. [Cue by Manus: Personal Agents with Phone, Email, Wallet](https://www.oflight.co.jp/en/columns/cue-by-manus-personal-agents-app-guide-2026)
63. [Cue by Manus: What It Is, Invite Code and Price](https://cellcog.ai/blog/manus-cue/)
64. [What is the current membership pricing for Manus? | Manus Help Center](https://help.manus.im/en/articles/11711111-what-is-the-current-membership-pricing-for-manus)
65. [Cue - Your Personal Agents, With Their Own Identity](https://cue.im/)
66. [Manus 2.0 and Cue: AI Agents With Wallets (October 2026) - AIToolsReview](https://aitoolsreview.co.uk/insights/manus-2-cue-agents)
67. [How can I delete my account?](https://help.manus.im/en/articles/11711969-how-can-i-delete-my-account)
68. [Cue by Manus - Apps on Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en)
69. [Cue by Manus - Free Android App Stats](https://www.appbrain.com/app/cue-by-manus/ai.manus.agents)
70. [Meta、パーソナルAIエージェント「Muse」を日本で提供開始](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)
71. [Meta Muse AI Agent: What It Is, How It Works, Access & Pricing](https://www.aiagentslibrary.com/blog/meta-muse-ai/)
72. [What Is Meta Muse? Price, Countries, App & Privacy](https://privacytestlab.com/articles/meta-muse-ai-agent)
73. [Meta Muse AI for Social Media Managers (2026): What the Agent Does, What It Costs, and How to Connect a Scheduler](https://postfa.st/blog/meta-muse-ai-social-media-managers)
74. [What Is Meta Muse? The AI Agent, Models and Plans Explained](https://techjournal.org/what-is-meta-muse)
75. [Meta Muse: Features, Access, and Pricing Explained](https://www.datacamp.com/blog/muse-agent)
76. [Meta Muse: What It Is, What It Costs, and 2 Problems](https://www.fieldy.ai/blog/meta-muse)
77. [Meta Muse Pricing: Free, Power, and Maximum Plans](https://www.layer3labs.io/guides/meta-muse-pricing)
78. [MetaのパーソナルAIエージェント「Muse」、日本でスタート - Impress Watch](https://www.watch.impress.co.jp/docs/news/2150567.html)
79. [MetaがパーソナルAIエージェント「Muse」を日本で提供開始、メールや予約などを自律的に実行](https://news.mynavi.jp/techplus/article/20261023-5178430/)
80. [Meta Muse: Personal Agent + Sentinel VM Security (Sept 2026)](https://explainx.ai/blog/meta-muse-personal-agent-launch-sentinel-vm-security-2026)
81. [Meta Museとは｜日本上陸の常駐AIエージェント【2026】](https://tatap.jp/knowledge/meta-muse-japan/)
82. [Meta Muse Zero-Day: Hidden Setting Enables Backdoor](https://tech-insider.org/meta-muse-zero-day-backdoor-vulnerability-2026/)
83. [AI Agent Privacy: Surprising Risks Behind Safe Promises](https://www.progressiverobot.com/2026/10/10/ai-agent-privacy-promises-openai-dots-meta-muse/)
84. [Meta Muse: Personal AI Agent Features and Privacy Guide](https://www.digitalapplied.com/blog/meta-muse-personal-ai-agent-guide)
85. [Perplexity Teammates: AI Agents That Own Your Ongoing Work - DEV Community](https://dev.to/neuraitool/perplexity-teammates-ai-agents-that-own-your-ongoing-work-1bpd)
86. [Get started with Perplexity teammates - Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)
87. [Perplexity Teammates take over a project for weeks, and here is what that colleague really costs](https://www.i-scoop.eu/perplexity-teammates/)
88. [Perplexity launches Teammates, persistent AI agents for Max subscribers](https://letsdatascience.com/news/perplexity-launches-teammates-persistent-ai-agents-for-max-s-704b7a36)
89. [Perplexity launches AI agents for work](https://daily.dev/posts/perplexity-launches-ai-agents-for-work-saaaxw0ib)
90. [Teammates, fully local Computer on Mac, and Voice mode](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)
91. [Microsoft's AI agent Copilot Cowork now available globally](https://seekingalpha.com/news/4604106-microsofts-ai-agent-copilot-cowork-now-available-globally-cowork-1-to-come-soon)
92. [OpenClaw vs Hermes Agent: Which AI Agent Should You Run in 2026?](https://www.context.dev/blog/openclaw-vs-hermes-agent)
93. [Hark AI: What Hark Pro Does, What It Costs, Early Reports](https://www.usecarly.com/blog/hark-ai/)
94. [OpenAI Dots Review: How It Works and Our First Day](https://www.theslidefactory.com/post/openai-dots-review)
95. [OpenAI Dots Review: I Tested 10 Business Tasks (2026)](https://www.aiagentslibrary.com/blog/openai-dots-review/)
96. [OpenAI Dots review: useful follow-up, real limits](https://www.neoteo.com/en/a-reported-openai-dots-test-finds-useful-follow-up-and-a-hard-stop)
97. [OpenAI Debuts 'Dots' AI Agent, Scraps GPT-6.1 After Deception Tests](https://www.forbes.com/sites/the-prompt/2026/09/29/with-dots-openais-answer-to-muse-and-instinct-is-here/)
98. [ChatGPT Dots Review 2026: A Complete Guide](https://emergent.sh/learn/chatgpt-dots-review)
99. [Grok Bot usage limits: Musk says serving costs were unsustainably high](https://www.datastudios.org/post/grok-bot-usage-limits-musk-says-serving-costs-unsustainably-high)
100. [Hark Review 2026: Features, Privacy, and Verdict](https://agent-finder.co/reviews/hark)

# パーソナルAIエージェント比較調査（2026年11月版）

調査基準日・確認日：2026年11月8日（日本時間）。本資料は `YanTKYS/devlog` のノートへ再編集するための一次調査資料であり、製品の実機評価や導入認定ではない。公式発表、現行ヘルプ、料金、規約と、出典を特定できた実践報告を区別して整理した。

GitHubの編集、PR作成、外部アカウントの接続、契約・購入、有料実機試験は実施していない。「未確認」は非対応を意味せず、取得した資料だけでは確定できなかったことを表す。公開ページは後から更新されるため、日付のないヘルプの内容は当日の取得スナップショットとして扱い、過去の全アカウントへの配信を保証しない。

## エグゼクティブサマリー

**本質的な変化は「質問に答えるAI」から「期限・監視対象・成果物・承認条件を持つ仕事の担当者」への移行である。**([OpenAI発表](https://openai.com/index/introducing-dots/)、[Duet発表](https://claude.com/resources/articles/claude-duet)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) dots、Grok Bot、Claude Duet、Cue、Muse、Teammatesはいずれも、会話を離れた後の仕事や継続的な文脈を製品設計に取り込んでいるが、能動的な確認と対外的な変更・送信の権限は同一ではない。([OpenAI発表](https://openai.com/index/introducing-dots/)、[Duet発表](https://claude.com/resources/articles/claude-duet)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 例えばdotsの自発的なバックグラウンド調査は読取専用で、Duetはアプリを数時間おきに確認し、Teammatesは担当役割から複数の作業を組み立てるという違いがある。([OpenAI発表](https://openai.com/index/introducing-dots/)、[Duet発表](https://claude.com/resources/articles/claude-duet)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))

- **日本での低リスクな入口：** Museは10月23日に日本提供開始が公式確認でき、使用量制限付き無料枠があるため、公開情報の継続監視や予定の確認から試す候補になる。([Meta日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[Muse料金](https://www.meta.com/help/subscriptions/1021145227643680/)、[Geminiヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[日本向けGoogle料金](https://gemini.google/jp/subscriptions/?hl=ja)) Tasks in Geminiは個人GoogleアカウントのPro／Ultraが対象で、日本向けProの表示価格は月2,900円だが、Keep ActivityとPersonal Intelligenceの有効化が必要で、端末依存の実行条件も確認したい。([Meta日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[Muse料金](https://www.meta.com/help/subscriptions/1021145227643680/)、[Geminiヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[日本向けGoogle料金](https://gemini.google/jp/subscriptions/?hl=ja))
- **既存の有料環境を生かす候補：** dotsはPro 100／200／500などが入口で、個人Proの最低価格は月100米ドルである。([Pro料金ヘルプ](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[dotsヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Max料金ヘルプ](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[Grok Bot現行ページ](https://x.ai/bot)) Teammatesは個人Max限定のWebリサーチプレビューで、Maxは月200ドルまたは年2,000ドル、Grok Botは現行のThe X SubscriptionのPremium月30ドル以上が入口となるが、日本向けのBot固有提供条件は別途確認が必要である。([Pro料金ヘルプ](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[dotsヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Max料金ヘルプ](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[Grok Bot現行ページ](https://x.ai/bot))
- **現時点で日本から試しにくい候補：** Claude Duetは米国のPro／Max／Ultra利用者向けウェイトリストで、日本語ヘルプがあっても日本提供を意味しない。([Duetヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Cue公式掲載](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Hark利用ガイド](https://hark.com/using-hark)、[Instinct規約](https://instinct.com/terms)) Cueは招待コードが必要で、Hark ProとInstinctは、日本向けの地域・言語・サービス利用条件を本調査では確定できなかった。([Duetヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Cue公式掲載](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Hark利用ガイド](https://hark.com/using-hark)、[Instinct規約](https://instinct.com/terms))
- **実績が比較的具体的な用途：** メールと予定の突合、返信漏れの抽出、会議準備、条件を絞った商品・ニュース監視である。([PC Watchのdots実践](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)、[Duetの10タスク検証](https://www.aiagentslibrary.com/blog/claude-duet-review/)、[Android AuthorityのMuse実践](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) 公開された実践報告には、請求書と発注書の支払日の不一致発見、Gmailの返信要否整理、eBayの定期検索がある一方、接続メールアカウントの取り違えや音声文字起こし不可も報告されている。([PC Watchのdots実践](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)、[Duetの10タスク検証](https://www.aiagentslibrary.com/blog/claude-duet-review/)、[Android AuthorityのMuse実践](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/))
- **複数エージェントの価値：** 調査、検証、成果物作成を分ける価値はあるが、役割を分けただけでは権限は隔離されない。([Grok Bot FAQ](https://docs.x.ai/grok-bot/faq)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) Grok Botの同一アカウント内Botsはファイル・ブラウザ・ログインを共有し、Teammatesは各自のコンピューターを持つ一方、同じProjectの文脈を共有するため、どちらも役割名だけを機密区分に使わない。([Grok Bot FAQ](https://docs.x.ai/grok-bot/faq)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))
- **組織・自治体向けの結論：** 最初は公開情報だけを入力し、非公開ファイル、個人情報、職員メール、決裁権限を渡さない試行を推奨する。([Teammates対象条件](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Gemini対象条件](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Duet対象条件](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 個人MaxのTeammates、個人GoogleアカウントのTasks、米国個人プレビューのDuetを、そのまま組織契約の代替と見なしてはならない。([Teammates対象条件](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Gemini対象条件](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Duet対象条件](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet))

選定の推奨は同条件の性能順位ではなく、利用条件と業務設計に基づく。本調査では6製品の同一タスク実測をしておらず、「最強」「最も正確」「何倍効率化」といった総合順位は付けない。

## パーソナルエージェントの定義と市場動向

### 本資料の判断基準

本資料では「本人に紐づく継続的な文脈を持ち、複数手順の仕事を実行し、一定の条件で本人不在でも進行・再確認できるもの」を広義のパーソナルエージェントとする。専用クラウドPCは必須とせず、仕事の継続性、アクセス範囲、トリガー、外部への作用、人間の監督という五つの軸で分類する。

| 分類 | 任せるもの | 継続性の判断 | 本資料での位置付け |
|---|---|---|---|
| 通常の会話型AI | 一問一答、文章の下書き | 次の指示が中心 | 単独では対象外 |
| 単発エージェント | 一つの調査・予約候補比較など | 依頼した仕事の完了まで | 継続型との比較対象 |
| スケジュール型自動化 | 毎朝の定型要約など | 指定時刻・条件で繰り返す | 役割の保持や変化への対応とは別 |
| 継続型・能動型 | 「このテーマを追い、変化したら調べる」 | 新しい状況に応じて次の仕事を組む | 中心的な調査対象 |
| 複数エージェント分業 | 調査、作成、検証の担当分け | 担当間の引き継ぎ | 個人利用でも成立 |
| 共有・組織エージェント | チームの共通業務 | 組織ID、管理、監査を伴う | 個人秘書とは契約・責任が異なる |

これは本資料の整理であり、業界統一の認証基準ではない。「24/7」という表示から、毎秒すべてのメールを読むこと、上限なしの計算、即時応答、障害時の自動復旧を推定しない。

### 2026年の変化をどう読むか

公式発表の時系列では、Gemini Sparkが5月19日、Grok Botが8月11日、Museが9月8日、dotsが9月29日、Claude Duetが10月21日、Teammatesのブログが11月4日であり、継続的な担当役割と通知が主要な訴求になっている。([Google発表](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)、[Grok Bot発表](https://x.ai/news/introducing-grok-bot)、[Meta発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[dots発表](https://openai.com/index/introducing-dots/)、[Duet発表](https://claude.com/resources/articles/claude-duet)、[Teammatesブログ](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[Manus公式記事一覧](https://manus.im/blog)) Cueは9月28日のManus 2.0で、Manus本体とは別の個人エージェントアプリとして紹介された。([Google発表](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)、[Grok Bot発表](https://x.ai/news/introducing-grok-bot)、[Meta発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[dots発表](https://openai.com/index/introducing-dots/)、[Duet発表](https://claude.com/resources/articles/claude-duet)、[Teammatesブログ](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[Manus公式記事一覧](https://manus.im/blog))

ただし「発表日にすべて使える」わけではない。([Duetヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[dotsヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Geminiヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) Duetはウェイトリスト、Teammatesはリサーチプレビュー、dotsのEnterpriseは11月18日まで管理者プレビューという段階差があり、Geminiも発表時のSparkの説明より現行Tasksヘルプの実行条件を優先する必要がある。([Duetヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[dotsヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Geminiヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop))

### 追加対象の選定

- **Tasks in Gemini、Copilot Cowork：** 個人アカウント・組織アカウントの違い、既存のGoogle／Microsoft環境との結び付きが意思決定に重要なため追加した。([Google公式ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Microsoft公式概要](https://learn.microsoft.com/en-us/copilot/cowork/))
- **OpenClaw、Hermes Agent：** 実行環境を自分で管理する選択肢として追加した。([OpenClaw公式説明](https://docs.openclaw.ai/start/why-openclaw)、[Hermes公式ドキュメント](https://hermes-agent.nousresearch.com/docs)) アプリが手元にあっても、外部モデルAPIへ送信するデータまでローカルとは限らない点を比較する。([OpenClaw公式説明](https://docs.openclaw.ai/start/why-openclaw)、[Hermes公式ドキュメント](https://hermes-agent.nousresearch.com/docs))
- **Hark Pro、Instinct：** 個人秘書型の設計とプライバシー・権限委任の違いを比較するため追加したが、日本で直ちに利用できる推奨製品とは位置付けない。([Hark公式ガイド](https://hark.com/using-hark)、[Instinct公式ページ](https://instinct.com/)、[Instinct規約](https://instinct.com/terms))

一般的なチャットAIや単発のコーディングエージェントは追加していない。製品数を増やすより、必須6製品の使い始め方、権限、実践根拠の深さを優先した。

## 主要製品の比較表

### 提供・アクセス・価格

価格の「ドル」は掲載ページの `$` 表記を指す。OpenAIのProヘルプはUSDを明示するが、他ページは通貨コード・税区分が明示されない場合があり、日本での税込請求額への換算は行っていない。

| 製品・提供元 | 提供段階 | 日本・日本語 | 最低料金・試用 | 利用窓口 |
|---|---|---|---|---|
| dots／OpenAI | 個人Pro等に段階提供。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) Enterprise等は管理者プレビュー中。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | ProはEEA・英国・スイス除外。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 日本は除外されないが個別配信待ちあり。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) dot固有の日本語保証範囲は未確認。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | Pro 100は100 USD/月。([Pro料金](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[発表](https://openai.com/index/introducing-dots/)) 最初のdotは対象プラン内。([Pro料金](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[発表](https://openai.com/index/introducing-dots/)) 無料個人枠なし。([Pro料金](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[発表](https://openai.com/index/introducing-dots/)) | Web、デスクトップ、iOS・Android、Slack・Teams。([発表](https://openai.com/index/introducing-dots/)、[ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) モバイルWeb非対応。([発表](https://openai.com/index/introducing-dots/)、[ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) |
| Grok Bot／xAI系・Cursor基盤 | ベータとして発表。([発表](https://x.ai/news/introducing-grok-bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) 現行はThe X Subscription対象シート。([発表](https://x.ai/news/introducing-grok-bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) | 日本向けBot利用可否は公式の明示を確保できず。([FAQ](https://docs.x.ai/grok-bot/faq)) 多言語UIあり、日本語の個別確認は未了。([FAQ](https://docs.x.ai/grok-bot/faq)) | Premium $30/月。([製品ページ](https://x.ai/bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) アカウントにより7日間・クレジット付き試用。([製品ページ](https://x.ai/bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) ストア試用は別条件。([製品ページ](https://x.ai/bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) | macOS、Windows、Linux、iOS 18+、iPadOS 18+、Android 9+。([FAQ](https://docs.x.ai/grok-bot/faq)) |
| Claude Duet／Anthropic | 米国ウェイトリスト・研究プレビュー。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 日本は現行対象外。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 日本語ヘルプの存在と対象地域は別。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | Pro $20/月、年$200。([料金](https://claude.com/pricing)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 対象個人プラン内追加料金なし。([料金](https://claude.com/pricing)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 招待が必要。([料金](https://claude.com/pricing)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 独立iOS・Androidアプリ、claude.ai。([発表](https://claude.com/resources/articles/claude-duet)) |
| Cue by Manus／Butterfly Effect | 招待コード付き早期アクセス。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) | iOS掲載言語に日本語。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) 日本の利用資格・ストア配信・招待入手は未確定。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) | 招待後Plus特典無料。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) 電話番号等のアプリ内購入あり。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) 総額・周期は要確認。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) | モバイル・デスクトップ案内、現行iOS／Android掲載。([公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) |
| Muse／Meta | 日本で10月23日提供開始。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) | 日本提供確認。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) 日本語機能の範囲と音声・アバターは別途確認。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) | 制限付き無料、Power $20/月、Maximum $100/月。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)) 円建て公式定価は本調査未確認。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)) | iOS、Android、muse.ai。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)) WhatsApp等の国別条件に注意。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)) |
| Teammates／Perplexity | 個人MaxのWebリサーチプレビュー。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) Enterpriseは初回対象に自動包含されない。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | 日本の個別除外は取得資料になし。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) アカウント表示で最終確認。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 固有日本語対応表は未確認。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | Max $200/月・$2,000/年。([Max](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[製品ページ](https://www.perplexity.ai/hub/products/teammate)) 期間限定の無料使用特典後はMaxクレジット。([Max](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[製品ページ](https://www.perplexity.ai/hub/products/teammate)) | 現行Web。([製品ページ](https://www.perplexity.ai/hub/products/teammate)) ネイティブモバイル・デスクトップは今後。([製品ページ](https://www.perplexity.ai/hub/products/teammate)) |

### 実行・自律性・環境

以下の機能欄は公式仕様・説明であり、本調査の実機確認結果ではない。具体的な利用者実績は後段の事例章に分離した。

| 製品 | 継続・定期・能動性 | 実行環境・PCを閉じる場合 | 記憶・並列 | 操作・対外行動 |
|---|---|---|---|---|
| dots | 目標を継続。([発表](https://openai.com/index/introducing-dots/)、[ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 定期確認可。([発表](https://openai.com/index/introducing-dots/)、[ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 自発的調査は読取専用。([発表](https://openai.com/index/introducing-dots/)、[ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | 専用クラウドPC。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) ローカルPC接続は任意・初期オフ。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | ChatGPT記憶＋dot独自記憶。([発表](https://openai.com/index/introducing-dots/)) 複数仕事を進行。([発表](https://openai.com/index/introducing-dots/)) 追加dotのチームは将来構想。([発表](https://openai.com/index/introducing-dots/)) | Web、ファイル、コード、接続アプリ、Work／Codex委任。([発表](https://openai.com/index/introducing-dots/)) 送信等は規則と審査で判断。([発表](https://openai.com/index/introducing-dots/)) |
| Grok Bot | 常時・routine、スケジュール・対応イベント。([FAQ](https://docs.x.ai/grok-bot/faq)) | 米国のユーザー単位microVM。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) 端末を閉じてもクラウド仕事は継続。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) ローカルコマンドは別許可。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) | 役割別Bot記憶。([FAQ](https://docs.x.ai/grok-bot/faq)) 一部個人情報・ファイル・ログインは共有。([FAQ](https://docs.x.ai/grok-bot/faq)) 複数Bot並列。([FAQ](https://docs.x.ai/grok-bot/faq)) | ブラウザ・端末・コネクタ。([セキュリティ](https://docs.x.ai/grok-bot/security)) 送信・購入等はAuto Reviewとルール次第。([セキュリティ](https://docs.x.ai/grok-bot/security)) |
| Claude Duet | 朝の要約、数時間おき確認、継続スレッド。([発表](https://claude.com/resources/articles/claude-duet)) 即時監視ではない。([発表](https://claude.com/resources/articles/claude-duet)) | クラウドPC・別クラウドブラウザ。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 端末オフでも継続。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 現行ブラウザは直接閲覧・引継ぎ不可。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | Claude記憶・skills・接続を継承。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 並列数未公表。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 調査・資料・業務アプリ。([発表](https://claude.com/resources/articles/claude-duet)) 送信、支払、署名、削除は承認設計。([発表](https://claude.com/resources/articles/claude-duet)) 証券取引等は禁止。([発表](https://claude.com/resources/articles/claude-duet)) |
| Cue | 定期・対応イベント、エージェント間引継ぎ。([ストア](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)、[発表](https://manus.im/blog/introducing-manus-2-0)) | 独自PCを持つ設計。([発表](https://manus.im/blog/introducing-manus-2-0)、[ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)) ただし付帯条件・停止時の挙動・SLA未確認。([発表](https://manus.im/blog/introducing-manus-2-0)、[ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)) Manus本体のCloud Computerと区別。([発表](https://manus.im/blog/introducing-manus-2-0)、[ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)) | Memory and Dream。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[発表](https://manus.im/blog/introducing-manus-2-0)) 複数エージェントのグループ。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[発表](https://manus.im/blog/introducing-manus-2-0)) | 独自メール・電話・wallet、旅行比較・注文・支払。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) 実際の対象店舗等は未確認。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) |
| Muse | アプリを閉じても継続、予定・目標・定期作業、変化の通知。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)) | 個人ごとに隔離したSecure VM。([発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)) Sentinelが外部アクセスを審査。([発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)) | Memory等を閲覧・編集可。([データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)) 複数の独立エージェント編成は取得資料で未確認。([データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)) | ブラウザ、ファイル、Gmail・予定等。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[承認設定](https://www.meta.com/help/superintelligence/1385290430137537/)) 送信・予約・購入は許可設定に従う。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[承認設定](https://www.meta.com/help/superintelligence/1385290430137537/)) |
| Teammates | 担当役割を維持、監視・定期・変化への対応、他agentを起動。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | 各agentに独立computer・browser。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)) クラウド継続型の説明。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)) Mac完全ローカルComputerとは別。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)) | Computerの記憶・Project・skillsを活用。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 分業・相互連絡。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | Slack、GitHub、Gmail等、desktop/browser/code。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) PRやチケット操作例あり。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 全操作一律承認の保証は未確認。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) |

### 監督と適性

| 製品 | 承認・記録・停止 | 個人／共有／組織への適性判断 | 最大の注意点 |
|---|---|---|---|
| dots | Custom rules、Activity、Pause、接続撤回。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 別Work／Codex・独立予定は別停止。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | 個人・組織プランあり。([発表](https://openai.com/index/introducing-dots/)) specialist dotsは企業pilotで別物。([発表](https://openai.com/index/introducing-dots/)) | 接続解除で既存記憶は消えない。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 1体の停止が全委任処理の停止ではない。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) |
| Grok Bot | Ask first等。([セキュリティ](https://docs.x.ai/grok-bot/security)) Enterpriseはaction recording・network policy。([セキュリティ](https://docs.x.ai/grok-bot/security)) Bot削除で共有diskは消えない。([セキュリティ](https://docs.x.ai/grok-bot/security)) | 個人・Teams・Enterprise。([FAQ](https://docs.x.ai/grok-bot/faq)) ただしBot間は権限境界でない。([FAQ](https://docs.x.ai/grok-bot/faq)) | 使用枠非数値・自動追加課金・共有ログイン。([FAQ](https://docs.x.ai/grok-bot/faq)) モデル選択不可。([FAQ](https://docs.x.ai/grok-bot/faq)) |
| Claude Duet | 送信等の承認、Tasksで確認、接続解除。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) ブラウザ直接引継ぎ不可。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 現行は個人米国プレビュー。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) Team／Enterprise不可。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | バックグラウンド処理も通常Claudeの枠を消費。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) |
| Cue | アプリ権限と購入確認あり。([ストア](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) 統一停止・詳細監査仕様は未確認。([ストア](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) | 個人用のチーム。([発表](https://manus.im/blog/introducing-manus-2-0)) 組織のIAM・監査機能と同一視しない。([発表](https://manus.im/blog/introducing-manus-2-0)) | 電話・wallet・PCの条件、Cue固有料金とデータ保持範囲が不透明。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[削除ヘルプ](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account)) |
| Muse | Always ask、action別許可、Activity log、接続撤回・Reset。([承認設定](https://www.meta.com/help/superintelligence/1385290430137537/)) 送信済みメールは戻せない。([承認設定](https://www.meta.com/help/superintelligence/1385290430137537/)) | 個人秘書向き。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) 日本提供と職場契約適合は別判定。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) | 学習利用設定は初回オン。([プライバシー](https://muse.ai/privacy)) Confidential VMは現行Secure VMとは別の予定機能。([プライバシー](https://muse.ai/privacy)) |
| Teammates | threadで仕事確認、desktop引継ぎ、既存plugin／Project権限。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 統一停止や詳細承認仕様は追加確認。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | 個人Maxで複数役割を持つ用途。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 共有threadは他者読取専用、Slackで協働可。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | プレビュー、月額と稼働creditsは別。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) Enterprise Maxでも自動付帯しない。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) |

## 各製品の詳細

### dots：OpenAI

- **概要：** 公式名称は小文字の「dots」、一体は「dot」。([発表](https://openai.com/index/introducing-dots/)) 9月29日発表で、個人のprimary dotと、企業内で固有ID・資格情報・専用責任を持つspecialist dotsは区別され、後者は限定企業pilotである。([発表](https://openai.com/index/introducing-dots/))
- **使い始め方：** 対象Proは18歳以上で、EEA・英国・スイスを除く市場に段階配信されるため、日本は地域条件上の候補だが、アカウントへの到達は別確認となる。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 現行ヘルプでは最新iOS／Android、デスクトップアプリ、desktop Webから作成でき、名前を付けて必要なPluginsだけ接続する。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 初回はdesktop限定とする発表時の案内より、このヘルプを優先する。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **料金と制限：** Pro 100／200／500は100／200／500 USD/月で年払いなし、最初のdotは対象Pro・Business Premiumに含まれるが、具体的なdot作業量は確認資料に数値なし。([Pro料金](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) Work／Codexへ委任した仕事は通常の枠・料金を別途使い、Enterpriseの11月4〜18日無料プレビューと11月18日課金開始は、個人Proの無料試用を意味しない。([Pro料金](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)、[発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **仕事の進め方：** 複数プロジェクトを継続し、定期確認やリマインドを設定でき、In progress／Scheduled／Completedで状況を確認する。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 自発的なproactive researchは接続済みアプリの読取専用ツールに限定され、送信・書換・ブラウザ操作を自発的研究の範囲で行う仕様ではない。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **作業環境・操作：** 独自クラウドPCとブラウザを使い、利用者はそのPCを開いて確認できる。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) ローカルPCアクセスは任意・初期オフで、desktop appからAllow accessするとファイル操作やローカルbrowserの利用が可能になり、Codex cloud environmentを使わせるには事前作成が必要である。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **記憶と個別最適化：** ChatGPT Memoryを出発点に、dot独自の記憶も作るため、共有Memory設定変更とdotが既に保存した内容の削除は同じではない。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) アプリ接続解除は既取得情報を消さず、dot削除は独自記憶の削除を開始するが、作成済みWork／Codex会話は残り、主会話はarchiveされる。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **連携：** 公式発表は4,000超のアプリに接続するplugin ecosystemとSlack・Teamsを説明し、現行ヘルプはChatGPT側のPlugins設定を共有するとしている。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 個別Gmail／Drive／GitHub等の利用可否・読取／書込scopeは接続時の画面で確かめる必要があり、数字は同じ権限で4,000アプリを操作できる保証ではない。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **人間の監督：** Custom rulesには「確認せず実行」「事前承認なら実行」「毎回確認」「本人へ引継ぎ」の区分があり、「下書きして」は送信許可にならない。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) Pause・Revoke access・Deleteがあるが、別Work／Codexや独立scheduled taskは別に停止する必要があり、password変更等は本人に残される。([現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **現実的な制約：** 追加dotのチームは発表時に将来像として説明されており、現行primary dotから無制限に固有dotを作れると解釈しない。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 米国Pro限定のtexting betaはiMessage／RCSで、SMS・group messaging非対応、Linq経由のためdotまでのend-to-end暗号化ではなく、日本からの通常利用と分ける。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))
- **情報の確度：** 11月8日確認、発表9月29日、発表記事に11月3日更新あり。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 日本語での個別機能品質、dot専用枠の数値、障害後の自動再開保証、全データの保持完了期限は未確認で、Enterprise等のGA表記と11月18日までの管理者有効化条件を併記する。([発表](https://openai.com/index/introducing-dots/)、[現行ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))

個人プランは学習利用を制御でき、Business／Enterprise／Eduは既定で学習対象にしないが、proactive researchやdotの内部notesが直接学習されないことと、それを使った適格会話・タスクが設定に応じて利用されることは区別されている。([OpenAI発表](https://openai.com/index/introducing-dots/)) 組織での試行は、ユーザー単位の有効化だけでなく、接続アプリと別委任タスクの監督も設計する。([OpenAI発表](https://openai.com/index/introducing-dots/))

### Grok Bot：xAI系、Cursorのアカウント・クラウド基盤

- **概要：** 正式名称はGrok Botで、8月11日にalways-on agentsとしてベータ発表された。([発表](https://x.ai/news/introducing-grok-bot)、[セキュリティ](https://docs.x.ai/grok-bot/security)、[Cursor公式発表](https://cursor.com/blog/joining-spacex)) 現行セキュリティ文書ではCursor server・accountを使い、first-party SpaceXSIまたは第三者モデルを選ぶ構成で、Cursorは8月14日にSpaceXによる買収完了を公式発表している。([発表](https://x.ai/news/introducing-grok-bot)、[セキュリティ](https://docs.x.ai/grok-bot/security)、[Cursor公式発表](https://cursor.com/blog/joining-spacex))
- **使い始め方：** 現行の新規契約はThe X SubscriptionのPremium／Super／Ultra、既存はCursor・SuperGrok等のlegacy条件もあるため、先に自分の契約経路を確認する。([FAQ](https://docs.x.ai/grok-bot/faq)) FAQはmacOS／Windows／Linux、iOS 18+／iPadOS 18+／Android 9+を案内するが、日本向けBot資格と日本語個別対応は今回未確定で、通常GrokやXの利用可能国からBotの可否を代用しない。([FAQ](https://docs.x.ai/grok-bot/faq)) Bot固有の契約上の年齢条件は未確認であり、OS versionの「18+」を利用年齢と混同しない。
- **料金と制限：** 製品ページはPremium $30、Super $100、Ultra $200の月払いを表示し、新体系ではGrok／Cursorとの週次pool、legacyでは別メーターという違いがある。([製品ページ](https://x.ai/bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) 枠の絶対数・リセット曜日時刻は未公表で、追加credits／on-demandの有効化、月額上限、Auto Top-upを確認する必要があり、月額上限は進行中タスクにより多少超える場合がある。([製品ページ](https://x.ai/bot)、[FAQ](https://docs.x.ai/grok-bot/faq))
- **仕事の進め方：** 役割別Botsを作り、グループ内で文脈や作業を引き継ぎ、routineを時刻や対応イベントで動かす。([発表](https://x.ai/news/introducing-grok-bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) 教えたブラウザ作業からdraft skillを作るTeach a taskは段階提供の場合があり、記録は10分以内、無人開始の承認は約30分で期限切れになる。([発表](https://x.ai/news/introducing-grok-bot)、[FAQ](https://docs.x.ai/grok-bot/faq))
- **作業環境・操作：** 米国のmember単位microVMで、同一アカウントの全Botが永続disk・files・browser session・loginを共有する。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) 各Botの画面でcomputer-useを並行できるが、ローカルcommand executionは別許可で既定は毎回確認、on-premises・顧客imageへの配置は非対応である。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security))
- **記憶と個別最適化：** Bot別の好み・役割・作業要約と、名前・timezone等の共通情報があり、「What do you remember about me?」で確認できる。([FAQ](https://docs.x.ai/grok-bot/faq)) Bot削除はプロフィール・会話・routineを消すが共有PC内のfilesやloginは残り得るため、Botを削除しただけで機密データを消去したと扱わない。([FAQ](https://docs.x.ai/grok-bot/faq))
- **連携：** Slack、Google Workspace、GitHub、Microsoft 365等がセキュリティ文書に挙がり、OAuth tokenはBotへ渡さずserver側で保持する構成である。([セキュリティ](https://docs.x.ai/grok-bot/security)、[FAQ](https://docs.x.ai/grok-bot/faq)) 専用connectorのないサイトはbrowser操作できる場合があるが、appごとのread/write一覧は今回取得資料で確認できず、connectorを優先することが公式に勧められている。([セキュリティ](https://docs.x.ai/grok-bot/security)、[FAQ](https://docs.x.ai/grok-bot/faq))
- **人間の監督：** Allow once／Always allow／DenyとAsk first等のAuto Reviewルールがあり、Enterpriseは強制ルール・network allowlistを設定できる。([セキュリティ](https://docs.x.ai/grok-bot/security)) Action RecordingはEnterprise限定・初期オフで90日保持、admin terminationはrunning Botを止めてもdurable diskを保持し、アカウントアクセス撤回とは別になる。([セキュリティ](https://docs.x.ai/grok-bot/security))
- **現実的な制約：** Bot間はセキュリティ境界ではなく、モデルを選べず、チームのmodel allowlistもBotには適用されない。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) サイトによるcloud traffic拒否、CAPTCHA、再ログインで本人への引継ぎがあり、無人承認の期限切れも長時間処理の中断要因となる。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security))
- **情報の確度：** 11月8日確認、FAQは10月29日、securityは11月6日更新。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) 発表時のSuperGrok／Cursor別枠と現行The X Subscription共通poolを混在させず、新旧契約・個人／teamの適用をアカウントで確定させる。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security))

無料試用は、Start Trialが出るアカウントの7日間・使用credits型と、Appleが管理する有料自動移行のストア試用を区別する必要がある。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security)) Privacy Mode有効時は学習対象外とする現行security説明がある一方、Legacy Privacy Modeは非対応なので、モード名だけで適合を判断しない。([FAQ](https://docs.x.ai/grok-bot/faq)、[セキュリティ](https://docs.x.ai/grok-bot/security))

### Claude Duet：Anthropic

- **概要：** Claude Duetは10月21日発表のproactive agentアプリで、米国Pro／Max／Ultra対象のウェイトリスト付きresearch previewである。([発表](https://claude.com/resources/articles/claude-duet)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) Team／Enterpriseはまだ対象外で、将来提供の予定と現在の組織利用可否を分ける。([発表](https://claude.com/resources/articles/claude-duet)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet))
- **使い始め方：** 米国のClaudeアカウントと対応有料プランを用意し、waitlistの招待を受け、指定メールと同じアカウントで独立iOS／AndroidアプリまたはWebを使う。([発表](https://claude.com/resources/articles/claude-duet)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 招待はwave配信で日付保証なし、日本在住者の正規利用候補には現時点で含めず、年齢・日本語保証範囲はDuet固有資料では未確認とする。([発表](https://claude.com/resources/articles/claude-duet)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet))
- **料金と制限：** preview中は追加料金なしで、Claudeの通常枠を朝のbriefや背景checkも消費する。([料金](https://claude.com/pricing)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) 料金表はPro月$20／年$200、Max月$100、Ultra月$200で、Duetヘルプは5時間・週次枠の共有とpreview用reset（Pro3回、Max／Ultra1回、未使用分12月15日失効）を案内するが、Ultra認証済みアカウントの5時間枠は料金表に例外がある。([料金](https://claude.com/pricing)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet))
- **仕事の進め方：** 一つの継続threadと話題別channel、朝のbrief、数時間おきの接続app確認、仕事完了・判断待ちの通知がある。([発表](https://claude.com/resources/articles/claude-duet)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) Tasksで進行・要入力を見て、Makeで成果物を扱い、完了提案が出ても本人がcompletedを確定する設計で、リアルタイムの緊急監視としては扱わない。([発表](https://claude.com/resources/articles/claude-duet)、[ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet))
- **作業環境・操作：** 自前cloud computerで働き、別cloud browserを固定commandで操作するため端末オフでも継続できるが、ユーザーはbrowserを見たりtake overしたりできない。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) ローカルPCの全filesや全Projectsへのアクセスはなく、Claude内の仕事は読めても変更できず、現行ヘルプはOpus 5.5固定・モデル選択不可としている。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security))
- **記憶と個別最適化：** 既存Claude memory・skills・connectorsを引継ぎ、project外のClaude会話等を検索できるが、Search and reference chats設定で停止できる。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) app解除後も既習情報はmemory resetまで残り、履歴削除、memory reset、account削除はそれぞれ別の操作である。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security))
- **連携：** Gmail、Google Calendar／Drive、Slack、QuickBooks、HubSpot、Docusign、Calendly等を案内し、Microsoft 365は現行未提供とされる。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[発表](https://claude.com/resources/articles/claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) Link・Shop PayはDuet内で接続する購入手段でStripe connectorとは別、1Password連携は発表・安全性記事ではcoming soonであり、提供済みと断定しない。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[発表](https://claude.com/resources/articles/claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security))
- **人間の監督：** メッセージ送信、支払、署名、削除の前に宛先・内容等を提示して承認を待つ設計で、支払等には省略できない確認もある。([発表](https://claude.com/resources/articles/claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) 証券取引や口座間送金は承認があっても不可で、outgoing messageの別classifierは資格情報・完全なカード番号・政府ID等の外部送信を止める仕組みである。([発表](https://claude.com/resources/articles/claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security))
- **現実的な制約：** 仕事中心に設計され、個人のticket予約等は強くないという公式の留保があり、大手サイトがDuetをblockすることも認められている。([発表](https://claude.com/resources/articles/claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)、[実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) 実践レビューにはMP3を文字起こしできず別手段のtranscriptを求めた例、接続Gmailが意図と違う例があり、approval flowや継続稼働のすべてが独立検証済みではない。([発表](https://claude.com/resources/articles/claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)、[実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/))
- **情報の確度：** 11月8日確認、発表10月21日、安全性記事10月23日。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) 定量的な同時タスク上限、Duet独自の保持期限・保存region、統一pauseの挙動は未確認であり、preview対象プランの現行表記は古いPro／Maxのみの記事より公式ヘルプを優先する。([ヘルプ](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security))

個人向けClaude料金表の学習利用はopt-out型であり、Duetの「資格情報をモデルに見せない」「独立classifierがある」ことは、個人契約のデータ利用条件や組織契約への適合を置き換えない。([Claude料金・データ比較](https://claude.com/pricing)、[Duet安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) Duet固有の保存期間が取れないため、非公開業務データを接続する判断には追加の契約確認が必要である。([Claude料金・データ比較](https://claude.com/pricing)、[Duet安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security))

### Cue by Manus：Butterfly Effect

- **概要：** 現行ストアの正式名は「Cue by Manus」、発表本文では「Cue」。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Manus発表](https://manus.im/blog/introducing-manus-2-0)、[独立運営再開](https://manus.im/blog/manus-resumes-independent-operations)、[日付付き記事一覧](https://manus.im/blog)) 9月28日のManus 2.0で紹介されたstandalone appで、sellerはBUTTERFLY EFFECT PTE. LTD.、Manusは9月1日に独立運営再開を公式発表しているため、現状を単に「MetaのCue」と記載しない。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Manus発表](https://manus.im/blog/introducing-manus-2-0)、[独立運営再開](https://manus.im/blog/manus-resumes-independent-operations)、[日付付き記事一覧](https://manus.im/blog))
- **使い始め方：** Manus sidebarのAgents (Cue!)からQRでappを取得し、ログイン後にinvitation codeを入力する案内がある。([公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) 現行iOS・Google Play掲載を確認し、iOSは18.0+、App Store表示言語に日本語が含まれるが、日本ストアの配信・地域資格・招待入手は未確定、ストアの13+評価を契約上の年齢条件と同一視しない。([公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB))
- **料金と制限：** early accessは招待コード付き無料、現行storeはアクセス後Plus membership無料とする一方、米国App Storeには電話番号$9.99、Cue Pro $100、Cue Max $200、Cloud Computer $39等の購入項目がある。([発表](https://manus.im/blog/introducing-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) これらの請求周期・適用対象・税・含む枠は掲載から確定できず、月額定価や全機能無料と読み替えず、Manus本体のPro料金も代用しない。([発表](https://manus.im/blog/introducing-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358))
- **仕事の進め方：** 自分用agentを一体または複数作り、group chatでgoalを共有して仕事を引き継ぐ。([Manus発表](https://manus.im/blog/introducing-manus-2-0)、[公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) Scheduled Automationと対応event／conditionへの反応は公式store・helpにあるが、稼働頻度、無人承認timeout、失敗後の自動再実行、並列数の確定仕様は未確認である。([Manus発表](https://manus.im/blog/introducing-manus-2-0)、[公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB))
- **作業環境・操作：** agentにemail・phone number・wallet・computerという独自identityを持たせる設計で、旅行・商品比較、確認後の予約・注文・支払、対応店舗のQRから専用Cueを作る用途が説明される。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)) Manus StudioのローカルComputer Useや、server用途の有料Cloud Computerは関連機能だが、Cue全員のPC仕様・料金・availabilityと同一ではない。([ストア](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[公式ヘルプ](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0))
- **記憶と個別最適化：** 「Memory and Dream」が食事の好み、旅行習慣、学習進捗、継続計画を保持すると説明する。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[削除ヘルプ](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account)) CueとManusはaccount・dataを共有し、Cueだけのaccount削除は現行非対応で、Manus account削除は両方に適用されるため、試用用の分離アカウントを考える意味がある。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[削除ヘルプ](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account))
- **連携：** 公式storeはemail／calendar／messaging servicesを挙げるが、Gmail・Notion等のCue固有connector、MCP対応、app別read/write一覧を確定できない。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) 独自電話番号があることと日本の店へ確実に電話予約できること、QR対応があることと任意の飲食店を使えることを分ける。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB))
- **人間の監督：** ユーザーがappとpermissionを選び変更でき、予約・order・paymentは確認後に完了するというstore説明を確認した。([Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)) メール送信・ファイル削除を含む統一approval matrix、すべてのagentの緊急停止、操作履歴の保持・exportは未確認なので、初回はwallet・電話・送信権限を有効化しない運用を推奨する。([Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB))
- **現実的な制約：** 発表時の「iOSは審査後」と、現行iOS掲載は時点差で説明できる一方、店舗・国・電話・walletの実運用は独立した実践根拠が不足する。([発表](https://manus.im/blog/introducing-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Manus privacy](https://manus.im/privacy)) Manus一般privacyはBrowser sandbox保持7日／21日を記すが、これをCueの永続computerやmemory全体の保持期間として転記しない。([発表](https://manus.im/blog/introducing-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Manus privacy](https://manus.im/privacy))
- **情報の確度：** 11月8日確認、9月28日の製品発表と11月7日更新Google Playを確認。([公式記事一覧](https://manus.im/blog)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) Cue固有料金の周期、個別memory削除、外部モデルへの送信条件、地域・年齢資格の完全な一覧は未確認である。([公式記事一覧](https://manus.im/blog)、[Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358))

Manus一般privacyは9月28日更新で、account削除後30日以内の削除に例外を設け、connector解除は会話・files・memoryの既存内容を消さないとしている。([Manus privacy](https://manus.im/privacy)) 非識別化等されたデータのmodel改善利用や米国等への移転もあるため、Cue固有の条件が不明な部分を「クラウドPCが隔離されているから私的」と補完してはならない。([Manus privacy](https://manus.im/privacy))

### Muse：Meta

- **概要：** 正式名はMuse、提供元Meta。([初回発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) 9月8日米国発表後、10月23日に日本提供開始が公式確認でき、個人の日常用件から継続目標まで扱うagentとして位置付けられる。([初回発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/))
- **使い始め方：** iOS・Android・muse.aiでMeta accountを使い、Facebook／Instagram連携またはemail／phoneでaccountを作る。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[開始ヘルプ](https://www.meta.com/help/superintelligence/1331373868832401/)、[privacy](https://muse.ai/privacy)) 既存Meta accountとのAccounts Center共有を避ける選択もprivacyに記載されるが、全機能の日本語保証は取得資料で未確定、voice／avatarは国別・英語限定表示等を別確認する。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[開始ヘルプ](https://www.meta.com/help/superintelligence/1331373868832401/)、[privacy](https://muse.ai/privacy)) 年齢は有料subscriptionで後述の成年条件を確認できる一方、無料枠の最低年齢は本調査で確定していない。
- **料金と制限：** 無料は使用量制限付きで数値未公表、Power $20/月で週500M Muse tokens、Maximum $100/月で週3B、月次自動更新である。([料金ヘルプ](https://www.meta.com/help/subscriptions/1021145227643680/)) subscriptionは18歳または居住国の成年要件と対象国を満たす必要があり、円建て定価・税・週reset時刻・tokenの内部計量方法は公式資料から確定できない。([料金ヘルプ](https://www.meta.com/help/subscriptions/1021145227643680/))
- **仕事の進め方：** appを閉じても作業を続け、状況変化・承認待ちで連絡し、Goalsで目標、Upcomingで予定taskやreminderを管理する。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)、[privacy](https://muse.ai/privacy)) calendar connectorが変更を自発的に受け取る場合は接続前に示されるが、全connectorが即時event-drivenとする仕様ではない。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)、[privacy](https://muse.ai/privacy))
- **作業環境・操作：** 個人ごとのMuse Secure VMにdata・credentialsを保持し、systemレベルで隔離されたSentinelがinternetへ出るactionを審査する。([初回発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[privacy](https://muse.ai/privacy)) browser・form・旅行予約・email等を説明するが、MetaもアクセスできないとするMuse Confidential VMは将来機能であり、現行Secure VMと同じ保証ではない。([初回発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[privacy](https://muse.ai/privacy))
- **記憶と個別最適化：** Memory、Soul、Identityやsystem filesを閲覧・編集し、forget skillで特定人物・topicの記憶削除を依頼できる。([データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)、[privacy](https://muse.ai/privacy)) message・file削除で学んだ内容が必ず消えるわけではなく、forgetも「best of its ability」で、Reset Museはhistory・files・active tasksを含む全情報の不可逆削除操作である。([データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)、[privacy](https://muse.ai/privacy))
- **連携：** 日本発表はGmail、Google Calendar、Instagram、Stripe、Shopify、Trip.com、Agoda、Klook等を挙げる。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) メルカリ、マネーフォワード ME、チケットぴあは連携を進める予定として扱い、現行の利用可能connector一覧にそのまま追加しない。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/))
- **人間の監督：** Settings → Permissionsでconnector・WebのAlways ask等を選び、Allow once／for this task／for this site／Always allowの範囲を指定できる。([承認ヘルプ](https://www.meta.com/help/superintelligence/1385290430137537/)) Activity logとUpcomingで確認し、chatで止められる作業もあるが、送信済みemail等は取り消せず、site単位の恒久許可は将来の作用範囲を広げる。([承認ヘルプ](https://www.meta.com/help/superintelligence/1385290430137537/))
- **現実的な制約：** 無料枠でも継続監視の頻度を上げれば上限に達し得るが、公開された利用者の使用率から他人のtask件数や実費を予測できない。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)、[privacy](https://muse.ai/privacy)、[日本の利用報告](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e)) 副chat削除とmemory削除、connector解除と既存data削除、Meta広告への非共有とAI学習非利用もそれぞれ別である。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)、[privacy](https://muse.ai/privacy)、[日本の利用報告](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e))
- **情報の確度：** 11月8日確認、日本提供開始10月23日、privacyの発効日は9月17日。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[privacy](https://muse.ai/privacy)) 日本のvoice／avatar、連携予定の国内3社、Confidential VMの提供済み証拠、同時task上限、全backupを含む具体的保持期間は未確認である。([日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[privacy](https://muse.ai/privacy))

最初にSettings → Data controls → Help improve our AI modelsをオフにすることを推奨する。([データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)、[privacy](https://muse.ai/privacy)) privacyは初回オンとし、offへの変更が過去interactionにも適用されると記す一方、connector由来情報も学習設定の対象であり、広告systemに会話・VM dataを共有しないという説明だけでは学習不使用にならない。([データ管理](https://www.meta.com/help/superintelligence/2225571704857152/)、[privacy](https://muse.ai/privacy))

### Teammates：Perplexity

- **概要：** 公式製品ページは「Perplexity Teammates」、本文ではteammates／一体のteammateを使う。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[ブログ](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)、[ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 11月4日ブログ、11月6日changelogを確認でき、個人MaxのWeb research previewであり、一般提供済みの全組織機能と扱わない。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[ブログ](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)、[ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))
- **使い始め方：** 個人MaxでWebにsign inし、sidebarのTeammates → Create teammateから名前・role・appearance・初期task・scheduleを設定する。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Max billing](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)) 日本の除外国指定は取得資料にないが実際のsidebar表示を確認し、Webで契約したProをmobile経由で別契約へupgradeし二重契約を作らないようbilling経路も確認する。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Max billing](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)) Teammates固有の最低年齢は取得資料から確定していない。
- **料金と制限：** Maxは$200/月または$2,000/年、年払いの月換算は約$166.67で月払い価格ではない。([Max billing](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[製品ページ](https://www.perplexity.ai/hub/products/teammate)、[credits](https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity)) Teammatesは期間限定の無料usage特典後に既存Max creditsを使い、通常Maxは月10,000 credits、新規bonus35,000は約30日で失効、毎月枠はbilling日に更新・繰越なしで、promotionの期限・量は一律に確定できない。([Max billing](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[製品ページ](https://www.perplexity.ai/hub/products/teammate)、[credits](https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity))
- **仕事の進め方：** 役割を維持し、taskを分解して追加agentを立ち上げ、並列結果を確認し、変化に応じて方向修正してreviewへ返す。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) Slackや接続toolsを監視でき、同一Projectのteammatesはcontext・files・instructionsを共有し、連絡を取り合う。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))
- **作業環境・操作：** 各agentが独立computer・desktop・browserを持ち、connectorのないsiteも操作し、本人がtake overして方向修正できる。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)) 11月6日changelogの「Macで完全ローカルComputer」は別項目であり、Web Teammatesそのものが完全ローカルになる証拠には使わない。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode))
- **記憶と個別最適化：** Computerのskills・memory・Projects・過去仕事を使い、feedbackを次の作業に反映する。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[Maxヘルプ](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[データ収集ヘルプ](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)) Brainは活動を知識化し、Settings → Memoryでentryを確認・編集・削除でき、Brainの書いたmemoryはモデル学習対象にしないとのMaxヘルプがあるが、これを全会話の学習不使用と読み替えない。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[Maxヘルプ](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[データ収集ヘルプ](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity))
- **連携：** Slack、GitHub、Gmail、Linear、Datadog等の例があり、installed plugins・skillsの既存permissionsを引き継ぐ。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) GitHub接続では対象repositoryを選び、Slackはworkspace・channel・監視条件・報告先を指定するが、全connectorのread/write scopeは接続時のauthorizationと実際のtoolごとに確かめる。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))
- **人間の監督：** 一つの継続threadで進行を確認し、workのreview、desktop引継ぎ、指示変更ができ、保存credentialsは暗号化しagentが見えない形で入力される。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) Teammates専用の全action承認matrix、全派生taskを一括停止する確定手順、削除後の永続disk・logs保持は今回未確認で、外部送信を常に止める設定があると断定しない。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))
- **現実的な制約：** 多agent、大規模files／code、頻繁なautomationはcreditsを増やす場合があり、残高不足時は一般Computerの仕様でactive taskがpauseし、補充・月更新でresumeする。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[credits](https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity)) Enterprise Pro／Maxは初回launchに自動包含されず、共有chatは他者read-onlyで、同じroleを他人が自由に操作できるチームbotとは異なる。([ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[credits](https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity))
- **情報の確度：** 11月8日確認、初回ブログ11月4日、ヘルプ11月5日更新、changelog11月6日。([ブログ](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode)) 独立した長期実践、地域・日本語保証の一覧、agent数上限、promotion終了条件、Teammates専用監査・停止・export仕様は追加検証が必要である。([ブログ](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work)、[ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[変更履歴](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode))

一般PerplexityのAI Data Retentionは個人Free／Pro／Maxで初期有効とするヘルプがあり、設定でoffにできる。([データ収集ヘルプ](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) TeammatesがComputerの安全基盤を使うこと、各agentのbrowser cookieが分離されることと、既存の広いplugin権限・Project共有が自動的に縮小されることは別である。([データ収集ヘルプ](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)、[Teammatesヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))

### 追加比較：Tasks in Gemini（旧Gemini Spark）

現行公式ヘルプの名称は「Tasks in Gemini／Manage your tasks & workflows」で、5月発表のGemini Sparkと、単なる時刻指定のScheduled ActionsやGoogle TasksのToDoリストは区別する。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Spark発表](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)) 現在の入口はGemini mobile・Web・Macのtask機能で、個人Google account、18歳以上、Google AI Pro／Ultra、Keep Activity on、Personal Intelligence opt-inが必要であり、仕事・学校accountは現時点で対象外である。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Spark発表](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/))

- **アクセスと料金：** 対象国はGemini提供国からEEA・Nigeria・Swiss・UKを除くとされ、日本はこの除外に入らない。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[日本料金](https://gemini.google/jp/subscriptions/?hl=ja)) 日本向けProは月2,900 JPY、Ultraは構成により月14,500／32,000 JPYの表示で、Tasks専用追加料金・確定task件数換算は未確認、無料・Plusだけで使えるとはしない。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[日本料金](https://gemini.google/jp/subscriptions/?hl=ja))
- **進め方と環境：** 最大15 task同時実行、時刻・eventのschedule、途中指示で進行更新、local Chrome auto browse・cloud remote browser・remote code実行がある。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) local Chromeは端末とChromeのawakeが必要で、remoteは端末を閉じても継続する一方、同じhelpにはdevice off時のschedule非実行記載もあり、「PCを閉じれば全定期taskが24/7動く」と包括保証しない。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop))
- **連携と監督：** Gmail・Calendar・Drive・Docs・Sheets・Slides・Keep・Tasks等の読取・作成・変更、local browserの既存loginを使う。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) 通信送信、変更・削除、購入、金融transaction、form提出等にconfirmationがあり、Stop response／Take control、Schedulesのpause、Browser dataとTask settingsのremote data削除が可能である。([現行ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop))
- **記憶・privacy・制約：** Personal Intelligenceと過去会話等を利用し、Activityの既定自動削除は18か月、人手reviewされた会話等はaccountから切り離して最大3年保持される場合がある。([Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB)) TasksはKeep Activity onを要求するため、履歴offで同じ運用ができると想定せず、local folders・remote browser cookie・task computer filesを別に管理する。([Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB))

採用価値はGoogle環境との近さにあるが、通常のGoogle Workspace組織契約への適用とは別判定になる。最初は公開情報＋手作業で渡した架空予定で試し、Chromeの普段のログインやDriveの広い権限を初日から渡さないことを推奨する。

### 追加比較：Copilot Cowork（個人用と組織用を分離）

Microsoftの現行概要はpersonalとwork／school両方を扱い、組織用は一般提供、個人用はpreviewとしている。([現行概要](https://learn.microsoft.com/en-us/copilot/cowork/)、[GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)) 6月16日の企業GA発表だけを見て「企業専用」、逆に個人previewだけを見て「すべて個人契約で企業監査対応」とは記載しない。([現行概要](https://learn.microsoft.com/en-us/copilot/cowork/)、[GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/))

- **アクセスと料金：** 個人向け米国ページはMicrosoft 365 Premium $19.99/月・$199.99/年、Pro $99.99/月、Premiumの1か月trialを表示するが、取得時にmarket unavailable表示があり日本資格は確定できない。([個人向けページ](https://www.microsoft.com/en-us/copilot/work/individuals)、[企業GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)) 企業GA発表はMicrosoft 365 Copilot USLにusage-based Cowork料金を重ねるモデルを示すため、月額seatだけを総額としない。([個人向けページ](https://www.microsoft.com/en-us/copilot/work/individuals)、[企業GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/))
- **進め方と環境：** Web、Windows／macOS、iPhone／Androidに入口があり、scheduled prompt・email／Teams eventのtask、pause／resume／cancelに対応する。([現行概要](https://learn.microsoft.com/en-us/copilot/cowork/)、[GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[更新履歴](https://learn.microsoft.com/en-us/copilot/cowork/whats-new)) クラウドtaskはlaptop offでも継続するが、local Edge利用は端末・login条件の影響を受け、6月のFrontier記載より8月のGA移行履歴を優先する。([現行概要](https://learn.microsoft.com/en-us/copilot/cowork/)、[GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[更新履歴](https://learn.microsoft.com/en-us/copilot/cowork/whats-new))
- **連携と監督：** Outlookの送信・返信・整理、Teams投稿、OneDrive／SharePoint、Word／Excel／PowerPoint等を扱い、approval画面はrisk levelとSend／Post等のactionを表示する。([現行概要](https://learn.microsoft.com/en-us/copilot/cowork/)) 一部類似操作の以後確認を省略する選択があり、最大50 custom skills、plugin追加、過去chat／taskをcontextに選ぶ機能がある。([現行概要](https://learn.microsoft.com/en-us/copilot/cowork/))
- **組織適性と限界：** 企業GAはaudit log、eDiscovery、DSPM、IRMs等の管理基盤とtenant／group／user予算・alertを説明する。([GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)) DLPはその6月発表ではcoming soonなので、11月時点の全対応を当該記事だけで保証せず、自治体はtenant契約・region・監査・label・data境界を別途照合する。([GA発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/))

Microsoft 365中心の組織には検討価値があるが、既存文書への過剰共有もWork IQ経由で可視化され得る範囲として点検したい。試行は公開情報を置く専用領域で行い、送信・削除・共有link作成を本人承認に固定する運用案とする。

### 追加比較：OpenClaw

OpenClawはOpenClaw Foundationが独立してstewardするMITのself-host型で、Foundationは有料tier・hosted service・tokenを売らないと説明する。([公式説明](https://docs.openclaw.ai/start/why-openclaw)) Gatewayを自分のPC／serverで動かすため、software無償と、model API・server・保守の費用ゼロは別であり、旧称の詳細な改称履歴は今回一次確認を完了していない。([公式説明](https://docs.openclaw.ai/start/why-openclaw))

- **開始・環境：** 公式Getting startedでruntime・onboarding・provider設定を行い、background Gatewayを維持する。([開始ガイド](https://docs.openclaw.ai/start/getting-started)、[個人秘書設定](https://docs.openclaw.ai/start/openclaw)) macOS／Linux／Windows系の導入経路があり、手元PCを落とせばそこでの処理は止まるため、24時間用途は常時server等を別に用意する。([開始ガイド](https://docs.openclaw.ai/start/getting-started)、[個人秘書設定](https://docs.openclaw.ai/start/openclaw))
- **継続仕事・連携：** WhatsApp、Telegram、Slack、Teams、Signal等をGatewayで接続し、proactive checkやautomationを利用する。([個人秘書設定](https://docs.openclaw.ai/start/openclaw)) 専用WhatsApp番号とallowFrom設定を勧める公式個人設定は、日常の全messageを無差別にagent入力にしないための具体的な注意になる。([個人秘書設定](https://docs.openclaw.ai/start/openclaw))
- **監督とprivacy：** sandboxは既定offで、trusted single operator前提、敵対的な複数利用者の境界ではない。([公式説明](https://docs.openclaw.ai/start/why-openclaw)、[公式security policy](https://github.com/openclaw/openclaw/security)) sandbox.mode all、workspace read-only、tool policy、networkを個別に設計し、native pluginsはin-processでsandbox外であることを踏まえ、model providerやchannelへの送信条件は別々に確認する。([公式説明](https://docs.openclaw.ai/start/why-openclaw)、[公式security policy](https://github.com/openclaw/openclaw/security))

技術検証・個人開発者向けの候補だが、閉域・自治体向けというだけで安全な完成品にはならない。更新適用、秘密管理、backup、job停止、ログ削除まで自分が運用責任を持てる場合に限定して試すことを推奨する。

### 追加比較：Hermes Agent

Nous ResearchのHermes Agentはself-improving agentとして、作業からskillsを作り、preferences・projects等を保持する設計を公式に説明する。([公式ドキュメント](https://hermes-agent.nousresearch.com/docs)) CLIだけでなくdesktop、messaging gateway、named Bots等の入口があるが、提供国・日本語UI保証や利用する外部modelの地域条件は別途確認が必要である。([公式ドキュメント](https://hermes-agent.nousresearch.com/docs))

- **開始・費用：** 公式installerとsetupでprovider・gatewayを設定し、自分のhostまたは対応remote backendを使う。([公式ドキュメント](https://hermes-agent.nousresearch.com/docs)、[DreamHostの構成検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/)) softwareはMIT・無料とする比較検証があるが、modelとhosting費用は別であり、月数ドルのVPS例を実際の総費用や十分な構成と保証しない。([公式ドキュメント](https://hermes-agent.nousresearch.com/docs)、[DreamHostの構成検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/))
- **継続・記憶：** 経験からskillを生成し、継続memory・profile・botの設定を持つ。([公式ドキュメント](https://hermes-agent.nousresearch.com/docs)、[cron公式文書](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)) cron機能は定期・対応event等の仕事に使えるが、設置先の稼働とprovider利用枠が前提で、完全local privacyを意味しない。([公式ドキュメント](https://hermes-agent.nousresearch.com/docs)、[cron公式文書](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron))
- **監督・安全性：** 現行securityは危険command確認smartを既定とし、manual／offも設定可能、unattended／cronは既定deny、未回答はdenyとする。([公式security](https://hermes-agent.nousresearch.com/docs/user-guide/security)) MCP spend_limitはYOLOでもconfirmation対象だが、container backendではcontainerを境界としてcommand確認を省く構成があり、環境変数やcredential filesを渡しすぎないことが重要である。([公式security](https://hermes-agent.nousresearch.com/docs/user-guide/security))

OpenClawとの比較では、自分のchat接続とGateway運用を重視するか、skillsと学習ループを重視するかを検討軸にする。既定設定の安全性や一回の移行成功だけから、実業務の正確性に順位を付けることはできない。

### 追加比較：Hark Pro

Hark ProはHarkの継続chatとcloud Handoffによる個人秘書で、公式発表はiOS／Android／Webでfree to everyoneとするが、国別資格表は取得資料にない。([発表](https://hark.com/articles/introducing-hark-pro)、[利用ガイド](https://hark.com/using-hark)) 発表本文の日付は「OCT 06」で年は未記載のため、厳密な発表年は未確認とする。([発表](https://hark.com/articles/introducing-hark-pro)、[利用ガイド](https://hark.com/using-hark)) 公式の使用ガイドはHomeのAction Cards／Panels、Chat、Projectsという構成を説明し、日本向け利用可否・日本語・年齢資格は未確定である。([発表](https://hark.com/articles/introducing-hark-pro)、[利用ガイド](https://hark.com/using-hark))

- **費用と仕事：** 全機能の制限付き無料、Hark Pro²は$20/月で2倍、Pro³は$100/月で10倍のusageだが、絶対枠・resetは未公表である。([料金](https://hark.com/pricing/)、[利用ガイド](https://hark.com/using-hark)) scheduled tasks、Google Workspace／Microsoft 365、website Handoff、覚えたSpecialtiesを使い、食料注文・予定・docs等を扱うとする。([料金](https://hark.com/pricing/)、[利用ガイド](https://hark.com/using-hark))
- **記憶・credentials：** 会話をmemoryとして使いforget依頼が可能で、Secured by Hark vaultはpassword／cardを暗号化し必要siteでのみ復元する説明である。([利用ガイド](https://hark.com/using-hark)) Action Buttonによる実行は説明されるが、全対外actionのapproval matrix・一括停止・全historyのexportは本調査未確認である。([利用ガイド](https://hark.com/using-hark))
- **privacyの特長と留保：** 11月5日privacyはAccount Information／Inputs／Outputs／Memory／Connectors／Sandbox Dataをmodel学習に使わず、明示送信Feedbackは例外とする。([privacy](https://hark.com/privacy-policy)) 削除はactive systems30日・backup90日が原則で例外あり、EEA／UK／SwissはMemory非提供とされるため、地域差を含む現行条件を読む必要がある。([privacy](https://hark.com/privacy-policy))

無料・学習不使用の明示は比較価値があるが、日本での実際の入口、日常serviceへの適合、独立した長期実践の裏付けは不足する。既存の個人accountを広く接続せず、公開情報だけのHandoffが利用できるかから確認する候補とする。

### 追加比較：Instinct

Instinctの運営主体はSpear Street Technology, Inc. d/b/a Instinctで、公式homepageはtext／callで依頼し、電話・computerを使う個人秘書として説明する。([公式ページ](https://instinct.com/)、[規約](https://instinct.com/terms)、[privacy](https://instinct.com/privacy-policy)) 公開ページだけでは価格・招待の現行条件・日本提供・日本語・具体的hosting構成は確定できず、規約は18歳以上、米国運営、特定地域・deviceでのavailabilityを保証しないとする。([公式ページ](https://instinct.com/)、[規約](https://instinct.com/terms)、[privacy](https://instinct.com/privacy-policy))

- **委任権限：** 規約はconnected servicesとの情報交換・data index・本人代理の契約／transaction／第三者terms承諾を含め、結果が本人を拘束することを記す。([規約](https://instinct.com/terms)) safeguardやconfirmationがある場合でも誤操作防止を保証せず、全送信・支払の直前に必ず本人確認する製品と断定できない。([規約](https://instinct.com/terms))
- **privacy：** model trainingのprospective opt-outはあるが、safety reviewでflagされた情報の例外があり、Google Workspace APIから受けた情報には別の学習不使用制限がある。([privacy](https://instinct.com/privacy-policy)) integration解除は既存indexed dataを削除せず、workspaceでのdata削除・account操作を別に行う必要がある。([privacy](https://instinct.com/privacy-policy))
- **導入判断：** app設定や規約上の許諾が広く、public homepageだけでは実費・承認・緊急停止の具体手順が不足する。([規約](https://instinct.com/terms)、[privacy](https://instinct.com/privacy-policy)) 日本から直ちに試す第一候補にはせず、アクセス条件と権限の狭め方を確認できるまで、金融・医療・他人への連絡を委任しない方針を推奨する。([規約](https://instinct.com/terms)、[privacy](https://instinct.com/privacy-policy))

## 実際の活用事例・失敗例

### 根拠の読み方

本章の「結果」は記事執筆者の申告であり、本調査で同じアカウント・入力・実行時刻を再現した結果ではない。一次的な実践報告でも、単一利用者、短期間、更新前のバージョン、本人の採点、商業的利害による限界があるため、横断的な成功率には換算しない。

| ラベル | 意味 | 採用する範囲 |
|---|---|---|
| 開発元のデモ・製品例 | 公式が意図する使い方 | 設計・導入案の参考。稼働実績とはしない |
| 公式導入事例 | 開発元が紹介する顧客の報告 | 顧客名・条件が分かる範囲。第三者検証とは別 |
| 独立メディアの実践 | 記者が自身で使用 | 記事中の具体的な操作・観察結果 |
| 本人の実践報告 | ブログ・技術投稿など | 日時・設定・人間の介入が分かる部分 |
| 商業利害のある検証 | affiliate、販売事業者等 | 利害と測定条件を明記して限定採用 |
| 推測・紹介記事 | 実行の裏付けなし | 実績として採用しない |

### メール・予定・会議準備

**dots：清水理史氏が支払日の不一致を発見した例。**([PC Watch](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)) PC Watchの11月6日記事は、筆者が「アル」と名付けたdotにGmailとGoogle Calendarを接続した自身の使用報告である。([PC Watch](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)) dotはメール添付の発注書と請求書、過去の支払条件のメールを突き合わせ、支払日が一か月ずれていると、個別の誤り探しを頼まれる前に報告したという。([PC Watch](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)) 人間が最終的な契約・請求条件を確認する必要は残り、記事は相手への訂正連絡まで自動完了した証拠ではない。([PC Watch](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html))

- **自動化の範囲：** 複数文書と過去メールを継続的な文脈として照合し、異常候補を報告した段階である。([実践記事](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html))
- **人間の判断：** 原本、支払期日、相手への照会・訂正の要否を確認する。ここは本資料の導入時の検収提案である。
- **限界：** 一件の観察で検出率は測れず、請求・契約の自動修正や送金への委任を正当化しない。

**dots：迷惑メール内の重要通知と複数プロジェクトの追跡。** 同記事では、迷惑メールに入った漏えい通知をdotが拾い、受信20:30に対して20:32の報告という具体的な時刻が示される。([PC Watch](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)) 別の例では、Wi-Fiルーターの資料がある別Projectを確認し、動画用販売リストへの有線LAN速度情報の反映を他の会話に依頼し、途中の進捗も確認したとされる。([PC Watch](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html)) 二分という一回の通知時間をSLAや全通知の即時性に一般化せず、project横断アクセスは便利さと情報境界の両面で評価する。

**Claude Duet：Diana氏の会議準備と受信箱整理。**([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) AI Agents Libraryの10月28日公開・29日更新レビューは、筆者が自費のClaude Max 5xと招待で10月27〜28日に行った二日間の試行で、Anthropicによるスポンサー・事前確認なしと明記する。([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) Gmail、Calendar、Drive等を使い、放送予定であることまで考慮した準備briefと、過去七日分から返信が必要な項目だけを選ぶ受信箱整理を行った。([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) 受信箱を変更・送信しない指示で実行したところ、最初のGmailは自動メールが中心と判断して正しいaccountか質問し、人間がaccountを切り替える必要があった。([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/))

- **自動化の範囲：** スレッド既返信確認、優先順位付け、会議資料のまとめまでで、送信・受信箱変更はしていない。([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/))
- **人間の介入：** 対象Gmail account確認、既に処理した事項の確認、briefの読了と完了確定である。([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/))
- **再現性の限界：** 一度の主要試行が中心で、朝の能動brief、appを閉じた後の稼働、送信承認、購入、使用枠消費は検証していないと筆者が列挙する。([実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/))

**Muse：PRメールの見落としと返信追跡。**([Android Authority](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) Android AuthorityのStephen Radochia氏は10月6日の一週間実践でGmailを接続し、製品レビュー提供のPRメールを探すよう任せ、本人が見落としていた重要メールの発見と、その後の返信・先方の反応の追跡が役立ったと記している。([Android Authority](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) 本人が購入代行への抵抗感も述べ、実際の購入は試していないため、メール支援の成功を購入の信頼性に広げない。([Android Authority](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/))

### 長期調査・ニュース・価格監視

**Muse：eBayのヴィンテージ機器を一日二回監視。** 同じ記者はPalm PDAやApple PowerBookの検索を一日二回に設定したが、当初は状態が悪い品や好みと違う候補が含まれたと報告する。([Android Authority](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) 「新品箱入りか極上状態」「新着順」「Buy It Nowあり」と条件を明示した後、希望に沿う定期リストになったという。([Android Authority](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) 重要なのはagentの一般的な買い物能力ではなく、検索条件と除外基準を教えることで成果物が改善した点である。

**Muse：日本の個人開発者の継続jobと枠不足。**([Qiita投稿](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e)) 11月2日のQiita投稿は、予定確認とフリマ・オークション関連新着メール監視を画面を見ていない平日日中も動かし、無料枠の不足見込みから本人がPowerへ課金したとする記録である。([Qiita投稿](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e)) GPS利用ではphoneにpermission dialogが出て、本人が許可後に目的地案内へ使えたとも報告している。([Qiita投稿](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e)) ただし本文はMuseの運用記録から作成しClaude Codeで確認したと説明され、usageは実token数でなくpercentageで、job別の消費内訳は不明なので、独立した計測や一般料金の根拠にしない。([Qiita投稿](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e))

長期テーマの適切な成果物は「新情報を毎回大量に要約すること」ではなく、「前回からの変化、一次出典、意味のある差分、未確定事項、次の確認日」である。これは本資料の推奨設計であり、すべての製品が既定でこの形式を保証するという意味ではない。

### 個人開発・GitHub・複数エージェント

**dots／Teammates：Issue調査からPRは現時点で公式例中心。** dotsはfeedbackから修正をscopeし、実装・test・動画付きPRをreviewへ出す例を掲げ、TeammatesはSlack／Linear／Datadog／GitHubを使い不具合を調査し、PRを開いて自動checkやreviewへ反応する例を説明する。([dots公式例](https://openai.com/index/introducing-dots/)、[Teammates公式説明](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) 本調査では、これら六製品を同条件で複数repositoryのCI監視に使った独立した長期実測は確保していない。したがって「自動mergeまで安全に運用できる実績」ではなく、試用すべきworkflowの仮説として採用する。

**Grok Bot：Jonathan Montoya氏の役割分担。**([本人レビュー](https://jonathanmontoya.com/post/grok-bot-review)) 10月30日の本人レビューは、約25 Botsを自身の事業で使い、Chief of Staff、content、quality、research、finance、support等に分け、content Botのdraftをquality Botへ渡す運用を述べる。([本人レビュー](https://jonathanmontoya.com/post/grok-bot-review)) ただしaffiliate disclosureがあり、task logs・統制試験・定量時間削減は示されないため、多数Botの必要性や品質向上の定量証拠とはしない。([本人レビュー](https://jonathanmontoya.com/post/grok-bot-review)) 筆者は一つの地味な週次jobから始め、手動で三回試し、修正してskill化・routine化する方法を勧め、blocked sites、再login、CAPTCHA、曖昧な指示、Bot増加によるnoiseも挙げている。([本人レビュー](https://jonathanmontoya.com/post/grok-bot-review))

分業するなら、調査役はread-only、実装役はtest repositoryまたはbranch限定、検証役はtestと根拠照合、人間はmerge・release・公開を担当する設計を推奨する。同じ誤前提を引き継ぐだけの二重要約を「独立検証」と呼ばず、検証役は元資料・test結果を直接確認する。

### 旅行・買い物・生活・小規模事業

**Cueの店舗QR／電話／walletは公式デモ・仕様説明。** 公式掲載は、対応店のQRから専用Cueを作り、好みを踏まえてmenuを選び、本人のpayment confirmation後に注文を完了する例を挙げる。([公式App Store掲載](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) 今回、日本の特定店舗での予約・通話・決済を、設定から完了まで追える本人の実践報告は確保できなかった。店舗・service・payment・電話番号の条件が分からないまま「国内のどの店でも注文可能」とはしない。

**Duetのビジネス購入は承認設計の公式説明。** AnthropicはLinkによるmerchant・amountを限定したone-time cardと本人承認、Shop Payを説明するが、Diana氏の実践では購入承認自体を試していない。([公式安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)、[実践レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) 旅行予約・購入代行の試行では、候補比較と入力準備までをまず委任し、日付・氏名・取消条件・総額・通貨・決済前の最終画面を本人が検収する運用を推奨する。

**営業・問い合わせ・家族調整は現時点で導入案を中心に評価。** Teammates公式は顧客問い合わせ、停滞したsales、返金前確認、campaign運営等を、Muse公式は食事制限を記憶した招待や買い物、Hark公式は食料注文や予定等を挙げる。([Teammates公式](https://www.perplexity.ai/hub/products/teammate)、[Muse公式](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[Hark利用ガイド](https://hark.com/using-hark)) 本調査では家族間調整や日本の小規模事業で、当事者・許可範囲・実際の成果・失敗まで揃った検証を十分に確保していないため、宣伝用の例を導入実績には転記しない。初期試行はFAQ回答案、日程候補、買い物リストまでとし、家族や顧客への送信を本人確認に残す。

### うまくいかなかった例と、見かけの成功を避ける検収

| 事例・根拠の性質 | 実際の問題 | 人間の介入・結果 | 一般化しない点 |
|---|---|---|---|
| Duet、Diana氏の自費二日間検証 | DriveのMP3を見つけたが文字起こしできず。([レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) | NotebookLM／Gemini等でtranscriptを作るか貼り付けるよう依頼し、議事録・follow-upは未作成。([レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) | 音声message入力対応と、任意音声fileの文字起こしは別 |
| Duet、同レビュー | XLSXのin-app previewがformulaを実行しない。([レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) | 外部で開いてscoreを変え、formulaが働くことを本人確認。([レビュー](https://www.aiagentslibrary.com/blog/claude-duet-review/)) | agentの「計算確認済み」だけで検収しない |
| Duet、Sid Saladi氏の有料記事公開部分 | websiteのlogin・upload・code・formに苦戦、job応募に10時間で一件送付と申告。([公開部分](https://sidsaladi.substack.com/p/claude-duet-101)) | 完全な手順はpaywall内で未取得。([公開部分](https://sidsaladi.substack.com/p/claude-duet-101)) 本人報告の存在まで採用。([公開部分](https://sidsaladi.substack.com/p/claude-duet-101)) | 成功率・原因・他製品との優劣は確定不可 |
| Muse、独立メディア一週間 | eBayの条件が曖昧で不適切な状態の品が混入。([実践](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) | 状態・並び順・購入形式を具体化して改善。([実践](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/)) | 「自分を理解する」は初期設定不要を意味しない |
| Grok Bot、affiliate付き本人報告 | site block、CAPTCHA、再login、approval timeout、noise。([レビュー](https://jonathanmontoya.com/post/grok-bot-review)) | 人間へhandoffし重要成果を確認。([レビュー](https://jonathanmontoya.com/post/grok-bot-review)) | 25 Botsの体験は一般利用者の再現保証ではない |
| OpenClaw／Hermes、販売事業者DreamHostのlab | file ownershipで移行block、job・AGENTS.md等が移らず、skill衝突・重複。([技術検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/)) | 所有権修正・手動copy・doctor確認。([技術検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/)) モデル接続なしでchat品質は測定していない。([技術検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/)) | 軽量・移行可能という結果から仕事品質を推定しない |

DreamHost検証は10月16日、Apple-silicon Mac上のarm64 Ubuntu VM、2 vCPU・約4GB memory、no swap、Dockerで行い、idle memoryは12回測定のmedian等、条件が示される。([検証条件](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/)) しかしmodel keyもlive messagingも使わず、回答品質・model料金・実運用は対象外なので、idle memoryの数値からpersonal assistantの能力を順位付けすることはできない。([検証の限界](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/))

Teammatesは基準日の数日前の公開で、Cueも招待条件を伴うため、根拠が薄い製品について無理に成功・失敗の事例数を揃えていない。今後の追跡では、長期の実行ログ、承認が止まった画面、誤操作からの復旧、実支出、手作業の残量を優先して記録する。

## シナリオ別の導入・選定案

この章は調査に基づく実務提案であり、各製品で実施済みの試験ではない。いずれも「一製品・一役割・一週間」から始め、成果物の採用を人間が判断し、接続を増やすのは成功条件を満たした後とする。

### 個人利用：メール・予定・日々の用事

日本からの第一候補は無料枠のMuse、Google環境中心ならTasks in Gemini、既にProを使うならdotsを比較する。([Muse日本提供](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[Gemini資格](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[dots資格](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) Duetは米国限定、Cueは招待、Hark／Instinctは日本資格の確認不足があるため、国内での最初の一週間の既定候補にはしない。([Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Cue](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Hark](https://hark.com/using-hark)、[Instinct](https://instinct.com/terms))

| 項目 | 推奨する試行設計 |
|---|---|
| 最初の一週間 | 初日公開news監視、二日目架空calendar、三〜五日目は試験用mailboxの朝briefと返信案、六日目に候補旅行の比較、七日目に成果と停止手順を確認 |
| 許可する権限 | 公開Webのread、専用mailboxのread、試験calendarのread、作業用folderへの成果物作成。主mailbox・全写真・位置情報・支払・連絡先・家族accountは初期接続しない |
| 成果物 | 要返信mailのURL／日付／根拠、今日の予定と衝突、確認待ち一覧。返信案は宛先・本文・参照元を付け、送信済みと下書きを明確化 |
| 検収 | 仕込んだ返信漏れ・重複予定・古いnewsを発見できるか。不要通知、誤った緊急扱い、確認に要する時間を毎日記録 |
| 撤退条件 | 未承認の送信・変更、指定外mailboxへのアクセス、停止確認不能は即時停止。二日続けて検収作業が元作業を上回るなら役割・頻度を縮小 |
| 広げる条件 | 一週間、根拠付き報告が安定し、誤検出が説明でき、停止・権限撤回・削除手順を実際に確認できた後、主mailboxの限定範囲読取を再審査 |

家族の予定を使う場合も、本人だけの同意で他人の健康情報・学校情報・行動履歴を全面的に渡さない。日程候補や匿名化した制約だけを渡し、家族へのメッセージ送信は本人確認に残す。

### 個人開発者：複数GitHub・Issue・PR・CI・技術ニュース

候補は既存Computer文脈を使うTeammates、ChatGPT側からWork／Codexへ委任するdots、routineとBot分業のGrok Bot、運用を自分で持つOpenClaw／Hermesである。([Teammates](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[dots](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Grok Bot](https://docs.x.ai/grok-bot/faq)、[OpenClaw](https://docs.openclaw.ai/start/openclaw)、[Hermes](https://hermes-agent.nousresearch.com/docs)) どれを選んでも、最初から複数repositoryのwrite・Actions secrets・本番deployを一括委任しない。

| 項目 | 推奨する試行設計 |
|---|---|
| 最初の一週間 | 公開repositoryを二つまで指定し、毎朝Issue・PR・失敗CIの差分と、依存packageのrelease情報をMarkdownにまとめる。後半に架空Issueから調査メモ・再現手順・修正案だけ作る |
| 許可する権限 | 初期は公開Webのみ、必要時に選択repositoryのread-only。write段階は専用test repoまたはbranch・draft PRに限定し、merge・tag・release・workflow編集・secret参照は不可 |
| 成果物 | URL、Issue／PR番号、CI runとcommit SHA、前回との差分、再現コマンド、原因仮説と反証、test結果。成果はローカルMarkdownで検収し、公開は別承認 |
| 検収 | 同じIssueを毎日新件扱いしない、CI failureと原因仮説を分ける、失敗したtestを成功と書かない。引用したreleaseの発表日とstable／preview区分を照合 |
| 撤退条件 | 未承認commit／comment／merge、workflowやsecretへの接触、指定外repo閲覧・書込で即停止。理由不明の再試行や通知loopが続く場合はschedule停止 |
| 広げる条件 | 少なくとも三回の手動監督runで根拠・差分・停止を検証後、draft PR作成まで再審査。人間はdiff・license・test・securityを確認し、merge／releaseを行う |

Grok Botでは複数Botsが共有loginを使うので、「研究Botは読むだけ、実装Botは書く」という役割指示だけでは権限を分離できない。([公式FAQ](https://docs.x.ai/grok-bot/faq)) Teammatesでも既存plugin権限を継承するため、試験Projectを作ることだけでGitHub側の過剰scopeが縮むとは考えない。([公式ヘルプ](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates))

技術newsは「収集役」「一次出典確認役」「週報編集役」に分ける余地があるが、同じ情報を繰り返し検索して費用とnoiseを増やさないよう、URL・前回確認日・既知versionを共通の台帳に残す。最初は一体で安定させ、異なる権限や独立検証が必要になった時だけ分業を追加する。

### 組織・自治体：公開情報調査と報告案の小規模試行

第一段階は製品の選定より、組織が許可した環境で公開情報だけを使う業務設計を優先する。([Cowork概要](https://learn.microsoft.com/en-us/copilot/cowork/)、[dots対象条件](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) Microsoft 365中心であれば組織用Copilot Cowork、既存ChatGPT Enterprise等ならdotsの管理者設定を検討できるが、契約・role・region要件を満たすかは別確認である。([Cowork概要](https://learn.microsoft.com/en-us/copilot/cowork/)、[dots対象条件](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot))

| 項目 | 推奨する試行設計 |
|---|---|
| 最初の一週間 | 官公庁・自治体公式サイトの公開制度改正／公募を一日一回確認し、期限・変更点・原文URL付きの庁内確認用報告案を作る。架空の案件台帳から進捗確認表も作成 |
| 許可する権限 | 公開Webのみ、組織承認済み専用sandboxへの保存のみ。LGWAN・基幹・文書管理・職員mail・住民情報・職員SSO・本番SharePointは接続しない |
| 成果物 | 公表日と施行日・募集期限を分離、対象条件・変更前後・原文引用箇所、未確定事項、確認担当、実行日時、入力・出力・停止記録 |
| 検収 | 原文との照合、日付とtimezone、対象自治体・対象者、更新見逃し、誤通知、問い合わせ先の正確性。法的解釈や正式回答は職員が確定 |
| 撤退条件 | 非公開領域への接続要求、個人情報の投入誘導、無承認の対外発信、原文を取得できないのに断定、ログ・削除・費用の説明不能で中止 |
| 広げる条件 | 情報分類・契約・DPA・subprocessor・保存region・学習利用・監査・管理者停止・予算上限・incident対応を組織が審査後、限定資料へ段階拡張 |

個人向け契約の学習offだけで職場利用が承認されたことにはならない。組織の情報セキュリティ責任者、調達・契約担当、文書・個人情報管理担当が、対象情報、委託範囲、再委託、越境移転、保存、監査、事故報告、終了時のデータ返還・削除を確認する運用を推奨する。

住民へのメール、法令解釈の確定、補助金採否、契約・支出、情報公開の可否、文書の正式廃棄、人事判断は、人間の責任ある最終確認を残す。試用の成功はAIの自律性を最大化することではなく、確認可能な成果を一定の負担と予算内で繰り返し得られることと定義する。

## 権限管理・セキュリティ・プライバシー・運用上の注意

### 「読取だけ」でも漏えい経路は残る

read-only connectorは元systemを変更する権限を減らすが、読んだ情報を別site・email・fileに出す権限まで自動的に止めるわけではない。([Gemini公式ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Duet安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)、[Muse公式発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)) Geminiはchatやconnected sourcesからの情報をbrowserでsiteへ共有し得ることを明記し、Duetは外向きmessage・uploadを別classifierで検査し、MuseはSentinelとpermissionで外部actionを監督する設計である。([Gemini公式ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Duet安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)、[Muse公式発表](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/))

初期設定では「入力元の読取範囲」と「出力先」を別に制限する。個人mail全体を読ませて公開Webへ自由にform入力できる状態を、read-onlyだから安全と評価しない。

### 製品の設定と結び付けた確認事項

| リスク | 確認された仕様・注意 | 最初の運用策 |
|---|---|---|
| 過剰な情報アクセス | Teammatesはinstalled plugin・Project権限、Duetは既存Claude接続を引継ぐ。([Teammates](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 既存接続を棚卸しし、新役割に必要なものだけ許可。試験account・repo・mailboxを分離 |
| prompt injection | Geminiはwebsite・mail・document・Markdown・multimediaの悪意ある指示を警告し、Duetも完全防御ではないとする。([Gemini](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 外部本文を指示と認めない。送信・download実行・秘密参照を禁止し、不審指示は記録して止める |
| 誤送信・誤購入 | Museはtask・site・connector単位に今後の許可を広げられ、Instinct規約は代理transactionを広く認める。([Muse設定](https://www.meta.com/help/superintelligence/1385290430137537/)、[Instinct規約](https://instinct.com/terms)) | Always ask／Ask first、購入・署名・予約確定は本人。宛先・添付・総額・取消条件を確認 |
| 誤削除・不要commit | dotsのCustom rulesはdraftとsendを区別し、Grokのapprovalは既に完了したactionを取り消さない。([dots](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Grok](https://docs.x.ai/grok-bot/security)) | 原本read-only、作業copy・branch限定。削除・merge・公開は承認対象。backupを別保持 |
| 資格情報・session漏えい | Grok同一account内はbrowser login共有、Gemini remote browserはcookieを保存し得る。([Grok FAQ](https://docs.x.ai/grok-bot/faq)、[Gemini](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) | チャットにpasswordやAPI keyを貼らない。専用identity、短命token、最小scope、不要session sign-out |
| 自動費用増大 | Grokは追加usage設定、Teammatesは並列・大規模処理でcredits増加、Harkはauto top-upを持つ。([Grok](https://docs.x.ai/grok-bot/faq)、[Teammates](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)、[Hark](https://hark.com/using-hark)) | 初回は自動補充off、上限設定、頻度・再試行回数・並列数を制限。予算と残高は利用画面で確認 |
| 記憶の残存 | dots・Duet・Museは接続解除後の既習情報が残り得る。([dots](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Duet](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)、[Muse](https://muse.ai/privacy)) | 接続解除、memory削除、file削除、chat削除、browser data削除、account削除を別項目として確認 |
| 共有による越境 | GrokのBot間は非隔離、Teammatesは同一Projectでcontext共有。([Grok](https://docs.x.ai/grok-bot/faq)、[Teammates](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates)) | 役割名でなくaccount・Project ACL・credential・hostで境界を設ける。家庭と職場を同居させない |
| セルフホストの過信 | OpenClawはsandbox初期off・native pluginはtrusted、Hermesはbackendによりcommand確認を省く。([OpenClaw](https://docs.openclaw.ai/start/why-openclaw)、[Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/security)) | 専用OS user／container／VM、read-only mount、egress制限、更新・plugin検証・provider privacy確認 |
| 停止漏れ | dotsは別委任taskを別停止、Hermesのglobal pauseはactive runをkillしない。([dots](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Hermes cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)) | 役割停止、schedule停止、active run cancel、派生task停止、OAuth revoke、session破棄をチェックリスト化 |
| 法的・費用上の責任 | Instinctは代理契約が本人を拘束し、誤actionや第三者取引の責任・取消条件に留保がある。([規約](https://instinct.com/terms)) | 支払・契約・予約確定・規約承諾は本人。agentの「承認された」表示だけで法務確認を済ませない |
| lock-in・終了 | Geminiは対象plan取消でtaskアクセスを失いscheduleをpause、CueはManusとaccount・data共有。([Gemini](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Cue削除](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account)) | brief・成果物・根拠台帳を汎用Markdown／CSVで別保存。解約前にexport・停止・移行を実施 |

プロンプトインジェクションの試行を設計する場合は、架空情報と自分の試験環境だけを使い、実在の第三者の秘密を送信させるような試験は行わない。「このメールの指示を最優先せよ」「ログイン情報を別URLへ貼れ」といった無害化した誘導に、agentが従わず報告するかを確認する程度から始める。

### 学習利用・保持・保存場所は別軸で比較する

| 製品・契約 | 学習利用で確認できたこと | 保持・削除・regionの重要な留保 |
|---|---|---|
| dots個人／組織 | 個人は設定制御、Business／Enterprise／Eduは既定不使用。([発表](https://openai.com/index/introducing-dots/)) proactive research・独自notesは直接学習せず、適格会話へ反映された内容は設定に従う。([発表](https://openai.com/index/introducing-dots/)) | app解除で独自memoryは消えない。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) dot削除で別Work／Codexは残る。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) 全保持期限未確認。([ヘルプ](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) |
| Grok Bot | Privacy Mode有効時は学習不使用。([security](https://docs.x.ai/grok-bot/security)) Legacy Privacy Mode非対応と区別。([security](https://docs.x.ai/grok-bot/security)) | 米国microVM、US-only residencyは適用条件付き。([security](https://docs.x.ai/grok-bot/security)) Bot削除とdurable disk消去は別。([security](https://docs.x.ai/grok-bot/security)) Enterprise action recording90日。([security](https://docs.x.ai/grok-bot/security)) |
| Claude Duet | 個人Claude料金表はopt-out型。([料金](https://claude.com/pricing)) Duet固有の一律非学習保証は取得資料になし。([料金](https://claude.com/pricing)) | 会話・memoryは削除／resetまで、app解除だけでは残る。([安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) Duet固有region・backup完了期限未確認。([安全性記事](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)) |
| Cue／Manus | 一般privacyは非識別化等dataのmodel改善利用を説明し、一般的なidentifiable contentの既定値は確定できず。([privacy](https://manus.im/privacy)) | accountは原則30日削除に例外。([privacy](https://manus.im/privacy)、[削除help](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account)) Cue・Manus共同account。([privacy](https://manus.im/privacy)、[削除help](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account)) 一般Browser sandbox7／21日をCue全体へ適用しない。([privacy](https://manus.im/privacy)、[削除help](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account)) |
| Muse | Help improve our AI models初回on、off変更は過去interactionにも適用との説明。([privacy](https://muse.ai/privacy)) 会話・VM dataの広告非共有は別の保護。([privacy](https://muse.ai/privacy)) | forgetはbest effort、Resetは全情報削除。([privacy](https://muse.ai/privacy)、[data管理](https://www.meta.com/help/superintelligence/2225571704857152/)) backupを含む全保持期限・日本region未確認。([privacy](https://muse.ai/privacy)、[data管理](https://www.meta.com/help/superintelligence/2225571704857152/)) Confidential VMは予定。([privacy](https://muse.ai/privacy)、[data管理](https://www.meta.com/help/superintelligence/2225571704857152/)) |
| Teammates／個人Max | 一般consumerはAI Data Retention初期on、opt-outは以後のdata。([data収集](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)、[Max](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)) Brainが書くmemoryの非学習は全taskへ一般化しない。([data収集](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)、[Max](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)) | 一般privacyは必要期間保持・法的例外・backup残存・米国等処理。([privacy](https://www.perplexity.ai/privacy)) Teammatesのdesktop／logs専用期限は未確認。([privacy](https://www.perplexity.ai/privacy)) |
| Tasks in Gemini | TasksはKeep Activity onが必要。([Task help](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB)) Activityは改善・生成AI trainingへ使われ得る。([Task help](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)、[Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB)) | Activity既定18か月、review済みdata最大3年。([Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB)) remote browser／computerは別削除。([Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB)) |
| Hark Pro | account・input/output・memory・connector・sandbox dataをtrainingに使わない。([privacy](https://hark.com/privacy-policy)) 明示Feedbackは例外。([privacy](https://hark.com/privacy-policy)) | 原則active30日、backup90日で削除、法的等例外。([privacy](https://hark.com/privacy-policy)) task終了でsandbox削除、返却outputsは残る。([privacy](https://hark.com/privacy-policy)) |
| Instinct | prospective opt-out、safety review例外、Google Workspace API dataには非学習制限。([privacy](https://instinct.com/privacy-policy)) | disconnectは既存indexを消さず。([privacy](https://instinct.com/privacy-policy)、[規約](https://instinct.com/terms)) 一般保持期限・日本region未確定、account後の削除に規約留保。([privacy](https://instinct.com/privacy-policy)、[規約](https://instinct.com/terms)) |
| OpenClaw／Hermes | 自分が選ぶmodel provider・channel・pluginの条件次第。([OpenClaw](https://docs.openclaw.ai/start/why-openclaw)、[Hermes](https://hermes-agent.nousresearch.com/docs)) Foundationに送らないこととAPIへ送らないことは別。([OpenClaw](https://docs.openclaw.ai/start/why-openclaw)、[Hermes](https://hermes-agent.nousresearch.com/docs)) | host／backup／logsは運用者責任。外部API・messagingの保持は別契約。self-hostだけで国内保存は保証しない |

Perplexityのprivacyにある「Email Assistantのemail contentを学習に使わない」条件は、Teammatesの全Gmail taskや全generated contentについて同じ保証が適用されると本調査では確認できない。([Perplexity privacy](https://www.perplexity.ai/privacy)) 製品名・処理経路・入力種別の違いを残し、最も有利な別製品の条項を横流ししない。([Perplexity privacy](https://www.perplexity.ai/privacy))

### 委任範囲を広げる実務基準

次の段階制は本資料の提案であり、業界標準や各社の保証ではない。一つの段階を安定運用できても、別のデータ種別・相手・金額へ自動的に許可を広げない。

| 段階 | 許すこと | 次へ進む前の検収 |
|---|---|---|
| 公開情報のみ | 公開Web read、local成果物 | URL・日付・差分・推測区分、指定外アクセスなし |
| 限定private read | 試験mailbox、選択repo、特定folder | OAuth scope確認、外部送信禁止、記憶削除と停止を確認 |
| draft作成 | 返信案、作業copy、draft PR | 宛先・変更点・test・原本不変、検収負担が利益を超えない |
| 限定write | 試験calendarやbranchへの変更 | rollback、duplicate防止、監査、予算、approval境界を確認 |
| 継続運用 | role・schedule・event対応 | 通知SLAではなく実測、費用上限、障害・停止・再開・解約訓練 |

人間の最終確認を外さない作業は、外部公開、相手の権利義務に関わる契約・署名、支払・購入・予約確定、個人情報・機密情報の送信、原本削除、本番deploy、組織の正式判断である。低額・定型であっても、本人が許可条件を具体的に定義でき、実行履歴・停止・取消を検証できるまでは自動実行へ移さない。

## 料金・アクセス条件で選ぶ場合の整理

### 購読料金と仕事量を分けて比較する

| 選択肢 | 確認できた料金の入口 | エージェントの利用量・追加費用 | 比較時の注意 |
|---|---|---|---|
| Muse | 無料、Power $20/月、Maximum $100/月。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)) | Power週500M、Maximum週3B Muse tokens。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)) 無料数値・reset時刻未公表。([料金](https://www.meta.com/help/subscriptions/1021145227643680/)) | tokenを他社のcredit・タスク数へ換算しない |
| Tasks in Gemini | 日本Pro月2,900 JPY、Ultra月14,500 JPY〜。([日本料金](https://gemini.google/jp/subscriptions/?hl=ja)) | Compute-based limits、同時15task、上位planで枠拡大。([Task help](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) | 一般Gemini使用量の倍率をTasks完成数としない |
| Grok Bot | Premium $30、Super $100、Ultra $200/月。([製品ページ](https://x.ai/bot)) | 週次pool、追加credits／on-demand。([FAQ](https://docs.x.ai/grok-bot/faq)) 新旧契約でmeter相違。([FAQ](https://docs.x.ai/grok-bot/faq)) | 無料trial表示の有無、store自動課金、追加上限確認 |
| dots | Pro 100 USD/月〜、上位200／500 USD。([料金help](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)) | 最初のdot込み、Work／Codex別枠。([発表](https://openai.com/index/introducing-dots/)) dot専用数値は未確認。([発表](https://openai.com/index/introducing-dots/)) | Plusだけでは対象外。Enterprise preview無料を個人へ適用しない |
| Claude Duet | Pro月$20／年$200、Max月$100、Ultra月$200。([料金](https://claude.com/pricing)) | Previewは追加料金なし、background含めClaude枠共有。([help](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)) | 米国・招待条件を満たさないなら価格比較だけでは使えない |
| Cue | 招待後Plus無料。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) | Phone number／PC／Pro／Max等IAPあり、周期・適用未確定。([App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) | Manus本体プランとCue固有料金を合算推定しない |
| Teammates | Max $200/月または$2,000/年。([Max](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)) | Promotion後Max credits、通常月10,000、100 credits=$1。([製品ページ](https://www.perplexity.ai/hub/products/teammate)、[credits](https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity)) | 前払い年額・月付与・購入credits・promotionを分離。task費用は予測しない |
| Copilot Cowork | 個人Premium米国表示$19.99/月、企業は契約＋usage。([個人](https://www.microsoft.com/en-us/copilot/work/individuals)、[企業](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)) | 個人agentic枠は数値未確定。([同上企業発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)) 組織はPayGo／P3等の消費課金。([同上企業発表](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)) | 日本資格・地域価格・既存契約を別確認 |
| Hark Pro | 制限付き無料、Pro² $20／Pro³ $100/月。([料金](https://hark.com/pricing/)) | 2倍／10倍usage、auto top-upあり、絶対枠未公表。([ガイド](https://hark.com/using-hark)) | 日本資格・reset・追加単価を確認 |
| Instinct | 公開定価未確認。([規約](https://instinct.com/terms)) 規約は有料機能の可能性を記載。([規約](https://instinct.com/terms)) | 代行先の購入・取消・feesは本人側。([規約](https://instinct.com/terms)) | 不明を無料と扱わない |
| OpenClaw／Hermes | software無料・MIT。([OpenClaw](https://docs.openclaw.ai/start/why-openclaw)、[比較検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/)) | hosting、model API、browser、保守、backup等は別 | 無償softwareと低い総保有費用は同義でない |

本調査では他社を含む実taskの消費credit・tokenを予測しない。予算は購読、追加稼働、代行先の実費、検収・復旧時間の四つに分け、アカウントの使用画面で確認した実績を次週の運用判断に使う。

### 「今すぐ試す」際の入口の優先順位

- **未契約で公開情報から：** 日本提供が確認できるMuseの無料枠を第一候補とし、既存Google環境の継続支援なら日本Pro価格とTasks資格を確認する。([Muse日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[Google料金](https://gemini.google/jp/subscriptions/?hl=ja)、[Tasks資格](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) これは低い導入摩擦の提案であり、能力順位ではない。([Muse日本発表](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)、[Google料金](https://gemini.google/jp/subscriptions/?hl=ja)、[Tasks資格](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop))
- **既に高額個人planを保有：** dotsやTeammatesの表示・対象条件をまず確認し、継続roleを一つだけ設定する。([dots](https://openai.com/index/introducing-dots/)、[Teammates](https://www.perplexity.ai/hub/products/teammate)) 最初のdot込み、Teammatesのpromotionは「すべてのtaskが無制限・永久無料」とは異なる。([dots](https://openai.com/index/introducing-dots/)、[Teammates](https://www.perplexity.ai/hub/products/teammate))
- **運用を自分で学ぶ：** OpenClaw／Hermesは専用VM・試験tokenで比較する候補だが、アップデートと秘密管理を担えない場合は、software無償を理由に選ばない。([OpenClaw trust model](https://github.com/openclaw/openclaw/security)、[Hermes security](https://hermes-agent.nousresearch.com/docs/user-guide/security))
- **地域・招待で詰まる：** Duetの米国限定やCueの招待をVPN等で回避する導入は推奨しない。([Duet条件](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Cue条件](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Harkガイド](https://hark.com/using-hark)、[Instinct規約](https://instinct.com/terms)、[Grok FAQ](https://docs.x.ai/grok-bot/faq)) Hark／InstinctとGrok Botの日本向け条件は正規の提供画面・supportで確定してから接続する。([Duet条件](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)、[Cue条件](https://apps.apple.com/us/app/cue-by-manus/id6808613358)、[Harkガイド](https://hark.com/using-hark)、[Instinct規約](https://instinct.com/terms)、[Grok FAQ](https://docs.x.ai/grok-bot/faq))

## 重要な不明点・検証が必要な事項

### 情報が変わった・矛盾して見える事項

| 論点 | 比較した出典と差分 | 本資料の処理 |
|---|---|---|
| dots初回作成 | 9月発表はdesktopで開始、現行helpはmobile作成も案内。([発表](https://openai.com/index/introducing-dots/)、[help](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | 現行helpを優先。過去の手順を現行制約として残さない |
| dots Enterprise | 発表のbetaと、現行helpのGA・11月18日までadmin preview。([発表](https://openai.com/index/introducing-dots/)、[help](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)) | GA表記でも基準日は管理者有効化条件あり。11月18日予定を実施済みにしない |
| Grok Bot課金 | 8月発表は別usage、現行FAQはX Subscription共通poolとlegacy別meterを分離。([発表](https://x.ai/news/introducing-grok-bot)、[FAQ](https://docs.x.ai/grok-bot/faq)) | 新規とlegacyを分ける |
| Grok倍率 | BotページはPremium比Super3.5倍／Ultra12倍、X SubscriptionはPlus比4／15／50。([Bot価格](https://x.ai/bot)、[subscription発表](https://x.ai/news/x-subscription)) | 基準・丸め・適用範囲が違う可能性はあるが解明できず、同一の正確な比率へ換算しない |
| X Subscription発表日 | 取得本文はOct 12、検索metadataにはOct 28表示。([取得した公式本文](https://x.ai/news/x-subscription)) | 発表日確定の主要根拠にしない。基準日の料金は現行Botページ・FAQで確認 |
| Cue iOS | 発表時はApp Store review待ち、現行掲載あり。([発表](https://manus.im/blog/introducing-manus-2-0)、[App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358)) | 現行iOSあり。ただし日本の配信・招待資格は別 |
| Muse日本 | 9月発表はUS、10月23日日本公式開始。([初回](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)、[日本](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/)) | 日本提供済み。古い英語reviewのUS-onlyを現行へ適用しない |
| Muse円料金 | 本人投稿はPower2,799円、公式helpは$20と地域差の記載。([本人投稿](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e)、[公式料金](https://www.meta.com/help/subscriptions/1021145227643680/)) | 円額は本人の一時点観察のみ。公式の日本共通定価として採用しない |
| Gemini常時稼働 | 発表はcloudで端末off継続、現行helpはlocal／remoteとschedule device条件を区分。([発表](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)、[help](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop)) | 実行経路ごとに確認。未整理部分を包括的24/7保証にしない |
| Cowork個人／組織 | 6月GAは企業中心、11月概要は個人previewも扱う。([GA](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[概要](https://learn.microsoft.com/en-us/copilot/cowork/)) | 組織GAと個人previewを別欄にする |

### 優先して再調査する事項

- **日本の利用資格：** Grok Bot、Cue、Hark Pro、Instinctの正規signup・store地域・phone対応、Teammatesの当該account配信を確認する。公開国一覧がない場合、一般chat製品の国リストやprivacyの国別条項を代用しない。
- **無料・promotionの終了：** Teammates無料usageの期限とamount、Cue無料Plusの期間・各IAP周期、Grok trialの表示条件、dots専用作業枠を確認する。加入画面のscreenと日時を証跡にし、他人のcampaignを自分の契約へ当てはめない。
- **停止・復旧：** 全製品で親role停止、schedule停止、child task cancel、接続revoke、browser session破棄を区分して試す。特にTeammates・Cueの統一停止・再開・重複実行防止は追加確認が必要。
- **権限の実効性：** Gmail readとsend、Calendar readとinvite、GitHub contents／issues／pull requests／workflows、Slack historyとpost、Drive readとshare／deleteを、接続画面とtool単位で表にする。未公開scopeは「連携あり」だけで埋めない。
- **記憶と削除：** chat・memory・source file・generated file・browser cookies・logs・backupを分け、削除完了と契約上の例外を確認する。CueとManusの共同accountや、Bot削除後の共有diskも対象にする。
- **preview／予定の追跡：** Duetの1Password・Team／Enterprise、Muse Confidential VM・国内提携・voice／avatar、dots追加体制、Teammates native appは、公式の実提供発表・対象account確認が出るまで予定欄に残す。
- **実践根拠の補強：** Cue・Teammatesの独立した長期利用、日本の複数repository管理、旅行・家族・小規模営業の設定から結果まで揃った報告を追う。二日間の好成績や主観scoreを可用性・成功率としない。

### 次回実機試用で記録する最小セット

記録項目は「日時・timezone、国・OS・app version、plan、role brief、接続scope、入力と原本、実行経路、approval画面、成果物、error・retry、本人作業時間、表示usage、停止・削除手順」とする。今回の資料には実機記録がないため、この欄を今後の検証テンプレートとして残す。

## 出典の検証記録と再調査先

以下は引用の代わりではなく、更新日と確認範囲の追跡台帳である。本文・表の重要な主張にはそれぞれ直接URLを置き、この台帳だけを根拠にしていない。全行の確認日は2026年11月8日で、相対更新日を厳密な公開日に変換していない。

### 公式の製品・アクセス・料金

| 資料 | 公開・更新日の確認 | 確認に用いた範囲 |
|---|---|---|
| [OpenAI Introducing dots](https://openai.com/index/introducing-dots/) | 公開9月29日、11月3日追記 | 名称、環境、自発的read、初回plan、安全、将来像 |
| [Getting started with your dot](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot) | 取得metadata11月7日、本文相対更新 | 現行setup、対象地域、rules、pause、delete、Enterprise preview |
| [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers) | 本文「5 days ago」 | USD月額、年払いなし、usageの別枠 |
| [ChatGPT pricing](https://chatgpt.com/pricing/) | 明示日なし | plan機能。動的な価格欠落はraw HTMLも照合し、Pro helpで補完 |
| [Introducing Grok Bot](https://x.ai/news/introducing-grok-bot) | 8月11日 | 発表時のbeta・旧plan・role分業 |
| [Grok Bot](https://x.ai/bot) | 明示日なし | 現行価格・shared cloud computer・routine |
| [Grok Bot FAQ](https://docs.x.ai/grok-bot/faq) | 10月29日更新 | 現行／legacy課金、trial、OS、共有memory・PC、使用枠 |
| [Introducing The X Subscription](https://x.ai/news/x-subscription) | 本文10月12日、検索metadata不一致 | 現行体系の補助。発表日の確定には不採用 |
| [Cursor is now a part of SpaceX](https://cursor.com/blog/joining-spacex) | 8月14日 | 運営関係の変更 |
| [Introducing Claude Duet](https://claude.com/resources/articles/claude-duet) | 10月21日、23日追記 | app、能動確認、cloud、承認、future |
| [Get started with Claude Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet) | 本文「Updated this week」 | US、waitlist、plans、reset、Tasks、limitations |
| [Claude pricing](https://claude.com/pricing) | 明示日なし | Pro／Max／Ultra料金、税別、一般学習条件・usage例外 |
| [Introducing Manus 2.0](https://manus.im/blog/introducing-manus-2-0) | 9月28日。年は公式記事一覧で照合 | CueとStudio／Cloud Computerの関係、early access |
| [Manus公式記事一覧](https://manus.im/blog) | 2.0は2026年9月28日、独立再開9月1日 | 年月日の補完のみ |
| [Manus Resumes Independent Operations](https://manus.im/blog/manus-resumes-independent-operations) | 9月1日。年は記事一覧で照合 | 現行の独立運営・データ復元の移行 |
| [What is new in Manus 2.0?](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0) | 10月1日表示 | Cue招待の入口、Automations、製品間の区分 |
| [Cue by Manus、App Store](https://apps.apple.com/us/app/cue-by-manus/id6808613358) | 掲載日なし、version履歴あり | 正式名、seller、iOS、日本語、IAP、無料特典 |
| [Cue by Manus、Google Play](https://play.google.com/store/apps/details?id=ai.manus.agents&hl=en_GB) | 11月7日更新 | 現行Android、automations、approval、Memory and Dream |
| [Meta Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) | 9月8日・30日の二日付表示 | Secure VM、Sentinel、初期launch、future機能 |
| [Muse日本提供開始](https://about.fb.com/ja/news/2026/10/muse-personal-ai-agent-launches-in-japan/) | 10月23日 | 日本availability、入口、国内提携予定、voice留保 |
| [How to get started with Muse](https://www.meta.com/help/superintelligence/1331373868832401/) | 本文「a day ago」 | account、main／side chat、artifact、voice地域留保 |
| [About Muse subscriptions](https://www.meta.com/help/subscriptions/1021145227643680/) | 本文「8 weeks ago」 | Power／Maximum、usage、月更新、成年・国条件 |
| [Perplexity Teammates](https://www.perplexity.ai/hub/products/teammate) | 明示日なし | 正式表記、role、継続thread、promotion、future apps |
| [Teammates are agents for complex, ongoing work](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work) | 11月4日 | 初回発表日、継続role、setup |
| [Get started with Perplexity teammates](https://www.perplexity.ai/help-center/en/articles/2026102601-perplexity-teammates) | 11月5日更新 | preview、個人Max、Project・tool権限、model・環境 |
| [11月6日Perplexity changelog](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode) | 11月6日 | TeammatesとMac local modeの区分 |
| [Perplexity Max](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max) | 9月14日更新 | 月／年料金、billing経路、Brain controls |
| [How credits work](https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity) | 11月4日更新 | 月枠・bonus・reset・補充・pause／resume |
| [Gemini appのagentic化発表](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/) | 5月19日 | Sparkの当初発表、trusted tester／US beta予定 |
| [Tasks in Gemini help](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Desktop) | 明示日なし | 現行正式表記、資格、15task、local／remote、権限・停止 |
| [日本向けGemini subscriptions](https://gemini.google/jp/subscriptions/?hl=ja) | 明示日なし | JPY月額、Pro／Ultra構成、個人account条件 |
| [Copilot Cowork overview](https://learn.microsoft.com/en-us/copilot/cowork/) | 11月7日更新 | 組織GAと個人preview、skills、approval、pause |
| [Copilot Cowork GA](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/) | 6月16日 | 組織cloud、課金、予算・監査、当時のfuture |
| [Cowork更新履歴](https://learn.microsoft.com/en-us/copilot/cowork/whats-new) | 11月7日更新 | local browserのGA等。11月の月次記載は個別配信保証なし |
| [Copilot for Individuals](https://www.microsoft.com/en-us/copilot/work/individuals) | 明示日なし | 米国表示価格・trial、market unavailable留保 |
| [OpenClaw Getting started](https://docs.openclaw.ai/start/getting-started) | 明示日なし | runtime、setup、background Gateway |
| [OpenClaw Personal assistant setup](https://docs.openclaw.ai/start/openclaw) | 明示日なし | chat連携、専用番号、allowlist、automation |
| [OpenClaw Why OpenClaw](https://docs.openclaw.ai/start/why-openclaw) | 比較snapshot reviewは8月27日 | Foundation、MIT、no paid tier、sandbox初期off |
| [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs) | 明示日なし | 提供元、入口、skills・memory、runtime |
| [Hermes cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | 本文明示日なし | gateway、schedule／webhook、pause／cancel／removeの差 |
| [Introducing Hark Pro](https://hark.com/articles/introducing-hark-pro) | 本文OCT 06、発表年は未確認 | 基準日に取得した機能説明として使用。発表年の確定には不採用 |
| [Using Hark Pro](https://hark.com/using-hark) | 明示日なし | Handoff、Services、memory、vault、auto top-up |
| [Hark pricing](https://hark.com/pricing/) | 明示日なし | 無料／20／100ドル、usage倍率 |
| [Instinct](https://instinct.com/) | 明示日なし | text／callという入口と製品例。価格・地域には不使用 |

### 公式の安全・データ条件

| 資料 | 日付 | 本調査の主な照合点 |
|---|---|---|
| [Grok Bot security](https://docs.x.ai/grok-bot/security) | 11月6日更新 | member VM、US、network・rules、recording、privacy mode |
| [Claude Duet Safety, Privacy, and Security](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security) | 10月23日 | credential proxy、outbound classifier、承認、memory、browser |
| [Manus privacy](https://manus.im/privacy) | 9月28日更新 | controller、非識別化data、account／sandbox削除、越境 |
| [Manus／Cue account削除](https://help.manus.im/en/articles/11711823-will-my-personal-data-be-deleted-after-i-delete-my-account) | 10月1日表示 | 共同accountとCue-only削除非対応 |
| [Muse privacy](https://muse.ai/privacy) | 9月17日発効 | training初期on、Accounts Center、memory、connector、future VM |
| [Muse guidance and approval](https://www.meta.com/help/superintelligence/1385290430137537/) | 本文8 weeks ago | read／write、許可範囲、Activity、不可逆action |
| [Muse data management](https://www.meta.com/help/superintelligence/2225571704857152/) | 本文8 weeks ago | training off、Memory／Soul／Identity、export、reset |
| [Muse privacy safety security help](https://www.meta.com/help/superintelligence/1047255454427887/) | 本文8 weeks ago | 個人VM・backup・隔離の補助確認 |
| [Perplexity Data Collection](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity) | 8月31日更新 | consumer初期on・prospective opt-out、Enterpriseとの差 |
| [Perplexity Privacy Notice](https://www.perplexity.ai/privacy) | 10月23日更新 | 一般保持、backup、米国等移転、Email Assistant条項の限定 |
| [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en-GB) | Hub10月26日、notice10月13日更新 | Activity、review retention、local folders・remote state |
| [OpenClaw security policy](https://github.com/openclaw/openclaw/security) | page明示日なし、掲載advisories9月11日 | trusted operator、非multi-tenant、sandbox・plugin、公開gateway禁止 |
| [Hermes security](https://hermes-agent.nousresearch.com/docs/user-guide/security) | 明示日なし | command承認、unattended deny、container・MCP、injection heuristic |
| [Hark privacy](https://hark.com/privacy-policy) | 11月5日更新 | training除外とFeedback例外、active30日・backup90日 |
| [Instinct terms](https://instinct.com/terms) | 8月26日改定 | 代理transaction、本人責任、confirmation留保、18+ |
| [Instinct privacy](https://instinct.com/privacy-policy) | 8月26日改定 | prospective opt-out、Workspace例外、indexとdisconnect |

### 実践報告の来歴

| 資料 | 日付・筆者 | 採用範囲と留保 |
|---|---|---|
| [PC Watchのdots特集](https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html) | 11月6日、清水理史氏 | 自身のGmail／Calendar・project横断の観察。独立再現なし |
| [Grok Bot本人レビュー](https://jonathanmontoya.com/post/grok-bot-review) | 10月30日、Jonathan Montoya氏 | 約25 Botsの役割分業・介入。affiliate開示、統制試験なし |
| [Duet 10 business tasks](https://www.aiagentslibrary.com/blog/claude-duet-review/) | 10月28日公開・29日更新、Diana氏 | 自費・非スポンサー、二日間・主要一回ずつ。採点を総合信頼性に不採用 |
| [Duet 101](https://sidsaladi.substack.com/p/claude-duet-101) | 11月5日、Sid Saladi氏 | 六日間本人試行の公開部分のみ。paywall内の手順は未読 |
| [Muse一週間実践](https://www.androidauthority.com/meta-muse-one-week-later-hands-on-3718233/) | 10月6日、Stephen Radochia氏 | Gmail・定期検索・条件修正。購入未試験、統制試験なし |
| [Muse無料枠からPowerへ](https://qiita.com/hisashi-ito/items/35ae4e1df207b0e5d34e) | 11月2日、投稿account hisashi-ito | 国内自己報告、Muse記録＋Claude Code確認の生成補助、usageは割合のみ |
| [DreamHost比較技術検証](https://www.dreamhost.com/guides/openclaw/openclaw-or-hermes-agent/) | 更新10月22日、VM試験10月16日 | 商用hosting販売者のlab。model非接続、idle・migrationのみ |

### 調査手順と到達限界

調査は、指定された公式入口7ページの直接取得、必須6製品の現行help・料金・privacy照合、追加候補の実在性確認、実践報告の本人性・日付・方法確認、最後に矛盾・未確認事項の整理の順で行った。取得に失敗したURLや不正なpathは別の正規公式pathを探し、取得できない本文を検索断片から再構成していない。

一次情報の確認を優先し、Reddit・X・GitHub Issueを網羅収集する調査にはしていない。日時・本人性・設定・結果が揃う記名記事を主に採用し、GitHubのsecurity policyとadvisoriesはself-host運用の境界確認に用いたが、個別incidentの全原因・修正versionまで追跡した脆弱性監査ではない。

このため、本資料から判断できるのは「どの契約・実行形態・監督条件で、何を小さく試すか」である。無人の本番運用、国内の全アカウントでの利用、固定料金内の処理件数、機密情報を含む業務への適合を保証する資料ではなく、次の一週間の限定試行と契約確認を設計するために用いる。

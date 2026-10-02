# 個人開発で使える無料・無料枠API

個人開発・PoC・技術検証で利用しやすいAPIやデータサービスをまとめる。

無料枠や利用条件は変更されるため、利用前に公式サイトで最新条件を確認する。

- 調査日: 2026-10-02
- 目的: 「何かAPIを組み合わせて試したい」ときに、候補を短時間で絞り込む
- 対象: APIまたはプログラムから扱える構造化データ・タイル配信があるもの。通常のWebページしかないものは載せていない

## この資料の確認範囲について

調査環境のネットワーク制限により、公式サイトのページ本体を直接取得できなかった。そのため、**公式ドメインに限定した検索結果の内容**と、取得できた**GitHub上の公式リポジトリ**（`public-apis` / `free-for-dev` / `voicevox_engine`）を根拠にしている。

- 無料枠の数値は、公式ドメインの検索結果で確認できたものだけを書いた。確認できないもの、変動が激しいものは「上限は公式参照」とした
- 非公式のまとめ・ブログは、数値や条件の根拠に使っていない
- 利用を決める前に、各項目の「公式」リンクで必ず再確認する

## 分類の見方

| 分類 | 意味 |
| --- | --- |
| 公共・無料 | 政府・自治体・公的機関が提供し、原則無料で継続利用できる。登録やAPIキーが必要なものを含む |
| 無料枠あり | 有料サービスだが、継続的なFree Tier（毎日・毎月の無料分）がある |
| 無料モデル・プラン | 特定のモデルや、無料プランの範囲だけが無料 |
| 無料 | 登録なし、または無料登録だけで使えるオープンなAPI。レート制限や利用ポリシーはある |
| 非商用のみ無料 | 個人・非営利・開発環境に限って無料。商用は別契約や有料 |
| Trial / 初回付与 | 評価用の試用枠、または初回だけ付与される無料分。継続的なFree Tierではない |
| ローカル実行 | クラウドAPIの無料枠ではなく、OSS等を自分の環境で動かす |
| カタログ | APIそのものではなく、APIを探すための一覧 |

## 一覧表

### 生成AI・LLM・Embedding

| API / サービス | 分類 | 無料利用 | 認証 | 主な用途 | メモ |
| --- | --- | --- | --- | --- | --- |
| Gemini API | 無料枠あり | 一部モデルのみ無料枠 | API Key | 生成・要約・分類 | 課金アカウントを紐付けると、そのプロジェクトの利用は全て課金対象 |
| Groq | 無料モデル・プラン | 無料プラン（上限は公式参照） | API Key | 高速なLLM応答 | 無料プランはカード不要。Developerへのアップグレードはカード等が必要 |
| OpenRouter | 無料モデル・プラン | `:free` モデルのみ | API Key | 複数LLMの切替・比較 | 無料モデルはレート制限あり。上限は残高で変わる |
| Mistral（Mistral Studio） | 無料枠あり | Freeティアあり（上限はコンソール参照） | API Key | LLM・OCR等の試作 | 旧名称 La Plateforme。名称はStudioへ移行している |
| Hugging Face Inference Providers | 無料枠あり | 月次の少額クレジット | HFトークン | 多様なOSSモデルの呼び出し | 無料ユーザーはPROより少額。超過は従量課金 |
| Cloudflare Workers AI | 無料枠あり | 1日あたりの無料割当 | CFアカウント / API Token | エッジでの推論 | 一部モデルは有料プラン必須（2026-07変更） |
| Cohere | Trial | 評価キー（月間上限あり） | API Key | Chat / Embed / Rerank の試用 | 商用・本番利用は不可。本番キーは従量課金 |
| Jina AI | Trial / 初回付与 | 新規キーに無料トークン | API Key | Embedding / Rerank / Reader | 付与分を使い切ると購入が必要 |
| Voyage AI | Trial / 初回付与 | アカウントごとの初回無料トークン | API Key | Embedding / Rerank | モデルごとに無料分が決まっている |

### 検索・ニュース・気象

| API / サービス | 分類 | 無料利用 | 認証 | 主な用途 | メモ |
| --- | --- | --- | --- | --- | --- |
| Brave Search API | 無料枠あり | 毎月$5分のクレジット | API Key | Web検索の組み込み | カード登録必須。帰属表示が条件 |
| Tavily | 無料枠あり | 月1,000クレジット | API Key | AIエージェント向け検索 | カード不要 |
| NewsAPI | 非商用のみ無料 | Developerプラン（開発環境のみ） | API Key | ニュース取得の試作 | 本番・ステージング・社内利用は不可 |
| Open-Meteo | 非商用のみ無料 | 非商用は無料 | 不要 | 天気・予報 | 商用は有料プラン。帰属表示（CC BY 4.0）が必要 |
| OpenWeatherMap | 無料枠あり | One Call 3.0は1日1,000回まで | API Key | 天気・予報 | 超過分は従量課金 |
| 気象庁 防災情報XML | 公共・無料 | 無料 | 不要 | 警報・地震・火山等の電文 | 出典明記が必要。提供の停止・遅延は保証されない |

### 公共データ・行政（日本）

| API / サービス | 分類 | 無料利用 | 認証 | 主な用途 | メモ |
| --- | --- | --- | --- | --- | --- |
| e-Stat API | 公共・無料 | 無料 | アプリケーションID | 政府統計 | ユーザー登録が必要。IDは1ユーザー3つまで |
| 日本銀行 時系列統計データAPI | 公共・無料 | 無料 | マニュアル参照 | 金融・経済の時系列 | 2026-02提供開始。20万系列超 |
| 法人番号システム Web-API | 公共・無料 | 無料 | アプリケーションID | 法人情報の照会・名寄せ | ID発行は手数料・添付書類なし。検証環境あり |
| e-Gov 法令API（Version 2） | 公共・無料 | 無料 | 登録・申請不要 | 法令本文・改正履歴 | 時点指定で過去の条文を取得できる |
| 国会会議録検索システム API | 公共・無料 | 無料 | 仕様上キーの記載なし | 発言・会議録の取得 | 多重リクエストは避ける |
| 国立国会図書館サーチ API | 公共・無料 | 無料（営利目的は申請が必要な場合あり） | 申請が必要な場合あり | 書誌・蔵書検索 | クレジット表示が必須 |
| 次世代デジタルライブラリー | 公共・無料 | 無料（営利かつ継続利用を除く） | 申請不要（条件あり） | 全文テキスト検索・IIIF | 実験的サービス。安定提供は前提にしない |
| 国土地理院 地理院タイル | 公共・無料 | 無料 | 不要 | 地図表示・標高・陰影 | 出典明示で申請不要（基本測量成果） |
| 国土数値情報 | 公共・無料 | 無料（ファイル配布） | 不要 | 行政区域・施設・災害リスク等のGISデータ | APIではなくダウンロード。データごとに商用可否が異なる |
| 不動産情報ライブラリ API | 公共・無料 | 無料 | 申請・審査後にAPIキー | 取引価格・地価・都市計画 | 審査は5営業日が目安 |
| 国土交通データプラットフォーム API | 公共・無料 | 無料 | アカウント + APIキー | 国交省系データの横断検索 | GraphQL。データごとにライセンスが異なる |
| PLATEAU データカタログAPI | 公共・無料 | 無料 | 記載なし | 3D都市モデル（3D Tiles / MVT） | CC BY 4.0等のオープンライセンス |
| アドレス・ベース・レジストリ / ABRジオコーダ | ローカル実行 + 公共データ | 無料 | 不要 | 住所の正規化・緯度経度付与 | ジオコーダはOSS。手元で動かす |
| 公共交通オープンデータセンター（ODPT） | 公共・無料 | 無料 | 登録 + APIキー | 鉄道・バス等の運行データ | データごとのライセンスは事業者が決める |
| J-Quants API | 無料枠あり | Freeプラン（12週遅延） | アカウント | 株価・財務データ | 無料は1年間で、毎分5回まで |
| e-Govデータポータル / 東京都オープンデータAPI | 公共・無料 | 無料 | 不要（東京都APIは登録不要） | データ検索・自治体データ | メタデータ取得APIはCKAN互換。旧データカタログサイトの後継 |

### 海外のオープンデータ・学術・為替・地図

| API / サービス | 分類 | 無料利用 | 認証 | 主な用途 | メモ |
| --- | --- | --- | --- | --- | --- |
| Wikimedia API | 無料 | 無料 | 不要（User-Agent必須） | 記事・要約・メタデータ | 匿名と識別済みでレート上限が違う |
| arXiv API | 無料 | 無料 | 不要 | 論文検索 | 3秒に1回・単一接続 |
| Crossref REST API | 無料 | 無料 | 不要（mailto推奨） | DOI・論文メタデータ | mailto付きの方が上限が高い |
| OpenAlex | 無料枠あり | 1日$1分の利用 | API Key（無料） | 論文・著者・機関の分析 | 2026-02以降はキー必須 |
| Frankfurter | 無料 | 無料 | 不要 | 為替レート | 中央銀行の公表レートを集約 |
| Nominatim（公開インスタンス） | 無料 | 無料（重い利用は禁止） | 不要（User-Agent必須） | ジオコーディング | 上限は1秒に1リクエスト |

### 開発・メディア・実用

| API / サービス | 分類 | 無料利用 | 認証 | 主な用途 | メモ |
| --- | --- | --- | --- | --- | --- |
| GitHub REST API | 無料 | 無料（レート制限あり） | 不要 / PAT | リポジトリ分析・自動化 | 未認証は1時間60回、認証で5,000回 |
| YouTube Data API | 無料枠あり | 1日10,000ユニット | API Key / OAuth | 動画・チャンネル情報 | メソッドごとに消費ユニットが違う |
| LINE Messaging API | 無料枠あり | コミュニケーションプラン（月200通） | チャネルアクセストークン | Bot・通知 | 上限を超える配信は不可 |
| Unsplash API | 無料枠あり | Demoは1時間50回 | Access Key | 写真の検索・表示 | 帰属表示とホットリンクが必須 |
| Pexels API | 無料枠あり | 1時間200回 / 月20,000回 | API Key | 写真・動画の検索 | 帰属表示が必要。上限引き上げは一時停止中 |
| TMDB | 非商用のみ無料 | 非商用は無料 | API Key | 映画・TV情報 | 商用・AI学習利用は別契約 |
| DeepL API Developer | Trial / 初回付与 | 累計100万文字（月次リセットなし） | API Key | 翻訳 | 上限に達するとGrowthへの移行が必要 |
| Google Cloud Vision（OCR） | 無料枠あり | 毎月最初の1,000ユニット | GCP認証 | 画像・文書のOCR | 超過は従量課金 |
| VOICEVOX ENGINE | ローカル実行 | 無料（商用・非商用とも可） | 不要（ローカルAPI） | 日本語音声合成 | クレジット表記が必要。キャラクターごとの規約が優先 |

### APIカタログ

| 名称 | 分類 | 認証 | 主な用途 | メモ |
| --- | --- | --- | --- | --- |
| public-apis | カタログ | 不要 | 公開APIの探索 | 各行に認証・HTTPS・CORSの有無がある。無料枠の最新条件は載っていない |
| free-for-dev | カタログ | 不要 | 無料枠のあるインフラ系サービスの探索 | 掲載条件は「Trialでなく無料枠」。APIよりインフラ寄り |
| publicapi.dev | カタログ | 不要 | カテゴリ別のAPI探索 | 認証方式で絞り込める |

## 詳細

### 生成AI・LLM・Embedding

#### Gemini API

- 種類: 生成AI（Google）
- 無料利用: 一部モデルにFree Tierがある。レート制限はモデルごとに異なる。具体的な数値とモデル名は変わりやすいため公式を参照
- 認証: API Key（Google AI Studioで発行）
- 主な用途: 文章の要約・分類・抽出、検索結果の整理
- 利用時の注意: 課金アカウントを紐付けると、以後その利用は全て課金対象になる。無料枠でのデータの取り扱いは規約を確認する
- 公式: [Pricing](https://ai.google.dev/gemini-api/docs/pricing) / [Rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) / [Billing](https://ai.google.dev/gemini-api/docs/billing)

#### Groq

- 種類: 高速推論のLLM API
- 無料利用: 無料プランがあり、レート制限（RPM / RPD / トークン）はモデルごと。具体値は公式のRate limitsとコンソールのlimits画面を参照
- 認証: API Key
- 主な用途: 応答速度が重要なチャット・エージェントの試作
- 利用時の注意: 無料プランはカード不要。Developerプランへのアップグレードは支払い方法が必要
- 公式: [Rate limits](https://console.groq.com/docs/rate-limits) / [Plans](https://console.groq.com/settings/billing/plans)

#### OpenRouter

- 種類: 複数モデルへの統一API
- 無料利用: モデルIDが `:free` で終わるものが無料。レート制限があり、クレジット残高の有無で上限が変わる。失敗したリクエストも上限に数えられる
- 認証: API Key
- 主な用途: 同じコードで複数のLLMを切り替えて比較する
- 利用時の注意: 無料モデルは入れ替わりが速く、提供が突然終わることがある。モデル名を固定した設計は避ける
- 公式: [Limits](https://openrouter.ai/docs/api_reference/limits)

#### Mistral（Mistral Studio）

- 種類: LLM・OCR等のAPI
- 無料利用: 実験・評価・試作向けのFreeティアがある。上限は秒間リクエスト、毎分トークン、毎月トークンの3種で、数値はコンソールのLimitsで確認する
- 認証: API Key
- 主な用途: 日本語を含む軽量なLLMの試作、文書のOCR
- 利用時の注意: 旧「La Plateforme」はStudioの名称に移っている。Freeティアのデータの取り扱いは規約を確認する。OCRはページ単価の課金で、無料枠の適用可否は要確認
- 公式: [Usage and limits](https://docs.mistral.ai/admin/user-management-finops/tier) / [Pricing](https://mistral.ai/pricing/)

#### Hugging Face Inference Providers

- 種類: 複数の推論プロバイダへのルーティング
- 無料利用: 全ユーザーに月次クレジットがあり、無料ユーザーはPROより少額。使い切ると従量課金
- 認証: HFトークン
- 主な用途: OSSモデルの動作確認、Embeddingや画像モデルの試用
- 利用時の注意: 自前のプロバイダキーを使うとクレジットは適用されない。旧「Inference API」の無料枠とは別物
- 公式: [Pricing and Billing](https://huggingface.co/docs/inference-providers/pricing)

#### Cloudflare Workers AI

- 種類: エッジ推論
- 無料利用: 1日あたりの無料割当（Neurons単位）がある。超過はWorkers Paidでの従量課金
- 認証: Cloudflareアカウント / API Token
- 主な用途: LLM・Embedding・画像などの軽量な推論をWorkersから呼ぶ
- 利用時の注意: 2026-07に、一部モデルがWorkers Paid限定になった。使うモデルが無料枠の対象か確認する
- 公式: [Pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) / [Changelog](https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/)

#### Cohere

- 種類: LLM・Embedding・Rerank
- 無料利用: **Trial**（評価キー）。継続的なFree Tierではない。エンドポイントごとに毎分上限と月間呼び出し上限がある
- 認証: API Key
- 主な用途: Rerankや多言語Embeddingの品質確認
- 利用時の注意: 評価キーは商用・本番利用が認められない。本番キーは従量課金
- 公式: [Rate limits](https://docs.cohere.com/docs/rate-limits) / [Pricing](https://cohere.com/pricing)

#### Jina AI

- 種類: Embedding / Rerank / Reader（URLの本文取得）
- 無料利用: 新規APIキーに無料トークンが付く。**初回付与型**で、使い切ると購入が必要。トークンはReader・Embeddings・Rerankerで共有
- 認証: API Key
- 主な用途: RAGの試作、Webページ本文のLLM向け変換
- 利用時の注意: 無料キーはレート制限が低い
- 公式: [Embeddings](https://jina.ai/embeddings/) / [Reranker](https://jina.ai/reranker/) / [Reader](https://jina.ai/reader/)

#### Voyage AI

- 種類: Embedding / Rerank
- 無料利用: アカウントごとに、モデルごとの初回無料トークンがある。継続的な毎月の無料枠ではない
- 認証: API Key
- 主な用途: 検索・RAGの精度比較
- 利用時の注意: モデルのラインナップが入れ替わるため、無料の対象モデルは公式Pricingで確認する
- 公式: [Pricing](https://docs.voyageai.com/docs/pricing)

### 検索・ニュース

#### Brave Search API

- 種類: Web検索API
- 無料利用: 各プランに毎月$5分の無料クレジット。クレジットを受けるには、プロジェクトのサイトまたはAboutページでBrave Search APIの帰属表示が必要
- 認証: API Key
- 主な用途: Web検索結果をアプリやLLMに組み込む
- 利用時の注意: **カード登録が必須**（利用上限を設定して無料クレジット内に収められる）。「毎月◯回まで無料」の古い説明が出回っているが、現在はクレジット方式
- 公式: [Pricing](https://api-dashboard.search.brave.com/documentation/pricing)

#### Tavily

- 種類: AIエージェント向けの検索・抽出API
- 無料利用: Researcherプランで月1,000クレジット。カード不要。Basic検索は1クレジット、Advanced検索は2クレジット
- 認証: API Key
- 主な用途: 検索結果の要約や調査エージェントの試作
- 利用時の注意: クレジット消費はエンドポイントによって変わる
- 公式: [Credits & Pricing](https://docs.tavily.com/documentation/api-credits)

#### NewsAPI

- 種類: ニュース検索API
- 無料利用: Developerプランは無料だが、**開発環境のみ**。ステージング・本番・社内利用は不可。localhostはCORS対応
- 認証: API Key
- 主な用途: ニュース一覧UIの試作
- 利用時の注意: 公開した時点でライセンスが失効し、有料契約が必要になる。個人の公開デモにも向かない
- 公式: [Pricing](https://newsapi.org/pricing) / [Terms](https://newsapi.org/terms)

### 気象

#### Open-Meteo

- 種類: 天気・予報・過去データAPI
- 無料利用: 非商用に限り無料。1日10,000回未満、1時間5,000回、1分600回
- 認証: 不要
- 主な用途: 天気を使うWebアプリや家庭内の自動化
- 利用時の注意: 広告やサブスクのあるサイトは非商用にあたらない。表示箇所には「Weather data by Open-Meteo.com」等のリンク（CC BY 4.0）が必要。商用は有料プラン
- 公式: [Terms](https://open-meteo.com/en/terms) / [Pricing](https://open-meteo.com/en/pricing)

#### OpenWeatherMap

- 種類: 天気API
- 無料利用: One Call API 3.0は1日1,000回まで無料。超過は従量課金
- 認証: API Key
- 主な用途: 現在の天気・予報・過去データの取得
- 利用時の注意: 超過課金が発生しうるため、サブスクの上限設定を確認する。他の旧エンドポイントの条件は別
- 公式: [One Call API 3.0](https://openweathermap.org/api/one-call-3) / [Pricing and limits](https://openweathermap.org/full-price)

#### 気象庁 防災情報XML

- 種類: 公共データ（XML電文のPULL配信）
- 無料利用: 無料。利用者登録は不要
- 認証: 不要
- 主な用途: 警報・注意報・地震・火山情報の取得、防災ダッシュボード
- 利用時の注意: 出典に気象庁ホームページである旨を明記する。メンテナンスで配信が止まったり遅れたりしても、気象庁は責任を負わない。確実性が要るなら気象業務支援センター等を使う。XMLの構造が複雑で、パース処理が必要
- 公式: [気象庁 高度利用者向け](https://www.data.jma.go.jp/developer/index.html) / [利用規約](https://www.jma.go.jp/jma/kishou/info/coment.html)
- 自治体との相性: 避難情報や防災情報の通知・可視化のPoCに使いやすい

### 公共データ・行政（日本）

#### e-Stat API

- 種類: 政府統計の総合窓口のAPI
- 無料利用: 無料
- 認証: ユーザー登録後に発行するアプリケーションID（1ユーザー3つまで。第三者への貸与・譲渡は不可）
- 主な用途: 人口・経済・産業などの統計を取得して分析する
- 利用時の注意: 統計表のID・分類コードの理解が必要
- 公式: [API機能](https://www.e-stat.go.jp/api/) / [利用規約](https://www.e-stat.go.jp/api/en/terms-of-use)
- 自治体との相性: 市区町村の比較や政策の基礎データ取得に使いやすい

#### 日本銀行 時系列統計データAPI

- 種類: 公共データ
- 無料利用: 無料（2026-02-18に提供開始）
- 認証: マニュアル参照
- 主な用途: 金利・為替・物価等の時系列を取得。Code API・Layer API・Metadata APIの3種。JSON / CSV
- 利用時の注意: 提供開始から日が浅い。仕様の変更に注意
- 公式: [お知らせ](https://www.boj.or.jp/statistics/outline/notice_2026/not260218a.htm) / [API機能利用マニュアル](https://www.stat-search.boj.or.jp/info/api_manual.pdf)

#### 法人番号システム Web-API

- 種類: 国税庁の公表データAPI
- 無料利用: 無料
- 認証: アプリケーションID（発行届出が必要。添付書類・手数料は不要）
- 主な用途: 法人名・所在地の照会、取引先データの名寄せ
- 利用時の注意: 検証環境（架空データ）にもアプリケーションIDが必要
- 公式: [Web-API](https://www.houjin-bangou.nta.go.jp/webapi/index.html)

#### e-Gov 法令API（Version 2）

- 種類: デジタル庁の法令データAPI
- 無料利用: 無料。利用の登録・申請は不要
- 認証: 不要（公式仕様を参照）
- 主な用途: 条文の検索・取得、特定の時点の条文の取得、廃止法令の検索
- 利用時の注意: 2025-03-14にVersion 2を公開。Version 1は当面継続。OpenAPI（Swagger UI）で試せる
- 公式: [Swagger UI](https://laws.e-gov.go.jp/api/2/swagger-ui/) / [ドキュメント](https://laws.e-gov.go.jp/docs/)
- 自治体との相性: 条例や要綱を作る際の関係法令の確認・突合に使いやすい

#### 国会会議録検索システム API

- 種類: 国立国会図書館の検索用API
- 無料利用: 無料
- 認証: 仕様上キーの記載なし（URLのクエリのみ）
- 主な用途: 国会での発言の検索・分析。会議単位・発言単位のJSON / XML
- 利用時の注意: 1回の返却は最大100件（会議単位の全文は10件）。連続アクセスは数秒空ける
- 公式: [API仕様](https://kokkai.ndl.go.jp/api.html)

#### 国立国会図書館サーチ API / 次世代デジタルライブラリー

- 種類: 書誌・蔵書の検索API（SRU・OpenSearch・OpenURL）と、全文検索の実験サービス
- 無料利用: 無料。営利企業が営利目的で使う場合は申請が必要。データ提供機関が許諾済みのデータは申請不要
- 認証: 用途により申請が必要
- 主な用途: 書籍・資料の検索、全文テキスト検索、IIIFでの画像取得
- 利用時の注意: クレジット表示が必須。次世代デジタルライブラリーは営利目的かつ継続的な利用を除いて申請不要だが、実験的サービスで継続提供は保証されない
- 公式: [API仕様の概要](https://ndlsearch.ndl.go.jp/help/api/specifications) / [次世代デジタルライブラリー](https://lab.ndl.go.jp/service/tsugidigi/)

#### 国土地理院 地理院タイル

- 種類: 地図タイル（PNG / JPEG）、標高（CSVタイル）、ベクトルタイル（提供実験）
- 無料利用: 無料
- 認証: 不要
- 主な用途: 地図表示、標高・地形の可視化
- 利用時の注意: 基本測量成果のタイルをリアルタイムに読み込む利用は、出典の明示のみで申請不要。ベクトルタイルは提供実験中。タイルの種類で条件が違うため一覧で確認する
- 公式: [地理院タイル一覧](https://maps.gsi.go.jp/development/ichiran.html) / [コンテンツ利用規約](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)
- 自治体との相性: 地図・地形・防災マップのPoCの下地に使いやすい

#### 国土数値情報

- 種類: GISデータのダウンロード（Shapefile / GeoJSON / GML）。Web APIではない
- 無料利用: 無料
- 認証: 不要
- 主な用途: 行政区域、公共施設、交通、災害リスク、地価などの可視化・分析
- 利用時の注意: データごとに条件が異なる（商用可、CC BY 4.0など）。利用前に個別ページを確認する
- 公式: [ダウンロードサイト](https://nlftp.mlit.go.jp/ksj/) / [利用約款](https://nlftp.mlit.go.jp/ksj/other/agreement.html)
- 自治体との相性: 公共施設や災害リスクの重ね合わせに使いやすい

#### 不動産情報ライブラリ API

- 種類: 国土交通省の不動産関連オープンデータAPI
- 無料利用: 無料
- 認証: API利用申請 → 審査（5営業日が目安）→ APIキー。ヘッダ `Ocp-Apim-Subscription-Key` に設定する
- 主な用途: 不動産取引価格、地価、都市計画などの取得
- 利用時の注意: すぐには使い始められない。申請が必要
- 公式: [API操作説明](https://www.reinfolib.mlit.go.jp/help/apiManual/) / [API利用申請](https://www.reinfolib.mlit.go.jp/api/request/)

#### 国土交通データプラットフォーム API

- 種類: 国交省系データの検索・取得（GraphQL）
- 無料利用: 利用者向けAPIの利用は無料
- 認証: アカウント登録 + アプリケーション登録によるAPIキー（`apikey` ヘッダ）
- 主な用途: 橋梁・道路・インフラ関連データ等の横断検索
- 利用時の注意: データは「フルオープン」「無償（登録者）」「有償」「限定」の4区分。ライセンスもカタログごとに確認する
- 公式: [API仕様](https://data-platform.mlit.go.jp/api_docs/) / [APIアクセス方法](https://data-platform.mlit.go.jp/api_docs/usage/apiaccess.html)

#### PLATEAU データカタログAPI

- 種類: 3D都市モデルの配信データ一覧（REST / GraphQL）
- 無料利用: 無料。CC BY 4.0等のオープンライセンスで商用も可
- 認証: 記載なし
- 主な用途: 3D Tiles / MVT を使った都市の3D表示、建物データの利用
- 利用時の注意: データの著作権は各地方公共団体に帰属し、公共データ利用規約（第1.0版）に準拠する
- 公式: [API リファレンス](https://docs.plateauview.mlit.go.jp/api/) / [サイトポリシー](https://www.mlit.go.jp/plateau/site-policy/)
- 自治体との相性: 都市計画・防災・景観の可視化PoCに使いやすい

#### アドレス・ベース・レジストリ / ABRジオコーダ

- 種類: デジタル庁の住所データと、住所の正規化を行うOSSのジオコーダ
- 無料利用: データは誰でも無料。ジオコーダは**ローカル実行**
- 認証: 不要
- 主な用途: 住所の表記ゆれを正規化し、町字IDと緯度経度を付与する
- 利用時の注意: クラウドのAPIではなく、手元で動かして使う
- 公式: [ABRジオコーダ](https://lp.geocoder.address-br.digital.go.jp/) / [データセット](https://dataset.address-br.digital.go.jp/)
- 自治体との相性: 住所を含む台帳や申請データの突合に使いやすい

#### 公共交通オープンデータセンター（ODPT）

- 種類: 交通事業者の運行・時刻表データ
- 無料利用: 登録は無料
- 認証: 開発者サイトに登録してAPIキーを発行（CC BY 4.0のデータは登録なしで使えるものもある）
- 主な用途: 鉄道・バスの時刻・位置情報を使った地図アプリ
- 利用時の注意: ライセンスは事業者・データごとに異なる（ODPT基本ライセンス、CC BY 4.0など）。再配布の制限を確認する
- 公式: [開発者サイト](https://developer.odpt.org/) / [規約類の改定](https://www.odpt.org/2021/06/01/news20210601_1/)
- 自治体との相性: コミュニティバスなど地域交通のデータ活用に使いやすい

#### J-Quants API

- 種類: JPXの株価・財務データ配信
- 無料利用: Freeプランあり。データは12週遅れで、過去2年分。APIは毎分5回まで。無料は1年で失効し、再登録できる
- 認証: アカウント登録
- 主な用途: 株価・決算データの分析の試作
- 利用時の注意: リアルタイム用途には向かない。CSVダウンロードは無料に含まれない
- 公式: [プラン](https://jpx-jquants.com/ja/help/plan) / [レート制限](https://jpx-jquants.com/ja/spec/rate-limits)

#### e-Govデータポータル / 東京都オープンデータAPI

- 種類: 中央行政のオープンデータポータル（CKAN互換のメタデータ取得API）と、自治体のAPI
- 無料利用: 無料。メタデータ取得APIは誰でも自由に利用できる
- 認証: e-Govデータポータルのメタデータ取得APIは不要。東京都のAPIは登録不要
- 主な用途: 府省庁・自治体のオープンデータを検索・取得する
- 利用時の注意: 旧「データカタログサイト」は2023年3月末にe-Govデータポータルへ移行した。APIで取れるのはデータセット・リソースなどのメタデータで、データ本体はCSV等のファイルを別に取得する。データごとにライセンス・更新状況が違う
- 公式: [e-Govデータポータル メタデータ取得API](https://data.e-gov.go.jp/data/api_guide) / [東京都APIの使い方](https://spec.api.metro.tokyo.lg.jp/spec/usage) / [東京都カタログ](https://catalog.data.metro.tokyo.lg.jp/)
- 自治体との相性: 他自治体との比較や、統計データとの突合に使いやすい

### 海外のオープンデータ・学術・為替・地図

#### Wikimedia API

- 種類: Wikipediaなどの記事・メタデータAPI
- 無料利用: 無料
- 認証: 不要。ただし連絡先を含む `User-Agent` を付ける
- 主な用途: 記事の要約・関連語の取得、LLMの補助知識
- 利用時の注意: 識別のないリクエストは上限が低い。上限は分あたりで管理され、超えると429
- 公式: [Rate limits](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits)

#### arXiv API

- 種類: 論文のメタデータ検索
- 無料利用: 無料
- 認証: 不要
- 主な用途: 論文の検索・トレンド分析
- 利用時の注意: 3秒に1リクエスト、同時接続は1つ。複数のマシンで制限を回避しない
- 公式: [Terms of Use](https://info.arxiv.org/help/api/tou.html)

#### Crossref REST API

- 種類: DOI・論文のメタデータ
- 無料利用: 無料
- 認証: 不要。`mailto` を付けるとPolite poolになり、上限が上がる
- 主な用途: 論文情報の補完、引用関係の調査
- 利用時の注意: 単一レコードの取得と、検索・フィルタでレート制限が違う
- 公式: [Access and authentication](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/)

#### OpenAlex

- 種類: 論文・著者・機関のカタログ
- 無料利用: 無料アカウントに1日$1分の利用枠。支払い方法は不要
- 認証: APIキー（2026-02-13以降は必須。無料で発行できる）
- 主な用途: 研究動向の分析、機関ごとの論文数の集計
- 利用時の注意: 検索は1回あたりの単価が高く、リスト取得や単体取得は安い。単価は公式を参照
- 公式: [Authentication](https://developers.openalex.org/guides/authentication) / [Pricing](https://help.openalex.org/access/pricing/)

#### Frankfurter

- 種類: 為替レートAPI
- 無料利用: 無料。公開エンドポイントにキーは不要
- 認証: 不要
- 主な用途: 為替換算、過去レートの時系列
- 利用時の注意: 中央銀行などの公表レートを集めたもの。取引用のリアルタイムレートではない
- 公式: [Frankfurter](https://frankfurter.dev/)

#### Nominatim（公開インスタンス）

- 種類: OpenStreetMapのジオコーディング
- 無料利用: 無料だが、1秒に1リクエストが絶対の上限で、大量利用は禁止
- 認証: 不要。`User-Agent` または `Referer` で自分のアプリを識別する
- 主な用途: 住所・地名の検索、逆ジオコーディング
- 利用時の注意: 帰属表示が必要。一括処理や定期的なスクリプトは制限される。大量に使うなら自前で動かす
- 公式: [Usage Policy](https://operations.osmfoundation.org/policies/nominatim/)

### 開発・メディア・実用

#### GitHub REST API

- 種類: GitHubのデータ取得・操作API
- 無料利用: 無料。未認証は1時間60回、認証済みは1時間5,000回。`GITHUB_TOKEN` は1リポジトリあたり1時間1,000回
- 認証: 不要 / Personal Access Token
- 主な用途: リポジトリ・PR・Issueの分析、自動化、Actionsとの連携
- 利用時の注意: 未認証はIPで数えられるため、すぐに上限に当たる
- 公式: [Rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)

#### YouTube Data API

- 種類: 動画・チャンネル情報のAPI
- 無料利用: 1日あたり10,000ユニットが既定のクォータ。一覧の読み取りは1ユニット前後、書き込みは50ユニット前後
- 認証: API Key / OAuth
- 主な用途: 動画・再生リストのメタデータ分析
- 利用時の注意: メソッドごとに消費ユニットが違う（検索系は特に確認が必要）。無効なリクエストも1ユニット以上を消費する。上限の引き上げは公式の監査・申請手続きが必要
- 公式: [Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost) / [Overview](https://developers.google.com/youtube/v3/getting-started)

#### LINE Messaging API

- 種類: LINE公式アカウントのBot・配信API
- 無料利用: コミュニケーションプラン（月額0円）で月200通まで。追加配信はできない
- 認証: チャネルアクセストークン
- 主な用途: 通知Bot、問い合わせ受付の試作
- 利用時の注意: 通数は「送信回数 × 友だち数」で数える。ライト以上のプランは月額固定費がかかる
- 公式: [Messaging APIの料金](https://developers.line.biz/ja/docs/messaging-api/pricing/)
- 自治体との相性: 住民向けの通知・問い合わせ窓口の小規模なPoCに使いやすい

#### Unsplash API / Pexels API

- 種類: 写真の検索API
- 無料利用: Unsplashは開発中（Demo）が1時間50回、承認後は1時間1,000回。Pexelsは既定で1時間200回・月20,000回
- 認証: API Key
- 主な用途: UIモックやブログ画像の自動取得
- 利用時の注意: どちらも帰属表示が必要。Unsplashは返されたURLでのホットリンクが必須。Pexelsは上限の引き上げ申請が現在一時停止中
- 公式: [Unsplash API Terms](https://unsplash.com/api-terms) / [Pexels API](https://www.pexels.com/api/documentation/) / [Pexels FAQ](https://help.pexels.com/hc/en-us/articles/47677890260761-Is-the-Pexels-API-free-to-use)

#### TMDB

- 種類: 映画・TV情報
- 無料利用: 非商用に限り無料
- 認証: API Key
- 主な用途: 映画一覧・推薦UIの試作
- 利用時の注意: 帰属表示とTMDBロゴが必要。有料アプリ、広告・収益化を伴うサイト、AI学習への利用は別契約が必要
- 公式: [API Terms of Use](https://www.themoviedb.org/api-terms-of-use)

#### DeepL API Developer

- 種類: 翻訳API
- 無料利用: **累計100万文字**まで。月次の無料枠ではなく、上限に達してもリセットされない。**初回付与型**に近い
- 認証: API Key
- 主な用途: 日本語・英語の翻訳を組み込んだ試作、多言語化の検証
- 利用時の注意: 上限に達したら、有料のDeepL API Growthへ移行する。旧「DeepL API Free」（月50万文字）は新規購入できない。商用利用などの条件は利用規約を確認する
- 公式: [DeepL API plans](https://support.deepl.com/hc/en-us/articles/360021200939-DeepL-API-plans) / [Usage and limits](https://developers.deepl.com/docs/resources/usage-limits)

#### Google Cloud Vision（OCR）

- 種類: 画像・文書のOCR
- 無料利用: 毎月最初の1,000ユニットが無料
- 認証: Google Cloudの認証
- 主な用途: 画像やスキャン文書からの文字抽出
- 利用時の注意: 超過分は従量課金。複雑な帳票はDocument AIなど別サービスの価格を確認する
- 公式: [Pricing](https://cloud.google.com/vision/pricing)

#### VOICEVOX ENGINE

- 種類: 音声合成エンジン（OSS）。**ローカル実行**
- 無料利用: 商用・非商用とも利用可。ただしクレジット表記が必要
- 認証: 不要。起動すると `127.0.0.1:50021` でHTTP APIが使える
- 主な用途: LLMの応答の読み上げ、ナレーション生成
- 利用時の注意: クラウドの無料枠ではなく、自分の端末やサーバーで動かす。生成した音声はキャラクターごとの規約にも従い、規約が違う場合は厳しい方が優先される。エンジンのライセンスはLGPL v3と、ソース公開が不要な別ライセンスのデュアル
- 公式: [利用規約](https://voicevox.hiroshiba.jp/term/) / [リポジトリ](https://github.com/VOICEVOX/voicevox_engine)

### APIカタログ

#### public-apis

- 種類: 公開APIの一覧（GitHub）
- 使い方: 目的のカテゴリを開き、認証（`No` / `apiKey` / `OAuth`）、HTTPS、CORSの列で絞る
- 利用時の注意: 無料枠の条件は載っていない。リンク切れや提供終了が混ざりうるため、必ず公式で確認する。READMEの冒頭にスポンサーの広告がある。日本の公共APIはほとんど載っていない（2026-10-02時点のクローンで、e-Stat・RESAS・気象庁は確認できなかった）
- 公式: [public-apis/public-apis](https://github.com/public-apis/public-apis)

#### free-for-dev

- 種類: 無料枠のあるサービスの一覧（GitHub）
- 使い方: 「APIs, Data and ML」「Generative AI」など、インフラ寄りのカテゴリから探す
- 利用時の注意: インフラ・DevOps向けの一覧で、掲載条件は「Trialではなく無料枠があること。期限付きなら1年以上」。APIの網羅を目的にしていない
- 公式: [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev)

#### publicapi.dev

- 種類: 公開APIのディレクトリ
- 使い方: カテゴリと認証方式（API Key / Bearer / OAuth / 認証なし）で絞る
- 利用時の注意: 登録は事業者の申請を含む。無料枠の最新条件は各APIの公式で確認する
- 公式: [publicapi.dev](https://publicapi.dev/)

## 組み合わせ例

小さく試せる組み合わせの例。いずれも既存プロジェクトとは無関係に、単独で試作できる。

- **Brave Search / Tavily + Gemini / Groq**
  → Web検索結果の要約・分類。検索は無料クレジットの範囲に収め、要約は無料枠のLLMで回す
- **e-Stat + 国土地理院 + 国土数値情報**
  → 地域統計の地図可視化。市区町村ごとの人口などを、行政区域のGISデータに重ねる
- **気象庁 防災情報XML / Open-Meteo + 地図**
  → 防災・気象ダッシュボード。Open-Meteoは非商用の範囲で使う
- **GitHub API + LLM（OpenRouter / Gemini / Groq など）**
  → 開発履歴やリポジトリの分析。PRやIssueの傾向をまとめる
- **国会会議録 API + e-Gov 法令API + LLM**
  → ある法令に関する国会での議論と条文の突合。時点指定で当時の条文を引ける
- **ABRジオコーダ + 自治体オープンデータ + 国土地理院**
  → 住所を含む表データの正規化と地図表示
- **日銀API + Frankfurter + J-Quants**
  → 金利・為替・株価の経済指標ダッシュボード
- **LLM + VOICEVOX**
  → 応答の読み上げ。音声合成はローカルで完結する
- **ODPT + 地図タイル**
  → 地域の公共交通の位置・時刻表の表示

## 誤認しやすい点

- **RESAS-API は終了している**。新規受付の停止に続き、2025-03-24にサービスが終了した。RESASの画面は継続しているが、APIとしては使えない
- **Brave Search API の無料枠は「毎月◯回」ではなく、毎月$5分のクレジット**。カード登録が必須で、帰属表示が条件
- **Cohere の無料キーは Trial**。商用・本番は不可
- **NewsAPI の無料プランは開発環境専用**。公開した時点で使えなくなる
- **TMDB と Open-Meteo は「無料」ではなく非商用のみ無料**。広告やサブスクのあるサイトは商用になる
- **Gemini は課金アカウントを紐付けると、そのプロジェクトは全て課金対象**
- **Hugging Face の無料分は月次の少額クレジット**。「Inference は無料」とは言えない
- **Jina と Voyage の無料トークンは初回付与型**。毎月の無料枠ではない
- **LINE Messaging API の無料プランは月200通で、超えると配信できない**
- **Spotify Web API は、現在の開発モードではPremiumアカウントが必要で、ユーザー数・アプリ数に上限がある**。非商用の学習用途向けに絞られているため、個人開発の候補から外した
- **GitHub Models は2026-07-30に終了している**。Playground・モデルカタログ・Inference API・BYOKのすべてが利用できない。Copilotとは別サービスで、掲載しない
- **DeepL API Free は新規購入できないが、後継の DeepL API Developer がある**。ただし月次の無料枠ではなく、累計100万文字の上限で、リセットされない
- **国土数値情報は「API」ではなくファイル配布**。ただし構造化データとしてプログラムから扱える
- **次世代デジタルライブラリーは実験的サービス**。継続提供を前提にしない
- **VOICEVOX は無料のクラウドAPIではなく、ローカルで動かすOSS**
- **「La Plateforme」は現在「Mistral Studio」**。「Hugging Face Inference」は現在「Inference Providers」

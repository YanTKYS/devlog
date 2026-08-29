# devlog

複数の GitHub リポジトリにまたがる開発記録を一箇所に集約するためのリポジトリです。

- 「何が起きたか」（merged PR / Release / デフォルトブランチへの直接コミット）は
  GitHub Actions が GitHub API から自動収集し、`logs/` に Markdown として蓄積します
- 「なぜそうしたか」（設計判断、技術的な気付きなど、人間が残すべき内容）は
  `projects/` と `notes/` に、人が手で書きます

自動生成ログと人間のメモを混在させないことで、後から読み返しやすい状態を保ちます。

## 構成

```text
devlog/
├─ README.md
├─ config/
│  └─ repositories.yml   # 収集対象リポジトリの一覧
├─ logs/
│  ├─ YYYY/YYYY-MM.md    # 自動収集ログ（月単位・正本）
│  ├─ today.md           # 今日の記録だけを抜き出した閲覧用（自動生成）
│  ├─ yesterday.md       # 昨日の記録だけを抜き出した閲覧用（自動生成）
│  └─ latest.md          # 全リポジトリの最新1件を一覧化した閲覧用（自動生成）
├─ projects/              # プロジェクトごとの判断・メモ（人間が記録）
├─ notes/                 # プロジェクト横断の知見（人間が記録）
├─ scripts/
│  └─ collect.py          # 収集スクリプト本体
└─ .github/workflows/
   └─ collect.yml         # 定期実行・手動実行ワークフロー
```

### logs/

`logs/YYYY/YYYY-MM.md` に、日付 → リポジトリ単位で以下を記録します。

```markdown
# 2026-08

## 2026-08-19

### markdownutil

- PR #27 UI調整
  - merged
  - https://github.com/YanTKYS/markdownutil/pull/27
```

- 記録単位は PR です。PR 内の個々のコミットは展開しません
- 同じ変更が PR 経由で既に記録されている場合、直接コミットとしては重複記録しません
- Release・直接コミットも、それぞれ `release` / `direct commit` として区別できる形で記録します
- 内容は GitHub API から取得できる事実のみです。AI による要約・推測は行いません
- devlog 自身の収集では、このワークフローが push する `chore(logs): update devlog entries`
  は direct commit として記録しません（自動 commit を再収集する自己循環を避けるため。
  他リポジトリの同名 commit は通常どおり記録します）
- 日付は GitHub API が返す UTC 時刻を JST（UTC+9 固定オフセット、DST なし）に変換して
  決定します。例えば JST 8/20 01:00 にマージされた PR は `2026-08-20` に記録されます
  （UTC のまま `.date()` を取ると `2026-08-19` になってしまうため、開発日誌として
  不自然にならないよう JST 変換してから日付を確定させています）。日本は DST がないため
  固定オフセットで十分と判断し、実装は `zoneinfo`（IANA タイムゾーンデータが必要で、
  実行環境によっては存在しない場合がある）ではなく、Python 標準ライブラリの
  `datetime.timezone(timedelta(hours=9))` のみを使っています
- `logs/` は自動生成物です。人間が残したい内容は `projects/` `notes/` に書いてください（詳細は各ディレクトリの README を参照）

#### `today.md` / `yesterday.md` / `latest.md`

`logs/YYYY/YYYY-MM.md` が正本です。`logs/today.md` `logs/yesterday.md` `logs/latest.md` は、
そこから抜き出して毎回作り直す閲覧用の自動生成ファイルで、手で編集しても次回実行時に
上書きされます。

- `today.md` / `yesterday.md`: JST 基準の今日・昨日の記録だけを表示します
  （該当する記録がない日でも生成されます）
- `latest.md`: `config/repositories.yml` の全リポジトリについて、devlog に収集済みの
  最新イベント（merged PR / Release / direct commit のいずれか）1件を一覧にします。
  記録が一度もないリポジトリも `記録なし` として必ず表示します

いずれも内容は最後に自動収集が走った時点までのものです。収集は1日1回（JST 06:00）なので、
`today.md` は「たった今」ではなく「最後の収集時点までの今日」を表し、`latest.md` も
GitHub 上の最終更新をその場で問い合わせた結果ではありません。

## 自動収集の仕組み

`.github/workflows/collect.yml` が `scripts/collect.py` を実行し、
`config/repositories.yml` に列挙されたリポジトリから

- マージ済み Pull Request
- Release（draft を除く）
- Pull Request を経由せずデフォルトブランチへ直接入ったコミット
  （コミットに紐づく merged PR がある場合はそちらとして記録済みとみなし、スキップします）

を取得し、対象月の `logs/YYYY/YYYY-MM.md` に追記します。

一覧の取得（PR・Release・コミット）は REST API です。コミットが merged PR に属するかの
判定だけは、コミット1件ごとに1リクエストを要する REST の代わりに GraphQL API へ
まとめて（既定 30 件ずつ）問い合わせます。認証には同じ `DEVLOG_READ_TOKEN` を使います。

**重複防止**: 別途の状態ファイルは持たず、各イベントの GitHub URL をそのまま重複判定の
キーとして使います。追記前に、対象月のファイル内に同じ URL が既に含まれていないかを
確認し、含まれていれば追記をスキップします。`logs/` 自体が唯一の正とするデータになる
ため、実行が数日飛んでも（`LOOKBACK_DAYS` 日分を毎回見直すので）取りこぼしにくく、
手動編集した行が消えたり増えたりしにくい、壊れにくい方式です。

## `config/repositories.yml` への対象追加方法

`repositories:` の下に `owner/repo` の形式で1行追記するだけです。

```yaml
repositories:
  - YanTKYS/nestsuite
  - YanTKYS/your-new-repo
```

private リポジトリを追加する場合は、下記の Secret 設定も必要です。

## GitHub Actions の実行方法

- **定期実行**: 毎日 1 回（UTC 21:00 = JST 06:00）自動実行されます。この場合、取得対象は
  直近 7 日分（`LOOKBACK_DAYS`）です。毎日走る前提での重複分を含んだ日数で、Actions が
  数日止まっても取りこぼしません。それ以上長く止まった場合は、下記の手動実行で
  `lookback_days` に任意の日数を指定して取り込めます
- **手動実行**: GitHub の Actions タブから `Collect devlog` ワークフローを選び、
  `Run workflow` を押すことで即時実行できます（`workflow_dispatch`）
- 収集結果に変更があった場合のみ `logs/` の変更を commit・push します。
  変更がない場合は commit を作成しません

### 過去分のバックフィル（初回導入時など）

手動実行時のみ、`lookback_days`（取得対象日数）を指定できます。空欄なら通常運用と同じ
7日です。導入初回に過去の履歴をまとめて取り込みたい場合や、Actions が長期間止まって
いた場合は、`Run workflow` 実行時に `lookback_days` へ `35` `365` `730` など必要な日数を
指定してください。一度に全履歴を取り込む必要はなく、必要な範囲だけ何度でも指定し直せます
（`logs/` への重複記録は発生しません）。

ページネーションは指定した `lookback_days` の範囲を実際に走査し終えるまで続く実装なので、
`730` 日のように長い期間を指定しても、途中で黙って取得を打ち切ることはありません
（暴走防止の安全上限のみ設けてあり、万一到達した場合はワークフローのログに warning が
出ます。通常の運用では発生しません）。

## private リポジトリ取得用 Secret の設定

対象リポジトリに private が含まれる場合、`devlog` リポジトリの
Settings → Secrets and variables → Actions に、以下の Secret を登録してください。

- **Secret 名**: `DEVLOG_READ_TOKEN`
- **値**: GitHub の Fine-grained personal access token
  - 対象は収集したいリポジトリのみに限定してください（Only select repositories）
  - Permissions は以下の read-only 権限のみで十分です
    - Contents: Read-only（コミット・Release の取得に使用）
    - Pull requests: Read-only（PR の取得に使用）
    - Metadata: Read-only（必須項目として自動付与されます）
  - 書き込み権限は不要です

`DEVLOG_READ_TOKEN` が未設定の場合、ワークフローが自動的に持つ `GITHUB_TOKEN` で
取得を試みますが、これは public リポジトリの読み取りにしか使えません。

## ローカルで試す方法

Python 3.8 以降があれば、依存ライブラリのインストールなしでそのまま実行できます
（OS のタイムゾーンデータベースにも依存しません）。

```bash
export DEVLOG_READ_TOKEN=ghp_xxxxxxxx   # 必須。GraphQL は未認証だと使えないため
export DEVLOG_LOOKBACK_DAYS=365          # 省略可。省略時は7日(通常運用と同じ)
python3 scripts/collect.py
```

`config/repositories.yml` を読み込み、`logs/YYYY/YYYY-MM.md` を生成・更新します。
再実行しても、既に記録済みの内容は重複追加されません。

トークンなしでも PR・Release は public リポジトリから取得できますが、direct commit の
判定に使う GraphQL は未認証では利用できないため、その分は warning を出してスキップします
（GitHub Actions 上では `GITHUB_TOKEN` があるため常に認証されます）。

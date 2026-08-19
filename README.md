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
│  └─ YYYY/YYYY-MM.md    # 自動収集ログ（月単位）
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
- `logs/` は自動生成物です。人間が残したい内容は `projects/` `notes/` に書いてください（詳細は各ディレクトリの README を参照）

## 自動収集の仕組み

`.github/workflows/collect.yml` が `scripts/collect.py` を実行し、
`config/repositories.yml` に列挙されたリポジトリから

- マージ済み Pull Request
- Release（draft を除く）
- Pull Request を経由せずデフォルトブランチへ直接入ったコミット
  （コミットに紐づく merged PR がある場合はそちらとして記録済みとみなし、スキップします）

を取得し、対象月の `logs/YYYY/YYYY-MM.md` に追記します。

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

- **定期実行**: 毎日 1 回（UTC 21:00 = JST 06:00）自動実行されます
- **手動実行**: GitHub の Actions タブから `Collect devlog` ワークフローを選び、
  `Run workflow` を押すことで即時実行できます（`workflow_dispatch`）
- 収集結果に変更があった場合のみ `logs/` の変更を commit・push します。
  変更がない場合は commit を作成しません

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

Python 3.9 以降があれば、依存ライブラリのインストールなしでそのまま実行できます。

```bash
export DEVLOG_READ_TOKEN=ghp_xxxxxxxx   # private を含めるならセット。public のみなら未設定でも可
python3 scripts/collect.py
```

`config/repositories.yml` を読み込み、`logs/YYYY/YYYY-MM.md` を生成・更新します。
再実行しても、既に記録済みの内容は重複追加されません。

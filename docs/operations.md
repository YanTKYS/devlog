# 運用ガイド

[README](../README.md) に戻る。

## ログ収集の設定

### 収集対象を追加する

[config/repositories.yml](../config/repositories.yml) の `repositories:` に、
`owner/repo` 形式で1行追加します。private リポジトリは、次のトークンの対象にも含めてください。

### 読み取り用トークンを設定する

devlog リポジトリの Settings → Secrets and variables → Actions に、
`DEVLOG_READ_TOKEN` を登録します。Fine-grained personal access token の対象を
収集したいリポジトリに限定し、次の最小権限を付けてください。

| 権限 | 設定・用途 |
| --- | --- |
| Contents | Read-only：コミット・Release の取得 |
| Pull requests | Read-only：PR の取得 |
| Metadata | Read-only：必須権限として自動付与 |

収集用トークンに書き込み権限は不要です。トークンをファイルやコミットに含めないでください。

未設定の場合、[収集ワークフロー](../.github/workflows/collect.yml) は自動提供の
`GITHUB_TOKEN` を使います。他の private リポジトリの取得には、そのリポジトリを対象にした
`DEVLOG_READ_TOKEN` が必要です。

## 定期実行・手動実行・バックフィル

GitHub Actions の **Collect devlog** が毎日 JST 06:00（UTC 21:00）に、直近7日分を収集します。
手動実行は Actions → Collect devlog → Run workflow から行います。

初回導入や長期間停止した後は、Run workflow の `lookback_days` に取得対象の日数
（例：`35`、`365`、`730`）を指定してください。空欄なら7日です。
同じ期間を再実行したときの重複防止と、ログの更新対象は [logs/README.md](../logs/README.md) を参照してください。
走査が安全上限に達した場合は warning が出るので、大きなバックフィルでは実行ログを確認してください。

収集結果や閲覧用ファイルに変更があった場合だけ、ワークフローが `logs/` を commit・push します。
各リポジトリの取得に失敗しても warning を出して続行するため、終了ステータスだけでなく
実行ログも確認してください。

## Pages の公開範囲を設定する

### リポジトリの公開許可リスト

**GitHub Pages は公開サイトです。** [config/pages.yml](../config/pages.yml) の
`public_repositories:` に書かれ、かつ `config/repositories.yml` に登録されたリポジトリだけが
掲載されます。未指定のリポジトリは、記録もリポジトリ名も Pages 用データに出力されません。

掲載するときは `owner/repo` 形式で1行追加します。**private リポジトリは追加しないでください。**
追加するとタイトル・URL が公開されます。この設定はサイト生成時の絞り込みであり、
収集対象やリポジトリ内の `logs/` の内容を変更・秘匿するものではありません。

### 公開するノート

[scripts/build_site.py](../scripts/build_site.py) の `PUBLIC_NOTES` に列挙されたノートだけを
公開します。現在の対象は [free-apis.md](../notes/free-apis.md) と
[ai-coding-tools.md](../notes/ai-coding-tools.md) です。追加時は次の2か所を更新してください。

1. `PUBLIC_NOTES` に `id`（英小文字とハイフン）・`source`・`description` を追加する。
2. [.github/workflows/pages.yml](../.github/workflows/pages.yml) の push の `paths` に、
   そのファイルを追加する。ノート変更時に Pages を更新するために必要です。

`notes/` や `data/deepresearch/` が丸ごとサイトへコピーされることはありません。
公開対象ノートへの相対リンクは閲覧UI内のリンクに、それ以外のファイルへの相対リンクは
GitHub 上の元ファイルへのリンクになります。公開する本文とリンク先を確認してください。

## Pages を有効化・デプロイする

初回はリポジトリの Settings → Pages → Build and deployment → **Source** を
**GitHub Actions** に設定します。Pages のデプロイ用 PAT は不要です。

**Deploy Pages** は、テスト → 静的サイト生成 → GitHub 公式 Actions によるデプロイを行います。
実行タイミングは次のとおりです。

- `main` の Collect devlog が成功した後。
- `main` にログ・UI・生成スクリプト・設定・公開ノートなどの対象ファイルが push されたとき。
  正確な対象は [pages.yml の `paths`](../.github/workflows/pages.yml) を参照してください。
- Actions → Deploy Pages → Run workflow からの手動実行。

自動収集の `GITHUB_TOKEN` による push では別ワークフローを起動できないため、
収集後のデプロイは `workflow_run` で起動します。デプロイ処理自体はログを収集しません。

サイトは既存ログから生成したデータと静的ファイルを配信し、表示時に GitHub API を呼びません。
「今日・昨日」は閲覧者の時計ではなく、最後の収集日（`logs/today.md` の見出し、JST）を基準にします。

## ローカルで開発・確認する

以下のコマンドはリポジトリのルートで実行します。Python は CI と同じ **3.12** を推奨します。
追加の Python パッケージは不要です。UIのテストには `node --test` が使える Node.js も必要です。

### サイト生成・表示・テスト

```bash
python3 scripts/build_site.py
python3 -m http.server --bind 127.0.0.1 -d _site 8000
```

`_site/` は Git 管理対象外の生成先です。再ビルド時には作り直されます。
生成後は HTTP サーバー経由で確認してください。`file://` では JSON データを読み込めません。
ソースを編集したら再ビルドし、ページを再読み込みします。

テストは別ターミナルで実行できます。

```bash
python3 -m unittest discover -s tests
node --test tests/site_lib.test.js tests/markdown_lib.test.js
```

### ログを収集する

`DEVLOG_READ_TOKEN`（または `GITHUB_TOKEN`）を安全な方法で環境変数に設定してから実行します。
権限は上記「読み取り用トークンを設定する」と同じです。

```bash
python3 scripts/collect.py
```

通常は直近7日分です。過去分を取得するときは環境変数で日数を指定します。

```bash
DEVLOG_LOOKBACK_DAYS=365 python3 scripts/collect.py
```

収集は追跡対象の `logs/` を更新するため、実行後に差分を確認してください。
public リポジトリの PR・Release はトークンなしでも取得できますが、直接コミットの判定に使う
GraphQL は認証が必須です。トークンなしではその取得が warning 付きでスキップされます。

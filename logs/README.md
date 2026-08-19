# logs/

`YYYY/YYYY-MM.md` に、対象リポジトリの merged PR・Release・デフォルトブランチへの
直接コミットを、GitHub Actions が自動収集して追記する場所です。

- 記録単位は PR（PR内の個々のコミットは展開しません）
- 同じ変更が PR 経由で既に記録済みの場合、直接コミットとしては重複記録しません
- 内容は GitHub API から取得できる事実のみで、要約や推測は含みません
- ファイルは `python3 scripts/collect.py`（または GitHub Actions）が生成・更新します。手で編集しても構いませんが、見出しの形式（`# YYYY-MM` / `## YYYY-MM-DD` / `### repo`）を崩すと次回実行時のマージに影響します

設計判断や技術的な気付きなど、人が書き残したい内容は `projects/` や `notes/` に記録してください。

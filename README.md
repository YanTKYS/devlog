# devlog

複数の GitHub リポジトリにまたがる開発記録と、人が残す知見を集約するリポジトリです。

- merged PR・Release・デフォルトブランチへの直接コミットを GitHub Actions で自動収集し、Markdown として蓄積します。
- 設計判断や技術的な気付きは、プロジェクト別のメモや横断的なノートに手で記録します。

## 開発ログ・ノートを見る

[GitHub Pages の閲覧UI](https://yantkys.github.io/devlog/) で、公開対象の開発ログとノートを読めます。
ログは月・リポジトリ・種別で絞り込めます。「今日・昨日」は最後の収集時点の記録です。

## ファイルの案内

| 場所 | 内容 |
| --- | --- |
| [logs/](logs/README.md) | 自動収集したログと閲覧用の一覧 |
| [projects/](projects/README.md) | プロジェクトごとの判断・メモ |
| [notes/](notes/README.md) | プロジェクト横断の知見・比較資料 |
| [data/deepresearch/](data/deepresearch/) | 調査原文 |
| [config/](config/) | 収集対象と Pages 公開対象の設定 |
| [scripts/](scripts/) | ログ収集・サイト生成 |
| [site/](site/) | 閲覧UIの HTML・CSS・JavaScript |
| [tests/](tests/) | データ生成・閲覧UIのテスト |

## 設定・運用を調べる

[運用ガイド](docs/operations.md) に、収集対象・認証の設定、定期／手動実行、バックフィル、
Pages の公開範囲・デプロイ、ローカル開発の手順をまとめています。
ログの形式と正本・派生ファイルの関係は [logs/README.md](logs/README.md) を参照してください。

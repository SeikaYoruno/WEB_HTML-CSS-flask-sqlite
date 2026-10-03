# バックエンド編

サーバーの中で動く**Python・Flask・データベース**を学びます。

## ゴール

まず[01_intro](01_intro/)で、コードを貼り付けながらFlaskとSQLiteのメモ帳を1時間で作り、サーバーで動くアプリの全体像をつかみます。

次の[02_memo_app_frontend](02_memo_app_frontend/)では、フロントエンド編で学んだJavaScriptを使って、ブラウザだけで動くメモアプリ（データは`localStorage`に保存）を作ります。完成したアプリを使ってみると、「別の端末から見られない」「誰のメモか区別できない」といった限界が見えてきます（[02_memo_app_frontendの最後の節](02_memo_app_frontend/#このアプリの限界とバックエンド編)）。

03章〜17章では、同じメモ帳アプリの**保存先をサーバー（Flask＋データベース）に移し**、データベース・ログイン・アプリの構造化（Blueprint）までを学びます。完成形は[02_backend/100_memo_api](100_memo_api/)で、01〜17章の内容だけで作られています。各章で学んだ内容は、[02_backend/00_my_app](00_my_app/)に積み上げていきます。

環境構築は[00_docs/setup/backend.md](../00_docs/setup/backend.md)（ライブラリは[00_docs/setup/requirements.txt](../00_docs/setup/requirements.txt)でまとめてインストール）、章をまたいで出てくる用語は[00_docs/glossary](../00_docs/glossary/)（用語集）にまとめています。

## 章の構成

| 章 | 内容 |
|---|---|
| [01_intro](01_intro/) | イントロダクション：コードを貼り付けながら、FlaskとSQLiteで動くメモ帳を1時間で作る |
| [02_memo_app_frontend](02_memo_app_frontend/) | 出発点：ブラウザだけで動くメモアプリを完成させ、その限界を確かめる（JavaScript） |
| [03_function](03_function/)〜[08_request](08_request/) | Pythonの関数とデコレータ、Flaskの基本（ルーティング・テンプレート・リクエスト） |
| [09_forms](09_forms/)〜[14_flask_migrate](14_flask_migrate/) | フォームとサーバー側の入力チェック、SQL・データベース |
| [15_login](15_login/)〜[17_blueprint](17_blueprint/) | ログイン・型ヒント・アプリの構造化（Blueprint） |
| [100_memo_api](100_memo_api/) | 完成形：01〜17章の内容を統合し、画面にはフロントエンド編の内容を取り入れたメモ帳アプリ（最初に動かして、ゴールを体験しておく） |
| [00_my_app](00_my_app/) | 自分だけの統合アプリ：各章で学んだ内容をここに積み上げていく |

各章の詳しい内容は、トップの[README.md](../README.md#バックエンド編02_backend)のチャプター一覧を参照してください。

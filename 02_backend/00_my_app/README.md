# 00 自分だけの学習統合アプリ

バックエンド編の各チャプターはテーマごとに独立したサンプルですが、`02_backend/00_my_app`は**自分で学んだ内容を1つのアプリに積み上げていく**ための場所です。各章を終えるたびに、その章で学んだ機能をこの`app.py`（や、必要に応じて分割したファイル）に反映していきます。

## 1つのアプリを育てる

`02_backend/02_memo_app_frontend`で完成させたブラウザ版のメモアプリ（[02_backend/02_memo_app_frontend](../02_memo_app_frontend/)）と同じ画面・同じデータの形のまま、**データの保存先をブラウザ（`localStorage`）からサーバー（Flask＋データベース）に移し**、機能を少しずつ育てていきます。

| 対象チャプター | 積み上がる機能 |
|---|---|
| `02_backend/02_memo_app_frontend` | （出発点）フロントエンド編で学んだJavaScriptで、ブラウザだけで動くメモアプリを作る。HTML・CSS・JavaScript・`localStorage` |
| `02_backend/03_function`〜`02_backend/08_request` | Flaskでページを配信する・一覧と詳細・テンプレート・リクエスト |
| `02_backend/09_forms`〜`02_backend/14_flask_migrate` | サーバー側の入力チェック付きの追加フォーム・データベースへの保存 |
| `02_backend/15_login`〜`02_backend/17_blueprint` | ログイン・型ヒント・Blueprintでのアプリの構造化 |

`02_backend/04_flask_basic`からは、フロントエンド編で作ったページをFlaskで配信します。バックエンド編は`02_backend/17_blueprint`までです。テーマの切り替えは一切なく、`02_backend/100_memo_api`が最終的な完成形です。

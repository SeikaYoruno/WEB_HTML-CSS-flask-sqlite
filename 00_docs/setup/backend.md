# 環境構築（バックエンド編）

> [バックエンド編](../../02_backend/)を始める前に行います。最初の章は[02_backend/01_intro](../../02_backend/01_intro/)です。ブラウザ・VS Codeの入れ方は[frontend.md](frontend.md)にあります（フロントエンド編から進めている場合は、用意済みです）。

バックエンド編で使うPython・ライブラリ・VS Codeの拡張機能を用意します。最初に1回だけ行えば、バックエンド編のすべての章で使えます。フロントエンド編（HTML・CSS・JavaScript）だけを進める間は不要です（VS Codeの拡張機能は、[vscode.md](vscode.md#htmlcssフロントエンド)を参照してください）。

## 目次

1. [Pythonを確かめる](#pythonを確かめる)
2. [仮想環境を作る](#仮想環境を作る)
3. [ライブラリをインストールする](#ライブラリをインストールする)
4. [VS Codeの拡張機能を入れる](#vs-codeの拡張機能を入れる)

---

## Pythonを確かめる

ターミナル（VS Codeなら「表示」→「ターミナル」）で、Pythonのバージョンを確かめます。**3.10以上**が必要です（このカリキュラムは3.11・3.13で動作確認しています）。

```bash
python3 --version     # Mac
python --version      # Windows
```

表示されない・3.9以下のときは、[python.org](https://www.python.org/downloads/)から最新版をインストールします（Windowsでは、インストーラーの最初の画面で「Add python.exe to PATH」にチェックを入れます）。

---

## 仮想環境を作る

**仮想環境**は、このカリキュラム専用のライブラリ置き場です。パソコン全体のPythonを汚さずに、決まったバージョンのライブラリを入れられます。リポジトリの一番上のフォルダ（`README.md`があるフォルダ）で作ります。

```bash
cd （このリポジトリのフォルダ）
python3 -m venv flaskenv          # Mac（Windowsは python -m venv flaskenv）
```

作った仮想環境を**有効にします**。ターミナルを開き直したときは、毎回この操作が必要です。

```bash
source flaskenv/bin/activate      # Mac
flaskenv\Scripts\activate          # Windows（PowerShell）
```

行の先頭に`(flaskenv)`と表示されれば、有効になっています。有効な間は、Mac でも`python`・`pip`と打つだけで、この仮想環境のものが使われます。

---

## ライブラリをインストールする

仮想環境が有効な状態で、バックエンド編（01〜17章）で使うライブラリをまとめてインストールします。使うライブラリとバージョンは、このフォルダの[requirements.txt](requirements.txt)に書いてあります。バージョンは、このカリキュラムで動作確認したものに合わせています。

```bash
pip install -r 00_docs/setup/requirements.txt
```

リポジトリのルート（`00_docs`・`01_frontend`・`02_backend`がある場所）で実行します。`requirements.txt`は「このプロジェクトに必要なライブラリの一覧」を書いたファイルで、Pythonのプロジェクトでよく使われます。

| ライブラリ | 用途 | 使い始める章 |
|---|---|---|
| Flask | Webアプリを作る本体（Jinja2・Werkzeugも一緒に入る） | [01_intro](../../02_backend/01_intro/) |
| Flask-WTF | フォームの入力チェック・CSRF対策 | [09_forms](../../02_backend/09_forms/) |
| SQLAlchemy | SQLを書かずにデータベースを扱う（ORM） | [12_sqlalchemy](../../02_backend/12_sqlalchemy/) |
| Flask-SQLAlchemy | SQLAlchemyをFlaskで使う | [13_flask_sqlalchemy](../../02_backend/13_flask_sqlalchemy/) |
| Flask-Migrate | テーブルの作成・変更を管理する（`flask db`コマンド） | [14_flask_migrate](../../02_backend/14_flask_migrate/) |
| Flask-Login | ログイン機能 | [15_login](../../02_backend/15_login/) |

SQLite（データベース）とsqlite3（PythonからSQLiteを使う道具）は、Pythonに最初から入っているので、インストールは不要です。

インストールできたかは、次のコマンドで確かめられます。

```bash
pip list
```

---

## VS Codeの拡張機能を入れる

VS Codeの左端の、四角が4つ並んだアイコン（拡張機能）から、名前で検索してインストールします。

| 拡張機能 | 発行元 | できること |
|---|---|---|
| Python | Microsoft | Pythonの色分け・補完・エラー表示。型を表示する**Pylance**も一緒に入る |
| Jinja | wholroyd | テンプレート（`templates/`の`.html`）の`{{ }}`・`{% %}`を色分けする |
| SQLite Viewer | Florian Klampfer | データベースのファイル（`.db`・`.sqlite`）をクリックすると、中身を表で見られる |

インストールしたら、VS Codeで使うPythonを、作った仮想環境に切り替えます。

1. コマンドパレット（Mac：`Cmd + Shift + P`／Windows：`Ctrl + Shift + P`）を開く
2. `Python: Select Interpreter`を選ぶ
3. 一覧から`flaskenv`と書かれたPythonを選ぶ

これで、`import flask`の行に波線（「見つからない」の警告）が出なくなります。そのほかの便利な拡張機能と使い方は、[vscode.md](vscode.md)にまとめています。

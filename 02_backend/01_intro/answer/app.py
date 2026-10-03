# ---------- 1. 準備 ----------
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Flaskが動いています！'


# ---------- 2. データベース ----------
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'memos.db')   # app.py と同じフォルダの memos.db


def get_db():
    """データベースにつなぐ"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # row['text'] のように、列の名前で取り出せるようにする
    return conn


def init_db():
    """memos テーブルが無ければ作る"""
    conn = get_db()
    conn.execute('CREATE TABLE IF NOT EXISTS memos (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT NOT NULL)')
    conn.commit()
    conn.close()


init_db()   # このファイルが読み込まれたときに、テーブルを用意する


# ---------- 3. 一覧を表示する ----------
from flask import render_template


@app.route('/')
def index():
    conn = get_db()
    memos = conn.execute('SELECT * FROM memos ORDER BY id DESC').fetchall()   # 新しい順
    conn.close()
    return render_template('index.html', memos=memos)


# ---------- 4. 追加する ----------
from flask import redirect, request, url_for


@app.route('/memos', methods=['POST'])
def add_memo():
    text = request.form['text'].strip()
    if text:
        conn = get_db()
        conn.execute('INSERT INTO memos (text) VALUES (?)', (text,))
        conn.commit()   # 変更を確定する（これを忘れると保存されない）
        conn.close()
    return redirect(url_for('index'))   # 一覧に戻る


# ---------- 5. 削除する ----------
@app.route('/memos/<int:memo_id>/delete', methods=['POST'])
def delete_memo(memo_id):
    conn = get_db()
    conn.execute('DELETE FROM memos WHERE id = ?', (memo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


# ========== ここより上に、2. 〜 5. のコードを貼り付けていく ==========

if __name__ == '__main__':
    app.run(debug=True, port=5100)   # debug=True：保存すると自動で再起動する

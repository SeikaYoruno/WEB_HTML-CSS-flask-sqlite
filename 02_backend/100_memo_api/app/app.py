"""
メモ帳アプリ（完成形） — バックエンド編（02_backend/01〜17）の内容を統合したFlaskアプリ

Flask・Jinja2・WTForms・Flask-SQLAlchemy・Flask-Migrate・Flask-Login・Blueprint で作る。
画面（templates/・static/）には、フロントエンド編で学んだ内容を取り入れている
（README の「フロントエンド編から取り入れた項目」）。

実行:
cd app
flask db upgrade
python app.py
"""
import json
import os
from typing import Optional

from flask import Flask, Response, redirect, url_for
from flask_migrate import Migrate
from flask_login import LoginManager

from models import db, Memo, User

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
instance_dir = os.path.join(base_dir, 'instance')
os.makedirs(instance_dir, exist_ok=True)   # SQLite はフォルダを自動では作らないので、先に作っておく（02_backend/07_with の os.path）

app.config['SECRET_KEY']                     = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///' + os.path.join(instance_dir, 'memos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SEED_JSON_PATH = os.path.join(base_dir, 'memos.json')

# models.py で db = SQLAlchemy() として作っているので、ここで app と結びつける（02_backend/17_blueprint）
db.init_app(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'            # ログインが必要なページを開いたときの移動先
login_manager.login_message = 'ログインしてください。'


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.query.get(int(user_id))


from auth.views import auth_bp
from memos.views import memos_bp

app.register_blueprint(auth_bp)
app.register_blueprint(memos_bp)


@app.route('/')
def index() -> Response:
    return redirect(url_for('memos.index'))


def init_db() -> None:
    """メモが1件も無ければ、memos.json の初期データを入れる（02_backend/17_blueprint と同じ）"""
    with app.app_context():
        if Memo.query.count() == 0:
            with open(SEED_JSON_PATH, encoding='utf-8') as f:
                memos_data = json.load(f)
            db.session.add_all([Memo(**data) for data in memos_data])
            db.session.commit()


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5085)

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ログインするユーザー（02_backend/15_login）"""
    __tablename__ = 'users'

    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)   # ハッシュ化したパスワード

    def set_password(self, raw: str) -> None:
        self.password = generate_password_hash(raw)

    def check_password(self, raw: str) -> bool:
        return check_password_hash(self.password, raw)


class Memo(db.Model):
    """メモ（02_backend/02_memo_app_frontend の localStorage のデータと同じ形）"""
    __tablename__ = 'memos'

    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title     = db.Column(db.String(100), nullable=False)
    category  = db.Column(db.String(50), nullable=False)
    body      = db.Column(db.String(500), nullable=False)
    due_date  = db.Column(db.String(50))                               # 期限（無ければ None）
    is_pinned = db.Column(db.Boolean, nullable=False, default=False)   # ピン留めしているか

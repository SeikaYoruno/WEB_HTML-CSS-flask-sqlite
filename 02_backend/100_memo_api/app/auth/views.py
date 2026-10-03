from flask import Blueprint, Response, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from models import db, User
from forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register() -> str | Response:
    form = RegisterForm()

    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('そのユーザー名はすでに使われています。')
            return render_template('auth/register.html', form=form)

        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('登録が完了しました。ログインしてください。')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login() -> str | Response:
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'ようこそ、{user.username} さん！')
            return redirect(url_for('memos.index'))
        flash('ユーザー名またはパスワードが正しくありません。')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout() -> Response:
    logout_user()
    flash('ログアウトしました。')
    return redirect(url_for('memos.index'))

from flask import Blueprint, Response, abort, flash, redirect, render_template, request, url_for
from flask_login import login_required

from models import db, Memo
from forms import ActionForm, MemoForm

memos_bp = Blueprint('memos', __name__, url_prefix='/memos')


def find_memo(memo_id: int) -> Memo:
    """id のメモを返す。無ければ 404 にする（02_backend/04_flask_basic のエラーハンドリング）"""
    memo = Memo.query.filter_by(id=memo_id).first()
    if memo is None:
        abort(404)
    return memo


@memos_bp.route('/')
def index() -> str:
    """メモ一覧。?category=仕事 のように指定すると、サーバー側で絞り込む（02_backend/08_request）"""
    category = request.args.get('category')

    query = Memo.query
    if category:
        query = query.filter_by(category=category)
    # ピン留めを先頭に、それ以外は新しい順（02_backend/02_memo_app_frontend と同じ並び順）
    memos = query.order_by(Memo.is_pinned.desc(), Memo.id.desc()).all()

    return render_template('memos/index.html', memos=memos, action_form=ActionForm())


@memos_bp.route('/<int:memo_id>')
def detail(memo_id: int) -> str:
    memo = find_memo(memo_id)
    return render_template('memos/detail.html', memo=memo, action_form=ActionForm())


@memos_bp.route('/new', methods=['GET', 'POST'])
@login_required
def create() -> str | Response:
    form = MemoForm()

    if form.validate_on_submit():
        memo = Memo(
            title=form.title.data,
            category=form.category.data,
            body=form.body.data,
            due_date=form.due_date.data or None,   # 空欄なら None
        )
        db.session.add(memo)
        db.session.commit()
        flash('メモを追加しました。')
        return redirect(url_for('memos.detail', memo_id=memo.id))

    return render_template('memos/create.html', form=form)


@memos_bp.route('/<int:memo_id>/edit', methods=['GET', 'POST'])
@login_required
def update(memo_id: int) -> str | Response:
    memo = find_memo(memo_id)
    form = MemoForm()

    if form.validate_on_submit():
        # 取り出したオブジェクトを書き換えて commit すると、データベースも更新される（02_backend/13_flask_sqlalchemy）
        memo.title    = form.title.data
        memo.category = form.category.data
        memo.body     = form.body.data
        memo.due_date = form.due_date.data or None
        db.session.commit()
        flash('メモを更新しました。')
        return redirect(url_for('memos.detail', memo_id=memo.id))

    if request.method == 'GET':
        # 初めて開いたときは、今の内容をフォームに入れておく
        form.title.data    = memo.title
        form.category.data = memo.category
        form.body.data     = memo.body
        form.due_date.data = memo.due_date

    return render_template('memos/update.html', form=form, memo=memo)


@memos_bp.route('/<int:memo_id>/delete', methods=['POST'])
@login_required
def delete(memo_id: int) -> Response:
    memo = find_memo(memo_id)
    if ActionForm().validate_on_submit():   # CSRF トークンの確認
        db.session.delete(memo)
        db.session.commit()
        flash('メモを削除しました。')
    return redirect(url_for('memos.index'))


@memos_bp.route('/<int:memo_id>/pin', methods=['POST'])
@login_required
def toggle_pin(memo_id: int) -> Response:
    """ピン留めの ON / OFF を切り替えて、元のページに戻る"""
    memo = find_memo(memo_id)
    if ActionForm().validate_on_submit():
        memo.is_pinned = not memo.is_pinned
        db.session.commit()
        flash('ピン留めしました。' if memo.is_pinned else 'ピン留めを外しました。')
    # request.referrer：このリクエストを送ったページ（一覧・詳細のどちらから押しても、そのページに戻る）
    return redirect(request.referrer or url_for('memos.index'))

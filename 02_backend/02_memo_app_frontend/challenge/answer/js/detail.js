/*
detail.js：メモ詳細ページ（detail.html?id=3）の処理

URL の ?id= からメモを探して表示する。無いメモの id なら、メッセージだけを出す。
*/

const detailStatus = document.getElementById('detail-status');
const detail = document.getElementById('detail');

let memos = [];
let memo = null;   // 表示中のメモ


// ============================================================
// ステップ5：メモの内容をページに入れる
// ============================================================
const showMemo = () => {
    document.title = `${memo.title} - メモ帳`;   // タブのタイトルも、メモのタイトルにする
    document.getElementById('detail-category').textContent = memo.category;
    document.getElementById('detail-title').textContent = memo.title;
    document.getElementById('detail-body').textContent = memo.body;
    document.getElementById('detail-edit').href = `edit.html?id=${memo.id}`;

    // 期限が無いメモは、期限の行（dl）ごと隠す
    const due = document.getElementById('detail-due');
    document.getElementById('detail-meta').hidden = !memo.due_date;
    if (memo.due_date) {
        due.dateTime = memo.due_date;
        due.textContent = memo.due_date;
    }

    detailStatus.textContent = '';
    detail.hidden = false;
};


// ============================================================
// ステップ6：削除
// ============================================================
document.getElementById('detail-delete').addEventListener('click', () => {
    openConfirm(`「${memo.title}」を削除しますか？`, () => {   // common.js
        memos = memos.filter((m) => m.id !== memo.id);
        saveMemos(memos);
        location.href = 'index.html';   // 削除したら一覧に戻る
    });
});


// ============================================================
// ページを開いたときの処理
// ============================================================
const start = async () => {
    try {
        memos = await initMemos();
    } catch (error) {
        console.error(error);
        detailStatus.textContent = 'メモを読み込めませんでした。python -m http.server で起動して開いているか確認してください。';
        return;
    }

    // ステップ5：URL の ?id= のメモを探す（getIdFromUrl() は storage.js）
    memo = memos.find((m) => m.id === getIdFromUrl());
    if (!memo) {
        detailStatus.textContent = '指定されたメモが見つかりません。';
        detailStatus.classList.add('error');
        return;
    }
    showMemo();
};

start();

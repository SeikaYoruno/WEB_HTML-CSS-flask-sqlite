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
    // TODO
};


// ============================================================
// ステップ6：削除
// ============================================================
// TODO：#detail-delete の click



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
    memo = null;   // TODO：URL の ?id= のメモを探す
    if (!memo) {
        detailStatus.textContent = '指定されたメモが見つかりません。';
        detailStatus.classList.add('error');
        return;
    }
    showMemo();
};

start();

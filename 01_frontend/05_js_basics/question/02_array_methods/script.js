const memos = [
    { id: 1, title: '買い物リスト', category: '家事', pinned: true },
    { id: 2, title: '企画会議メモ', category: '仕事', pinned: false },
    { id: 3, title: '読書メモ：銀河鉄道の夜', category: '趣味', pinned: false },
    { id: 4, title: '会議の議事録', category: '仕事', pinned: true },
    { id: 5, title: '旅行の持ち物リスト', category: 'プライベート', pinned: false },
];


// TODO 1
const ids = undefined;   // undefined を書き換える


// TODO 2
const pinnedCount = undefined;   // undefined を書き換える


// TODO 3
const findMemo = (id) => {
};


// TODO 4
const searchTitles = (keyword) => {
};


// TODO 5
const categories = [];



// TODO 6
const countIf = (items, test) => {
};


// TODO 7
const getToday = () => '2026-10-03';
const getShortTitle = (memo) => memo.title.slice(0, 4);   // slice(0, 4)：先頭から4文字を取り出す

const todayText = getToday;
const getShortTitles = () => memos.map(getShortTitle());


// ============================================================
// テスト（ここから下は書き換えない）
// ============================================================
// check(説明, 結果を返す関数, 期待する値)：途中でエラーが起きても、残りのテストは続けて実行する
const check = (label, getActual, expected) => {
    try {
        const actual = getActual();
        const ok = JSON.stringify(actual) === JSON.stringify(expected);
        if (ok) {
            console.log(`✅ ${label}`);
        } else {
            console.log(`❌ ${label}　結果：${JSON.stringify(actual)}　期待：${JSON.stringify(expected)}`);
        }
    } catch (error) {
        console.log(`❌ ${label}　エラー：${error.message}`);
    }
};

check('TODO 1：ids', () => ids, [1, 2, 3, 4, 5]);
check('TODO 2：pinnedCount', () => pinnedCount, 2);
check('TODO 3：findMemo(3)', () => findMemo(3), memos[2]);
check('TODO 3：findMemo(99)', () => findMemo(99), undefined);
check('TODO 4：searchTitles(会議)', () => searchTitles('会議'), ['企画会議メモ', '会議の議事録']);
check('TODO 4：searchTitles(リスト)', () => searchTitles('リスト'), ['買い物リスト', '旅行の持ち物リスト']);
check('TODO 5：categories', () => categories, ['家事', '仕事', '趣味', 'プライベート']);
check('TODO 6：countIf(数値)', () => countIf([3, 8, 1, 6], (n) => n > 4), 2);
check('TODO 6：countIf(ピン留め)', () => countIf(memos, (memo) => memo.pinned), 2);
check('TODO 6：countIf(仕事)', () => countIf(memos, (memo) => memo.category === '仕事'), 2);
check('TODO 7：todayText', () => todayText, '2026-10-03');
check('TODO 7：getShortTitles()', () => getShortTitles(), ['買い物リ', '企画会議', '読書メモ', '会議の議', '旅行の持']);
check('元の memos が変更されていない', () => memos.length, 5);

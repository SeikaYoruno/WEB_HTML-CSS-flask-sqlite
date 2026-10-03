// ============================================================
// 1. 関数は「値」として扱える
// ============================================================
// 関数を変数に入れたり、別の関数に渡したりできる
const greet = (name) => `こんにちは、${name}さん`;
const sayHello = greet;            // () を付けないと「関数そのもの」を渡す
console.log(sayHello('山田'));      // こんにちは、山田さん

// greet と greet() の違い
console.log(typeof greet);         // function（関数そのもの）
console.log(typeof greet('a'));    // string（関数を呼び出した結果）


// ============================================================
// 2. コールバック関数：あとで呼び出してもらう関数
// ============================================================
// 引数として渡し、相手の都合のよいタイミングで呼び出してもらう関数を「コールバック関数」と呼ぶ
const repeat = (times, callback) => {
    for (let i = 0; i < times; i++) {
        callback(i);               // 受け取った関数を、ここで呼び出す
    }
};

repeat(3, (i) => {
    console.log(`${i + 1}回目の呼び出し`);
});

// これまで使ってきた forEach も、コールバック関数を受け取る関数
//   ['a', 'b'].forEach((x) => { ... });
//                      └──────────────┘ 要素1つごとに呼び出してもらう関数
// このあと学ぶ addEventListener も同じ
//   button.addEventListener('click', () => { ... });
//                                    └──────────┘ クリックされたときに呼び出してもらう関数


// ============================================================
// 3. 配列のよく使うメソッド
// ============================================================
const memos = [
    { id: 1, title: '買い物リスト', category: '家事', pinned: true },
    { id: 2, title: '企画会議メモ', category: '仕事', pinned: false },
    { id: 3, title: '読書メモ：銀河鉄道の夜', category: '趣味', pinned: false },
    { id: 4, title: '資料作成', category: '仕事', pinned: true },
];

// map()：各要素を変換した「新しい配列」を作る
const titles = memos.map((memo) => memo.title);
console.log(titles);   // ['買い物リスト', '企画会議メモ', '読書メモ：銀河鉄道の夜', '資料作成']

// filter()：条件に合う要素だけの「新しい配列」を作る
const pinned = memos.filter((memo) => memo.pinned);
console.log(pinned.length);   // 2

// find()：条件に合う「最初の1件」を返す（見つからなければ undefined）
const memo3 = memos.find((memo) => memo.id === 3);
console.log(memo3.title);     // 読書メモ：銀河鉄道の夜
console.log(memos.find((memo) => memo.id === 99));   // undefined

// includes()：その値が含まれているか（true / false）
const categories = memos.map((memo) => memo.category);
console.log(categories.includes('仕事'));   // true
console.log(categories.includes('旅行'));   // false

// 組み合わせる：「仕事」カテゴリのメモのタイトルだけを取り出す
const workTitles = memos
    .filter((memo) => memo.category === '仕事')
    .map((memo) => memo.title);
console.log(workTitles);      // ['企画会議メモ', '資料作成']

// 文字列の includes() もある（部分一致の検索に使える）
console.log('企画会議メモ'.includes('会議'));   // true


// ============================================================
// 4. forEach / map / filter の使い分け
// ============================================================
// forEach：1件ずつ「何かをする」（画面を書き換える・ログを出す）。戻り値は無い
// map    ：1件ずつ「変換して」新しい配列を作る
// filter ：1件ずつ「残すかどうか判定して」新しい配列を作る
// find   ：条件に合う1件を探す

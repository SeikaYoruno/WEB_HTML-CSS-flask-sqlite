/*
解答3：何が出力される？
*/

// --- 真偽の判定 ---
console.log(Boolean(''));          // Q1 正解：false（空文字は falsy）
console.log(Boolean('0'));         // Q2 正解：true（中身のある文字列は truthy。数値の 0 とは別物）
console.log(Boolean([]));          // Q3 正解：true（空の配列も truthy。Pythonの [] は偽なので要注意）
console.log(Boolean(null));        // Q4 正解：false

// --- == と === ---
console.log(10 == '10');           // Q5 正解：true（== は型を変換してから比べる）
console.log(10 === '10');          // Q6 正解：false（=== は型も比べる。数値と文字列なので別物）

// --- 要素が見つからないとき ---
const el = document.getElementById('not-exist');
console.log(el);                   // Q7 正解：null（該当する要素が無い）
console.log(el ? 'あり' : 'なし');  // Q8 正解：なし（null は falsy）

// --- 配列メソッド ---
const nums = [3, 8, 1, 6];
console.log(nums.map((n) => n * 2));         // Q9 正解：[6, 16, 2, 12]（すべての要素を変換した新しい配列）
console.log(nums.filter((n) => n > 4));      // Q10 正解：[8, 6]（条件に合う要素すべて）
console.log(nums.find((n) => n > 4));        // Q11 正解：8（条件に合う「最初の1件」だけ。配列ではない）
console.log(nums.find((n) => n > 100));      // Q12 正解：undefined（見つからない）
console.log(nums.includes(6));               // Q13 正解：true

// --- 関数とコールバック ---
const double = (n) => n * 2;
console.log(typeof double);        // Q14 正解：function（() を付けないと関数そのもの）
console.log(typeof double(5));     // Q15 正解：number（() を付けると呼び出した結果の 10）

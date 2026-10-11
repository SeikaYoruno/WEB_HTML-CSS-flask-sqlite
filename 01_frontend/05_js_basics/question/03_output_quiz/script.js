// --- 真偽の判定 ---
console.log(Boolean(''));          // Q1 予想：
console.log(Boolean('0'));         // Q2 予想：
console.log(Boolean([]));          // Q3 予想：
console.log(Boolean(null));        // Q4 予想：

// --- == と === ---
console.log(10 == '10');           // Q5 予想：
console.log(10 === '10');          // Q6 予想：

// --- 要素が見つからないとき ---
const el = document.getElementById('not-exist');
console.log(el);                   // Q7 予想：
console.log(el ? 'あり' : 'なし');  // Q8 予想：

// --- 配列メソッド ---
const nums = [3, 8, 1, 6];
console.log(nums.map((n) => n * 2));         // Q9 予想：
console.log(nums.filter((n) => n > 4));      // Q10 予想：
console.log(nums.find((n) => n > 4));        // Q11 予想：
console.log(nums.find((n) => n > 100));      // Q12 予想：
console.log(nums.includes(6));               // Q13 予想：

// --- 関数とコールバック ---
const double = (n) => n * 2;
console.log(typeof double);        // Q14 予想：
console.log(typeof double(5));     // Q15 予想：

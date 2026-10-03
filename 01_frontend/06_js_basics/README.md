# 06 JavaScriptの基本文法

> フロントエンド編 ／ 前の章：[05_css_layout](../05_css_layout/) ／ 次の章：[07_js_dom_events](../07_js_dom_events/)

HTMLが「構造」、CSSが「見た目」を担当するのに対し、**JavaScript**はWebページの「動き」を担当する、ブラウザの中で動くプログラミング言語です。この章では、JavaScriptの読み込み方とデバッグの方法、変数・条件分岐などの基本文法、関数とコールバック・配列の扱い方を学びます。ページの要素を操作するのは、次の[07_js_dom_events](../07_js_dom_events/)からです。

## 目次

0. [JavaScriptの読み込み方とデバッグ](#0-javascriptの読み込み方とデバッグ)
1. [JavaScript基本文法](#1-javascript基本文法)
2. [関数とコールバック・配列](#2-関数とコールバック配列)

---

## フォルダ構成

```
01_frontend/06_js_basics/
├── README.md
├── example/                      サンプル（1つのサンプル＝1つのフォルダ）
│   ├── 01_js_basics/             JavaScript基本文法・null・真偽の判定・===
│   │   ├── index.html
│   │   └── script.js
│   └── 02_functions_arrays/      関数とコールバック・配列メソッド
│       ├── index.html
│       └── script.js
└── question/                     練習問題（3問。問題文はREADMEの各節の最後）
    ├── 01_basic_functions/       練習問題1：基本文法で関数を書く
    │   ├── index.html
    │   └── script.js
    ├── 02_array_methods/         練習問題2：配列メソッドとコールバック
    │   ├── index.html
    │   └── script.js
    ├── 03_output_quiz/           練習問題3：何が出力されるか予想する
    │   ├── index.html
    │   └── script.js
    └── answer/                   解答（問題と同じ名前のフォルダ。中のファイル構成も問題と同じ）
        ├── 01_basic_functions/
        ├── 02_array_methods/
        └── 03_output_quiz/
```

---

## 0. JavaScriptの読み込み方とデバッグ

### `<script>`タグ

JavaScriptは、CSSと同じく別ファイル（`.js`）に書いてHTMLから読み込むのが基本です。

```html
<body>
    ...ページの内容...

    <!-- </body> の直前に書く -->
    <script src="script.js"></script>
</body>
```

| ポイント | 説明 |
|---|---|
| `src` | 読み込むJavaScriptファイルのパス（CSSの`<link href>`と同じく相対パスで書ける） |
| `</body>`の直前に置く | ブラウザはHTMLを上から順に読む。`<head>`で読み込むと、まだ存在しない要素をJavaScriptが探してしまい、`null`になって動かない |
| `<script defer src="...">` | `<head>`に書きたい場合は`defer`を付けると、HTMLを読み終えてから実行される（どちらの書き方でもよい） |

### コンソール

開発者ツール（`F12`／Mac：`Cmd + Option + I`）の**Console**タブには、`console.log()`で出力した値と、JavaScriptのエラーが表示されます。Consoleに直接`1 + 2`のように打ち込んで、その場でJavaScriptを試すこともできます。

### 動かないときの調べ方

JavaScriptは、エラーが起きるとその行で処理が止まり、それ以降のコードが実行されません。「動かない」ときは次の順に調べます。

1. **Consoleに赤字のエラーが出ていないか**を見る。エラー文の右端のファイル名と行番号をクリックすると、該当行に移動できる
2. エラーが出ていないのに動きがおかしいときは、**途中の値を確かめる**。`console.log(変数)`を入れるか、**Sources**パネルでファイルを開き、行番号をクリックして**ブレークポイント**を置く。その行で処理が一時停止し、変数にマウスを乗せると中身が見える（再開は▶ボタン）

よく出るエラーは次の3つです。

| エラー | 意味 | よくある原因 |
|---|---|---|
| `TypeError: Cannot read properties of null (reading 'addEventListener')` | `null`のプロパティを読もうとした | `getElementById`の綴り間違い・HTMLの`id`の付け忘れ・`<script>`を`<head>`で読み込んでいる |
| `ReferenceError: xxx is not defined` | 定義されていない変数を使った | 変数名の打ち間違い・宣言する前に使っている |
| `SyntaxError: Unexpected token` | 文法が間違っている | カッコ・引用符の閉じ忘れ、`,`の付け忘れ |

存在しないプロパティを読んだとき（`value.lenght`のような打ち間違い）は、エラーにならず`undefined`になります。表示に`undefined`と出たら、プロパティ名を疑いましょう。07_js_dom_events の練習問題1で、実際に探してみます。

---

## 1. JavaScript基本文法

> [example/01_js_basics/index.html](example/01_js_basics/index.html) / [example/01_js_basics/script.js](example/01_js_basics/script.js)

この先で使うJavaScriptの最低限の文法を確認します。ブラウザで開き、開発者ツールのコンソールで結果を確認してください。

### 変数：let と const

```javascript
let count = 1;
count = 2;   // let は再代入できる

const name = 'メモ帳';
// name = '別の名前';   // const は再代入できないのでエラーになる
```

JavaScriptでは、変数を使う前に`let`か`const`で宣言します（Pythonなら`x = 1`だけで使えますが、JavaScriptでは宣言が必要です）。何が変わるか分からない場合はまず`const`を使い、再代入が必要になったら`let`に変えるのが一般的です。

### データ型とテンプレートリテラル

```javascript
const str = 'こんにちは';                    // 文字列
const num = 42;                              // 数値（整数と小数を区別しない）
const isDone = true;                         // 真偽値（true / false）
const list = [1, 2, 3];                      // 配列（Pythonのlistに相当）
const obj = { title: 'メモ', category: '仕事' };   // オブジェクト（Pythonのdictに相当）

// テンプレートリテラル：バッククォート(`)で ${式} を埋め込める（Pythonのf文字列に相当）
const message = `${name}には${list.length}件のメモがあります`;
```

### 関数（アロー関数）

```javascript
// function 宣言
function add(a, b) {
    return a + b;
}

// アロー関数（本章で多用する書き方）
const addArrow = (a, b) => {
    return a + b;
};

// 処理が1行だけなら {} と return を省略できる
const addShort = (a, b) => a + b;
```

### 条件分岐・繰り返し

```javascript
if (score >= 80) {
    console.log('合格');
} else if (score >= 50) {
    console.log('もう少し');
} else {
    console.log('不合格');
}

for (let i = 0; i < 3; i++) {
    console.log(`ループ ${i} 回目`);
}

// 配列を1件ずつ処理する（Pythonの for x in list: に相当）
categories.forEach((category) => {
    console.log(category);
});
```

### `null`と`undefined`

```javascript
let notAssigned;
console.log(notAssigned);          // undefined（宣言しただけで、まだ値が入っていない）

const missing = document.getElementById('body');
console.log(missing);              // null（id="body" の要素が無い）
// console.log(missing.value);     // TypeError：null のプロパティは読めない
```

| 値 | 意味 | よく出会う場面 |
|---|---|---|
| `undefined` | まだ値が入っていない | 宣言しただけの変数、存在しないプロパティ（`obj.lenght`のような打ち間違い）、`find()`で見つからなかったとき |
| `null` | 「無い」ことを意図的に表す値 | `getElementById()`・`querySelector()`で要素が見つからなかったとき |

### 真偽の判定：truthy と falsy

`if`の条件には、`true`/`false`以外の値も書けます。次の6つは**偽（falsy）**として扱われ、それ以外はすべて**真（truthy）**になります。

| falsy な値 | |
|---|---|
| `false`・`0`・`''`（空文字）・`null`・`undefined`・`NaN` | これ以外（`'0'`・`[]`・`{}`も含む）はすべて truthy |

```javascript
const bodyTextarea = document.getElementById('body');
if (bodyTextarea) {
    // 要素があるとき（null でないとき）だけ実行される
}

if (input.value.trim()) {
    // 空白を除いて1文字以上入力されているときだけ実行される
}
```

複数のページで同じ`script.js`を読み込むと（制作課題のHPのように）、ページによっては要素が無く`null`になります。`if (要素)`はこの性質を使った「要素があるときだけ処理する」書き方です。

> 注意：Pythonでは空のリスト`[]`は偽ですが、JavaScriptの空の配列`[]`は**真**です。配列が空かどうかは`list.length > 0`で判定します。

### 比較は`===`を使う

```javascript
1 == '1';     // true （== は型を変換してから比べる）
1 === '1';    // false（=== は型も含めて比べる）
1 !== '1';    // true （!== は「等しくない」）
```

`==`は型を自動で変換するため思わぬ結果になります。**比較は常に`===`と`!==`を使います**。また、古いコードでは変数の宣言に`var`が使われていることがありますが、予期しない動きをしやすいため、今は`let`と`const`だけを使います。

### （参考）Pythonとの対応

Pythonを触ったことがある人向けの対応表です。Pythonは`02_backend/03_function`以降で本格的に使うので、今は読み飛ばしても構いません。

| Python | JavaScript |
|---|---|
| `x = 1`（変数） | `let x = 1;` または `const x = 1;` |
| `None` | `null`（または`undefined`） |
| `==`（値の比較） | `===` |
| `and` / `or` / `not` | `&&` / `||` / `!` |
| `True` / `False` | `true` / `false` |
| `[1, 2, 3]`（list） | `[1, 2, 3]`（配列） |
| `{"a": 1}`（dict） | `{ a: 1 }`（オブジェクト） |
| `f"{name}さん"` | `` `${name}さん` ``（テンプレートリテラル） |
| `def f(a, b): return a + b` | `const f = (a, b) => a + b;`（アロー関数） |
| `for x in list:` | `list.forEach((x) => { ... });` |
| `[x for x in list if 条件]` | `list.filter((x) => 条件)` |

### 実行方法

`example/01_js_basics/index.html`をブラウザで直接開き、開発者ツール（`F12`または右クリック→検証）の「コンソール」タブで`console.log()`の出力を確認してください。

### 動作確認：コンソールに出力される値を確認する

| 確認する行 | 確認したいこと |
|---|---|
| `console.log(count, name);` | `2 メモ帳`と出力される（`let`で再代入した後の`count`の値が`2`になっている） |
| `console.log(message);` | `メモ帳には3件のメモがあります`と出力される（テンプレートリテラルで`${name}`・`${list.length}`が埋め込まれている） |
| `console.log(add(1, 2), addArrow(1, 2), addShort(1, 2));` | `3 3 3`と出力される（3つとも同じ結果を返す関数であることが分かる） |
| 条件分岐・for文・forEachの出力 | `合格` → `ループ 0 回目`〜`ループ 2 回目` → `家事`・`仕事`・`趣味`の順に出力される |
| `console.log(workMemos);` | `category`が`'仕事'`の要素だけが残った配列（`[{ id: 2, title: '企画会議メモ', category: '仕事' }]`）が出力される（`filter()`の効果） |
| 「6. null と undefined」の出力 | `undefined`→`null`の順に出力される |
| 「7. 真偽の判定」の出力 | `false`・`0`・空文字・`null`・`undefined`が`falsy`、`'a'`・`1`・`[]`・`{}`が`truthy`と出力され、最後に`要素が無いので何もしない`・`空欄`と出力される |
| 「8. 比較は === を使う」の出力 | `==`の3行はすべて`true`、`===`の2行は`false`、`!==`の行は`true` |

**正常な状態の見分け方**：コンソールに赤字のエラー（`Uncaught ReferenceError`など）が出ていなければ、上から順にすべての`console.log`が実行されています。途中で出力が止まっている場合は、それより前の行に文法ミスがないか確認してください。


### 練習問題1：基本文法で関数を書く

> 問題：[question/01_basic_functions/index.html](question/01_basic_functions/index.html)・[question/01_basic_functions/script.js](question/01_basic_functions/script.js) ｜ 解答：[question/answer/01_basic_functions/index.html](question/answer/01_basic_functions/index.html)・[question/answer/01_basic_functions/script.js](question/answer/01_basic_functions/script.js)

<details>
<summary>問題の内容を開く</summary>

`01_basic_functions/script.js`の`TODO 1`〜`TODO 6`の関数の中身を書きます。`01_basic_functions/index.html`を開くと、ファイルの一番下のテストが実行され、Consoleに ✅（正しい）／❌（間違い）が表示されます。❌のときは、結果と期待する値も表示されます。すべて ✅ になれば完成です。

変数の宣言には`let`か`const`を使い（`var`は使わない）、比較には`===` / `!==`を使います。

| # | 関数 | やること | 例 |
|---|---|---|---|
| 1 | `getGrade(score)` | 点数から評価を返す。80点以上→`'合格'`、50点以上→`'もう少し'`、それ以外→`'不合格'` | `getGrade(80)` → `'合格'` |
| 2 | `formatMemo(memo)` | メモのオブジェクトから「[カテゴリ] タイトル」という文字列を作る | `formatMemo({ title: '企画会議メモ', category: '仕事' })` → `'[仕事] 企画会議メモ'` |
| 3 | `sumTo(n)` | 1からnまでの合計を返す | `sumTo(3)` → `6`、`sumTo(10)` → `55` |
| 4 | `isFilled(text)` | 文字が「空白を除いて1文字以上」あるかを`true` / `false`で返す | `isFilled('メモ')` → `true`、`isFilled('   ')` → `false` |
| 5 | `countByCategory(memos, category)` | メモの配列のうち、指定したカテゴリのメモが何件あるかを返す | `countByCategory(memos, '仕事')` → `2` |
| 6 | `describeList(list)` | 配列の件数を文章で返す。0件なら`'メモはありません'`、それ以外なら`'3件のメモがあります'`のように返す | `describeList([])` → `'メモはありません'` |

| # | ヒント |
|---|---|
| 1 | `if` / `else if` / `else` |
| 2 | テンプレートリテラル（バッククォート`` ` ``と`${}`） |
| 3 | 合計を入れる変数は、あとで値を足していくので`let`で宣言する。`for`文で1からnまで繰り返す |
| 4 | `文字列.trim()`で前後の空白を除く。空文字`''`は falsy。`if (条件) { return true; }`と書いてもよいし、比較の結果をそのまま`return`してもよい |
| 5 | 件数を入れる変数を`let`で用意し、`forEach`で1件ずつ見て、カテゴリが等しければ1増やす |
| 6 | 空の配列`[]`は truthy なので、`if (list)`では空かどうか判定できない |

</details>

---

## 2. 関数とコールバック・配列

> [example/02_functions_arrays/index.html](example/02_functions_arrays/index.html) / [example/02_functions_arrays/script.js](example/02_functions_arrays/script.js)

### 関数は「値」として扱える

```javascript
const greet = (name) => `こんにちは、${name}さん`;

typeof greet;        // 'function'（() を付けない → 関数そのもの）
typeof greet('a');   // 'string'  （() を付ける → 呼び出した結果）
```

JavaScriptでは、関数を変数に入れたり、別の関数の引数に渡したりできます。`()`を付けるかどうかで「関数そのもの」か「呼び出した結果」かが変わる点に注意します。

### コールバック関数

引数として渡し、**相手の都合のよいタイミングで呼び出してもらう関数**を、コールバック関数と呼びます。

```javascript
const repeat = (times, callback) => {
    for (let i = 0; i < times; i++) {
        callback(i);            // 受け取った関数を、ここで呼び出す
    }
};

repeat(3, (i) => console.log(`${i + 1}回目`));
```

これまでに出てきた`forEach`も、この後の`addEventListener`も、コールバック関数を受け取る関数です。

```javascript
memos.forEach((memo) => { ... });                   // 要素1つごとに呼び出してもらう
button.addEventListener('click', () => { ... });    // クリックされたときに呼び出してもらう
```

この「あとで呼び出してもらう関数を渡す」考え方は、`02_backend/03_function`でPythonのデコレータを学ぶときや、[09_js_data](../09_js_data/)の`fetch()`で通信の結果を受け取るときにも出てきます。

### 配列のよく使うメソッド

| メソッド | 戻り値 | 用途 |
|---|---|---|
| `forEach(fn)` | なし | 1件ずつ「何かをする」（画面を書き換える・ログを出す） |
| `map(fn)` | 新しい配列 | 1件ずつ**変換**する（メモの配列 → タイトルの配列） |
| `filter(fn)` | 新しい配列 | 条件に合うものだけを**残す** |
| `find(fn)` | 1件（無ければ`undefined`） | 条件に合う**最初の1件**を探す |
| `includes(値)` | `true`/`false` | その値が含まれているか。文字列にも使える（部分一致の検索） |

```javascript
const titles = memos.map((memo) => memo.title);
const pinned = memos.filter((memo) => memo.pinned);
const memo3 = memos.find((memo) => memo.id === 3);
categories.includes('仕事');      // true
'企画会議メモ'.includes('会議');   // true

// つなげて書ける：「仕事」のメモのタイトルだけ
const workTitles = memos
    .filter((memo) => memo.category === '仕事')
    .map((memo) => memo.title);
```

`map`・`filter`は元の配列を変更せず、新しい配列を返します。

### 動作確認：コンソールに出力される値を確認する

`example/02_functions_arrays/index.html`をブラウザで開き、Consoleを確認します。

| 確認する出力 | 確認したいこと |
|---|---|
| `function`と`string` | `greet`は関数そのもの、`greet('a')`は呼び出した結果（文字列）であることがわかる |
| `1回目の呼び出し`〜`3回目の呼び出し` | `repeat()`に渡した関数が3回呼び出されている |
| `map`・`filter`・`find`の出力 | タイトルの配列、ピン留めの件数`2`、`読書メモ：銀河鉄道の夜`、見つからないときの`undefined` |
| `workTitles` | `['企画会議メモ', '資料作成']`（`filter`と`map`をつなげた結果） |


### 練習問題2：配列メソッドとコールバック

> 問題：[question/02_array_methods/index.html](question/02_array_methods/index.html)・[question/02_array_methods/script.js](question/02_array_methods/script.js) ｜ 解答：[question/answer/02_array_methods/index.html](question/answer/02_array_methods/index.html)・[question/answer/02_array_methods/script.js](question/answer/02_array_methods/script.js)

<details>
<summary>問題の内容を開く</summary>

`02_array_methods/script.js`の`TODO 1`〜`TODO 7`を書きます。練習問題1と同じく、`02_array_methods/index.html`を開くとConsoleにテスト結果が表示されます。

TODO 1〜4は`for`文を使わず、`map` / `filter` / `find` / `includes`で書きます。元の`memos`配列は変更しません。

| # | やること | 期待する結果 |
|---|---|---|
| 1 | `ids`：すべてのメモの`id`だけを並べた配列 | `[1, 2, 3, 4, 5]` |
| 2 | `pinnedCount`：ピン留め（`pinned`が`true`）のメモの件数 | `2` |
| 3 | `findMemo(id)`：`id`を受け取り、そのメモ（オブジェクト）を返す。無ければ`undefined` | `findMemo(3).title` → `'読書メモ：銀河鉄道の夜'` |
| 4 | `searchTitles(keyword)`：タイトルにキーワードを含むメモの「タイトルの配列」を返す（`filter`と`map`をつなげる。文字列にも`includes()`が使える） | `searchTitles('会議')` → `['企画会議メモ', '会議の議事録']` |
| 5 | `categories`：カテゴリの一覧（重複なし・登場順）。空の配列に、`forEach`で1件ずつ見て、まだ`includes()`されていないカテゴリだけ`push()`する | `['家事', '仕事', '趣味', 'プライベート']` |
| 6 | `countIf(items, test)`：配列の各要素を「判定する関数」`test`に渡し、`true`が返ってきた要素の件数を返す（2節の`repeat()`と同じく、受け取った関数を中で`test(item)`のように呼び出す。`filter`と`length`を使ってもよい） | `countIf([3, 8, 1, 6], (n) => n > 4)` → `2`、`countIf(memos, (memo) => memo.pinned)` → `2` |
| 7 | `todayText`と`getShortTitles`の2か所は、どちらも「関数そのもの」か「呼び出した結果」かを間違えている。`()`を足すか消すかして直す | `todayText` → `'2026-10-03'`、`getShortTitles()` → 各タイトルの先頭4文字の配列 |

</details>

### 練習問題3：何が出力されるか予想する

> 問題：[question/03_output_quiz/index.html](question/03_output_quiz/index.html)・[question/03_output_quiz/script.js](question/03_output_quiz/script.js) ｜ 解答：[question/answer/03_output_quiz/index.html](question/answer/03_output_quiz/index.html)・[question/answer/03_output_quiz/script.js](question/answer/03_output_quiz/script.js)

<details>
<summary>問題の内容を開く</summary>

1節・2節のまとめの問題です。`03_output_quiz/script.js`の15個の`console.log`（真偽の判定・`==`と`===`・要素が見つからないとき・配列メソッド・関数とコールバック）の出力を、ブラウザで**開く前に**予想し、各行の「`// Q◯ 予想：`」の後ろに書き込みます。

| 確認する操作 | 確認したいこと |
|---|---|
| 予想を書き終えてから`03_output_quiz/index.html`を開き、Consoleを見る | 予想と実際の出力を比べる |
| 外れたものについて、1節・2節を読み直す | なぜその出力になるのかを説明できる |

</details>

---

## 次のステップ

続きは [07_js_dom_events](../07_js_dom_events/) です。JavaScriptでページの要素を書き換え、クリックや入力に反応させます。

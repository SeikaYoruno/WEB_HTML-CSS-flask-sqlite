# 06 DOM操作とイベント

> フロントエンド編 ／ 前の章：[05_js_basics](../05_js_basics/) ／ 次の章：[07_js_ui](../07_js_ui/)

[05_js_basics](../05_js_basics/)で学んだ文法を使って、JavaScriptからページの要素を取得・書き換える**DOM操作**と、クリック・入力・ホバーなどに反応する**イベント**を学びます。最後に、ページを再読み込みせずに表示を切り替える「絞り込み」を作ります。

章の最後の制作課題では、オリジナルHPにJavaScriptで動き（ハンバーガーメニュー・一覧の絞り込み・お問い合わせの入力チェック）を付けます。ここで学ぶ書き方は、バックエンド編のメモ帳アプリ（`02_backend/02_memo_app_frontend`・`02_backend/100_memo_api`）でもそのまま使います。

## 前提

| チャプター | 使う知識 |
|---|---|
| 02_html_semantic_form | `id`・`class`・`data-*`属性、フォーム部品 |
| 03_css_basics | クラスセレクタ（JavaScriptからクラスを付け外しして見た目を切り替える） |
| 05_js_basics | 変数・真偽の判定・関数とコールバック・配列メソッド・デバッグの方法 |

## 目次

1. [DOM操作](#1-dom操作)
2. [イベント](#2-イベント)
3. [クライアント側での絞り込み](#3-クライアント側での絞り込み)
- [制作課題：オリジナルHP（ステップ3）](#制作課題オリジナルhpステップ3)

---

## フォルダ構成

```
01_frontend/06_js_dom_events/
├── README.md
├── example/                      サンプル（1つのサンプル＝1つのフォルダ）
│   ├── 01_dom/                   DOM操作（取得・書き換え・属性・要素の作成・XSS）
│   │   ├── index.html
│   │   └── script.js
│   ├── 02_events/                イベント（イベントオブジェクト・ホバーとフォーカス・submit・preventDefault・confirm）
│   │   ├── index.html
│   │   └── script.js
│   └── 03_client_filter/         クライアント側での絞り込み
│       ├── index.html
│       └── script.js
├── question/                     練習問題（4問。問題文はREADMEの各節の最後）
│   ├── 01_debug_counter/         練習問題1：動かない文字数カウンターを直す（デバッグ）
│   │   ├── index.html
│   │   └── script.js
│   ├── 02_memo_cards/            練習問題2：配列のデータからメモカードを作る
│   │   ├── index.html
│   │   └── script.js
│   ├── 03_form_validation/       練習問題3：フォームの送信前に入力をチェックする
│   │   ├── index.html
│   │   └── script.js
│   ├── 04_tag_filter/            練習問題4：タグとキーワードの両方で絞り込む
│   │   ├── index.html
│   │   └── script.js
│   └── answer/                   解答（問題と同じ名前のフォルダ。中のファイル構成も問題と同じ）
│       ├── 01_debug_counter/
│       ├── 02_memo_cards/
│       ├── 03_form_validation/
│       └── 04_tag_filter/
└── challenge/                         制作課題（オリジナルHP）ステップ3：HTML・CSSは完成済み、js/script.js にTODOを書く
    └── answer/                        完成例
```

---

## 1. DOM操作

> [example/01_dom/index.html](example/01_dom/index.html) / [example/01_dom/script.js](example/01_dom/script.js)

ブラウザは読み込んだHTMLを、JavaScriptから操作できる**DOM**（Document Object Model：要素の木構造）に変換して保持しています。JavaScriptでDOMを書き換えると、画面にすぐ反映されます。まずは要素を取得して内容を書き換える基本を、文字数カウンターを題材に学びます。

```javascript
// 1. document.getElementById() で要素を取得する
const textarea = document.getElementById('body');
const counter = document.getElementById('count');

// 2. addEventListener() でイベント（入力のたびに発火する 'input'）を監視する
textarea.addEventListener('input', () => {
    const length = textarea.value.length;

    // 3. textContent を書き換えると画面表示が更新される
    counter.textContent = length;

    // 4. classList.toggle() で条件に応じてCSSクラスを付け外しする
    counter.classList.toggle('over', length > 450);
});
```

### ポイント

| 要素・メソッド | 説明 |
|---|---|
| `document.getElementById('id')` | `id`属性が一致する要素を1つ取得する |
| `要素.addEventListener('input', 関数)` | 入力のたびに関数を実行する（クリックなら`'click'`） |
| `要素.value` | 入力欄（`input`・`textarea`・`select`）に入力されている値 |
| `要素.textContent` | 要素の中のテキストを取得・書き換える |
| `要素.classList.toggle('クラス名', 条件)` | 条件が`true`ならクラスを付け、`false`なら外す |

### `querySelector`：CSSのセレクタで要素を取得する

```javascript
document.querySelector('a.doc-link');                 // クラス
document.querySelector('#count');                     // ID
document.querySelector('meta[name="csrf-token"]');    // 属性セレクタ
document.querySelectorAll('.card');                   // 一致するものすべて
```

| メソッド | 取得するもの | 見つからないとき |
|---|---|---|
| `getElementById('id')` | `id`が一致する要素1つ | `null` |
| `querySelector('セレクタ')` | 一致する**最初の**要素1つ | `null` |
| `querySelectorAll('セレクタ')` | 一致する要素**すべて**（`NodeList`） | 空の`NodeList`（`length`が`0`） |

`01_frontend/03_css_basics`で学んだセレクタがそのまま使えます。

### 属性の読み書き

```javascript
link.getAttribute('href');                      // 属性の値を読む
link.setAttribute('target', '_blank');          // 属性を追加・変更する
link.dataset.lang;                              // data-lang="..." の値（data-* 属性専用）
button.setAttribute('aria-expanded', 'true');   // 制作課題のハンバーガーメニューで使う
```

### 要素を作って追加する

```javascript
const li = document.createElement('li');   // 1. 要素を作る（まだ画面には無い）
li.className = 'card';                     // 2. class を設定する
li.textContent = memo.title;               //    中身を設定する
list.append(li);                           // 3. 画面上の要素に追加して、初めて表示される

li.remove();                               // 要素を消す
list.textContent = '';                     // 子要素をすべて消す
```

### `textContent`と`innerHTML`の違い（XSSに注意）

| プロパティ | 文字列の扱い | 安全性 |
|---|---|---|
| `textContent` | **ただの文字**として表示する | 安全 |
| `innerHTML` | **HTMLとして解釈**して表示する | ユーザーの入力を入れると危険 |

```javascript
const userInput = `<img src=x onerror="alert('乗っ取り')">`;
el.textContent = userInput;   // 文字列がそのまま表示される
el.innerHTML = userInput;     // <img> として解釈され、onerror のスクリプトが実行される
```

ユーザーが入力した文字列を`innerHTML`に入れると、悪意のあるタグやスクリプトがページ内で実行されてしまいます。これを**XSS（クロスサイトスクリプティング）**と呼びます。**ユーザーの入力やサーバーから受け取ったデータを表示するときは`textContent`を使う**のが原則です。`02_backend/06_jinja2`では、Jinja2が`{{ }}`の中身を自動でエスケープ（`<`などの記号を、タグとして働かない形に変換）して、同じ攻撃を防いでいることを学びます。

### 実行方法

`example/01_dom/index.html`をブラウザで直接開いてください。

### 動作確認：DOMを操作できているか

| 確認する操作 | 確認したいこと |
|---|---|
| テキストエリアに1文字入力する | `0 / 500文字`の`0`が`1`に変わる（`input`イベントのたびに`textContent`が書き換わる） |
| 文字を消していく（Backspace） | 文字数の表示もリアルタイムに減っていく |
| 450文字を超える文章を貼り付ける | 451文字目に達した瞬間、文字数の表示が赤字になる（`classList.toggle('over', length > 450)`） |
| 451文字以上の状態から文字を消して450文字以下に戻す | 赤字が元の色（グレー）に戻る（`toggle`は条件が`false`になるとクラスを自動で外す） |
| `textarea`の`maxlength="500"`を超えて入力しようとする | それ以上は入力できない（ブラウザの`maxlength`属性による制限で、JavaScriptのコードとは別の仕組み） |
| 「2. querySelector と属性の読み書き」を見る | `href=...`・`data-lang=ja`・`target=_blank（JavaScriptで追加）`と表示される。MDNのリンクをクリックすると新しいタブで開く |
| 「3. 要素を作って追加する」を見る | HTMLには空の`<ul>`しか書いていないのに、カテゴリのバッジ付きでメモが3件表示される。ElementsパネルでJavaScriptが作った`<li>`を確認できる |
| 「4. textContent と innerHTML の違い」を見る | textContentの欄には`<img ...>`という文字列がそのまま表示される |
| `01_dom/script.js`の`innerHTML`の行のコメントを外してリロードする（確認後は戻す） | 「乗っ取り」というアラートが出る（入力した文字列の中のスクリプトが実行された） |

**正常な状態の見分け方**：文字数の表示が「今テキストエリアに実際に入っている文字数」と常に一致していれば正常です。ズレている場合は`textarea.value.length`の取得タイミングやイベント名（`'input'`か`'change'`か）を疑ってください。

---

## 2. イベント

> [example/02_events/index.html](example/02_events/index.html) / [example/02_events/script.js](example/02_events/script.js)

クリック・入力・送信など、ページ上で起きた出来事を**イベント**と呼びます。`addEventListener('イベント名', コールバック関数)`で、そのイベントが起きたときに実行する処理を登録します。

### よく使うイベント

| イベント名 | 発生するタイミング | 主な対象 |
|---|---|---|
| `click` | クリックされたとき | ボタン・リンク |
| `input` | 入力欄の値が変わるたび（1文字ごと） | `input`・`textarea` |
| `change` | 値が確定したとき（チェックボックスの切り替え・`select`の選択など） | `select`・チェックボックス |
| `keydown` | キーが押されたとき | 入力欄・ページ全体 |
| `mouseenter` / `mouseleave` | マウスが要素に入ったとき / 出たとき（ホバー） | どの要素でも |
| `focus` / `blur` | 要素が選ばれた（フォーカスされた）とき / 外れたとき | ボタン・リンク・入力欄 |
| `submit` | フォームが送信されようとしたとき（ボタンのクリック・Enterキー） | `form` |

### イベントオブジェクト

コールバック関数は、引数で**イベントオブジェクト**を受け取れます。何が起きたかの情報が入っています。

```javascript
document.getElementById('buttons').addEventListener('click', (event) => {
    const button = event.target.closest('button');   // 実際にクリックされた要素から、最も近い button を探す
    if (!button) {
        return;
    }
    console.log(button.dataset.color, event.type);
});

input.addEventListener('keydown', (event) => {
    console.log(event.key);   // 押されたキー（'a'、'Enter' など）
});
```

| プロパティ・メソッド | 説明 |
|---|---|
| `event.target` | イベントが実際に起きた要素 |
| `event.type` | イベントの種類（`'click'`など） |
| `event.key` | 押されたキー（キーボードのイベント） |
| `event.preventDefault()` | ブラウザの**既定の動作**を止める（下で説明） |
| `要素.closest('セレクタ')` | 自分または祖先から、セレクタに合う最も近い要素を探す |

上の例のように、ボタン1つずつではなく**親要素に1回だけ**イベントを登録し、`event.target`で「どのボタンが押されたか」を判定する書き方もよく使われます（イベントは子から親へ伝わるため）。

### ホバーとフォーカス

マウスを要素に乗せること（**ホバー**）に反応するには、`mouseenter`と`mouseleave`を使います。

```javascript
button.addEventListener('mouseenter', () => { tip.hidden = false; });   // 乗せたら表示
button.addEventListener('mouseleave', () => { tip.hidden = true; });    // 外したら隠す
button.addEventListener('focus', () => { tip.hidden = false; });        // キーボードで選ばれたときも表示
button.addEventListener('blur', () => { tip.hidden = true; });
```

| 使い分け | 例 |
|---|---|
| 見た目を変えるだけなら、CSSの`:hover`・`:focus-visible`（03_css_basics 2節） | ボタンの色を変える・影を付ける |
| 中身を書き換える・別の要素を出す・処理を止めるなら、JavaScriptの`mouseenter`/`mouseleave` | ツールチップを作って表示する・スライドショーの自動再生を止める（07_js_ui 4節） |

| イベント | 違い |
|---|---|
| `mouseenter` / `mouseleave` | その要素に入ったとき・出たときに**1回だけ**発生する。普段はこちらを使う |
| `mouseover` / `mouseout` | 中の子要素に移るたびにも発生する（イベントが子から親へ伝わるため） |
| `focus` / `blur` | その要素自身が選ばれた・外れたときだけ発生する |
| `focusin` / `focusout` | 中の子要素が選ばれた・外れたときにも発生する（07_js_ui 4節で使う） |

スマホにはマウスが無いので、ホバーは起こりません。ホバーでしか見られない情報を作らず、`focus`やクリックでも同じ情報が見られるようにしておくと、キーボードやタッチ操作の人にも届きます。

### 既定の動作を止める：`preventDefault()`

ブラウザには、イベントごとに決まった「既定の動作」があります。

| 操作 | 既定の動作 |
|---|---|
| フォームの`submit` | 入力内容をサーバーに送信して、ページを移動する |
| リンクの`click` | `href`のページに移動する |
| フォームの`reset` | 入力内容を初期状態に戻す |

`event.preventDefault()`を呼ぶと、この既定の動作を止められます。送信前の入力チェックによく使います。

```javascript
form.addEventListener('submit', (event) => {
    if (!titleInput.value.trim()) {
        event.preventDefault();   // 送信を止める
        titleError.textContent = 'タイトルを入力してください';
    }
});
```

ボタンの`click`ではなくフォームの`submit`を監視すると、Enterキーでの送信も同じように扱えます。

> HTMLの`required`でも空欄は防げますが、空白だけの入力（`'   '`）は通ってしまいます。JavaScriptなら`trim()`を使った細かいチェックができます。ただし、ブラウザ側のチェックは開発者ツールなどで無効にできるので、`02_backend/09_forms`で**サーバー（Python）側でも必ずチェック**します。

### `confirm()`で確認する

```javascript
link.addEventListener('click', (event) => {
    if (!confirm('外部サイトに移動します。よろしいですか？')) {
        event.preventDefault();   // 「キャンセル」なら移動を止める
    }
});
```

`confirm('メッセージ')`は確認ダイアログを表示し、「OK」なら`true`、「キャンセル」なら`false`を返します。

Flaskのテンプレートでは、これをHTMLの属性（`onsubmit`）で短く書くこともあります。

```html
<button type="submit" onclick="return confirm('削除しますか？')">削除</button>
```

`onclick`属性の中で`false`を`return`すると、`preventDefault()`と同じく既定の動作（ここではフォームの送信）が止まります。つまり「キャンセル」を押すと`confirm()`が`false`を返し、削除のリクエストが送られません。

### 動作確認：イベントを受け取れているか

`example/02_events/index.html`をブラウザで開いて確認します。

| 確認する操作 | 確認したいこと |
|---|---|
| 「赤」「青」「緑」のボタンを押す | 押したボタンの色の名前と`event.type = click`が表示される（親要素の1つのリスナーで3つのボタンを処理している） |
| 下の入力欄でキーを押す | 押したキーの名前（`a`・`Enter`・`Shift`など）が表示される |
| タイトルを空、または空白だけにして「保存する」を押す | 送信されず、赤字のエラーメッセージが表示される |
| タイトルを入力して「保存する」、またはEnterキーを押す | 「◯◯を送信します」と表示される（`submit`を監視しているのでEnterキーでも同じ処理が動く） |
| 「MDNへ移動する」をクリックして「キャンセル」を選ぶ | ページが移動しない |
| 「削除」ボタンを押して「キャンセル」を選ぶ | フォームが送信されない（URLの末尾に`#`が付かない） |
| 「4. ホバーとフォーカス」のボタンにマウスを乗せる・Tabキーで移動する | どちらの方法でも、ボタンの上に説明（ツールチップ）が表示され、外れると消える |
| 点線の箱の中で、子要素の上を行き来する | `mouseover`の回数だけがどんどん増え、`mouseenter`は箱に入ったときだけ増える |


1節・2節を学んだら、次の3問に取り組みます。HTMLとCSSは完成しているので、`.js`ファイルを書いてブラウザで確認し、解答と見比べます。

### 練習問題1：動かない文字数カウンターを直す（デバッグ）

> 問題：[question/01_debug_counter/index.html](question/01_debug_counter/index.html)・[question/01_debug_counter/script.js](question/01_debug_counter/script.js) ｜ 解答：[question/answer/01_debug_counter/index.html](question/answer/01_debug_counter/index.html)・[question/answer/01_debug_counter/script.js](question/answer/01_debug_counter/script.js)

<details>
<summary>問題の内容を開く</summary>

`01_debug_counter/index.html`は「入力した文字数を表示する」はずのページですが、動きません。バグは3つあります（HTMLに1つ、`01_debug_counter/script.js`に2つ）。[05_js_basicsの0節](../05_js_basics/#0-javascriptの読み込み方とデバッグ)で学んだ、ConsoleのエラーメッセージとSourcesパネルのブレークポイントを使って、原因を見つけて直します。

| # | 進め方 |
|---|---|
| 1 | まずConsoleを開いてリロードし、赤字のエラーを読む（何行目の、何が`null` / `undefined`か） |
| 2 | エラーを1つ直したらリロードし、次のエラーを見る |
| 3 | エラーは出ないのに表示がおかしいときは、Sourcesパネルで`01_debug_counter/script.js`を開き、行番号をクリックしてブレークポイントを置く。入力して止まったら、変数にマウスを乗せて値を確認する |

| 確認する操作 | 確認したいこと |
|---|---|
| 文字を入力・削除する | 入力するたびに「◯文字」が正しく増減する |
| 21文字以上入力する | 文字数が赤字になる |
| Consoleを見る | エラーが出ていない |

</details>

### 練習問題2：配列のデータからメモカードを作る

> 問題：[question/02_memo_cards/index.html](question/02_memo_cards/index.html)・[question/02_memo_cards/script.js](question/02_memo_cards/script.js) ｜ 解答：[question/answer/02_memo_cards/index.html](question/answer/02_memo_cards/index.html)・[question/answer/02_memo_cards/script.js](question/answer/02_memo_cards/script.js)

<details>
<summary>問題の内容を開く</summary>

`02_memo_cards/script.js`の`memos`配列の5件を、カードとして表示します。`TODO 1`〜`TODO 4`を書きます。

| # | やること | ヒント |
|---|---|---|
| 1 | `createCard(memo)`：メモ1件分のカード要素を作って返す。構造は下のとおり（📌は`pinned`が`true`のときだけ） | `document.createElement()` / `要素.className` / `要素.textContent` / `要素.append()`。タイトルは`textContent`で入れる（`innerHTML`は使わない） |
| 2 | `render(items)`：渡された配列のメモをすべて表示する。`list`の中身を空にし、各メモを`createCard()`して`list`に追加し、`shownCount`に「◯件表示中」と表示する | `list.textContent = '';`で子要素をすべて消せる |
| 3 | ピン留めの件数を`pinnedCount`に「ピン留め：◯件」と表示する | `filter()`で`pinned`が`true`のものだけにして、`length`を数える |
| 4 | 検索欄に入力するたびに、タイトルに入力文字を含むメモだけを`render()`する | `'input'`イベント / `searchInput.value.trim()` / `文字列.includes()`。空欄のときは`includes('')`が常に`true`になるので、特別扱いしなくても全件表示になる |

```html
<li class="card">
    <span class="tag">家事</span>
    <span class="pin">📌</span>      <!-- pinned が true のときだけ -->
    <h2>買い物リスト</h2>
</li>
```

| 確認する操作 | 確認したいこと |
|---|---|
| ページを開く | 5件のカードが表示され、「ピン留め：2件 ／ 5件表示中」と表示される |
| 検索欄に「リスト」と入力する | 「買い物リスト」「旅行の持ち物リスト」の2件だけになり、「2件表示中」になる |
| 検索欄を空にする | 5件すべてに戻る |

</details>

### 練習問題3：フォームの送信前に入力をチェックする

> 問題：[question/03_form_validation/index.html](question/03_form_validation/index.html)・[question/03_form_validation/script.js](question/03_form_validation/script.js) ｜ 解答：[question/answer/03_form_validation/index.html](question/answer/03_form_validation/index.html)・[question/answer/03_form_validation/script.js](question/answer/03_form_validation/script.js)

<details>
<summary>問題の内容を開く</summary>

`03_form_validation/index.html`のフォームに、`submit`・`preventDefault`・`confirm`を使った入力チェックを付けます。HTMLの`required`などは、「JavaScriptだけで」チェックする練習のため、あえて付けていません。

| # | 仕様 |
|---|---|
| 1 | 「保存する」を押したとき（フォームの`submit`）に次をチェックし、問題があれば送信を止めて、各入力欄の下の`.error`にメッセージを表示する。問題が無い欄のメッセージは消す。タイトルが空白だけ・空なら「タイトルを入力してください」、本文が前後の空白を除いて10文字未満なら「本文は10文字以上で入力してください」 |
| 2 | エラーのある入力欄には`invalid`クラスを付ける（CSSで赤枠になる）。直ったら外す |
| 3 | すべて問題なければ、送信は止めたうえで`#result`に「保存しました：（タイトル）」と表示する（このページには送信先が無いため。`02_backend/09_forms`以降は実際にFlaskへ送信する） |
| 4 | 「クリア」ボタン（`type="reset"`）を押したとき、何か入力されていれば`confirm('入力内容を消しますか？')`で確認し、キャンセルなら消さない |

`03_form_validation/script.js`には次の3つを書きます。

| # | やること | ヒント |
|---|---|---|
| 1 | `showError(input, errorEl, message)`：エラー表示を切り替える関数。`message`が空文字なら、メッセージを消して`invalid`クラスを外す。`message`があれば、表示して`invalid`クラスを付ける | `errorEl.textContent = message;` / `input.classList.toggle('invalid', 条件)` |
| 2 | フォームの`submit`イベントで入力をチェックする（仕様1〜3） | `event.preventDefault()`で送信を止める。エラー文は`条件 ? 'エラー文' : ''`の形（三項演算子）で書くと短くなる |
| 3 | フォームの`reset`イベントで確認する（仕様4）。消す場合は、エラー表示と`#result`も消す | `reset`イベントでも`preventDefault()`で既定の動作（入力を消す）を止められる |

| 確認する操作 | 確認したいこと |
|---|---|
| 何も入力せずに「保存する」を押す | 2つの欄の下にエラーが表示され、枠が赤くなる |
| 正しく入力して「保存する」を押す | エラーが消え、「保存しました：（タイトル）」と表示される |
| 入力した状態で「クリア」を押し、確認でキャンセルする | 入力内容が残っている |

</details>

---

## 3. クライアント側での絞り込み

> [example/03_client_filter/index.html](example/03_client_filter/index.html) / [example/03_client_filter/script.js](example/03_client_filter/script.js)

この先の`02_backend/08_request`では、`request.args`を使ってサーバー（Flask）側でデータを絞り込む方法を学びます。ここでは同じ「絞り込み」を、**サーバーに問い合わせずJavaScriptだけ**で行います。

```javascript
const buttons = document.querySelectorAll('.filters button');
const cards = document.querySelectorAll('.card');

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        buttons.forEach((b) => b.classList.remove('active'));
        button.classList.add('active');

        const selected = button.dataset.category;   // data-category="..." の値を取得

        cards.forEach((card) => {
            const match = selected === 'all' || card.dataset.category === selected;
            card.classList.toggle('hidden', !match);
        });
    });
});
```

### ポイント

| 要素・メソッド | 説明 |
|---|---|
| `document.querySelectorAll('.card')` | 条件に一致する要素を**すべて**取得する（`NodeList`が返る） |
| `NodeList.forEach(関数)` | 取得した要素それぞれに対して処理を行う |
| `要素.dataset.category` | `data-category="..."`のようなカスタム属性の値を取得する |

### サーバー側の絞り込みとの違い

| | サーバー側（`02_backend/08_request`で学ぶ） | クライアント側（本章） |
|---|---|---|
| 絞り込みの実行場所 | Flask（Python） | ブラウザ（JavaScript） |
| ページの再読み込み | 発生する（新しいHTMLを受け取る） | 発生しない（今のページのまま） |
| 向いている場面 | データ件数が多い・全件を一度に送りたくない | 表示中のデータの中で切り替えたいだけ |

### 実行方法

`example/03_client_filter/index.html`をブラウザで直接開いてください（Flask不使用）。カテゴリボタンをクリックすると、ページ全体が再読み込みされずにカードの表示・非表示だけが切り替わることを確認できます。

### 動作確認：クリックしたカテゴリだけ表示されるか

| 確認する操作 | 確認したいこと |
|---|---|
| 初期表示を確認する | 「すべて」ボタンが`active`（青背景）になっており、4件のカードがすべて表示されている |
| 「仕事」ボタンをクリックする | 「仕事」ボタンだけが`active`になり、`data-category="仕事"`の2枚（企画会議メモ・資料作成）だけが残り、他の2枚（買い物リスト・読書メモ）が非表示になる |
| 続けて「趣味」ボタンをクリックする | 表示が切り替わり、「読書メモ」1枚だけが表示される（前に選んだ「仕事」の`active`は自動的に外れる） |
| 「すべて」ボタンをクリックする | 4枚のカードがすべて再表示される |
| 操作中にページ全体が再読み込みされていないか確認する | 再読み込みは発生しない（ブラウザのタブのリロードアイコンが回らない、スクロール位置も保持される） |

**正常な状態の見分け方**：クリックのたびに「押したボタンだけが`active`」「そのカテゴリに一致するカードだけが表示」の2つが同時に成立していれば正常です。片方だけ変化する場合は、`buttons.forEach`または`cards.forEach`のどちらか一方しか正しく動いていない可能性があります。


### 練習問題4：タグとキーワードの両方で絞り込む

> 問題：[question/04_tag_filter/index.html](question/04_tag_filter/index.html)・[question/04_tag_filter/script.js](question/04_tag_filter/script.js) ｜ 解答：[question/answer/04_tag_filter/index.html](question/answer/04_tag_filter/index.html)・[question/answer/04_tag_filter/script.js](question/answer/04_tag_filter/script.js)

<details>
<summary>問題の内容を開く</summary>

作品一覧を、タグのボタンとキーワードの検索欄の**両方**で絞り込みます。[example/03_client_filter](example/03_client_filter/index.html)との違いは、1つの作品が複数のタグを持つこと（`data-tags="HTML CSS"`のように空白区切り）と、2つの条件を両方満たす作品だけを表示することです。

| # | 仕様 |
|---|---|
| 1 | タグのボタンを押すと、押したボタンだけ`aria-pressed="true"`にし、他は`"false"`にする（CSSで`[aria-pressed="true"]`が青くなる） |
| 2 | 選ばれているタグを持つ作品だけを表示する。「すべて」（`data-tag="all"`）なら全件 |
| 3 | 検索欄に入力するたびに、タイトル（`h3`の文字）にキーワードを含む作品だけを表示する |
| 4 | 2と3は組み合わせて働く（例：「JavaScript」を選んで「アプリ」と入力→「メモ帳アプリ」「タイピングアプリ」だけ） |
| 5 | `#count`に「◯件表示中」と表示する。0件のときは`#empty`（「該当する作品はありません」）を表示する |

`04_tag_filter/script.js`には次の3つを書きます。

| # | やること | ヒント |
|---|---|---|
| 1 | `applyFilter()`：今の条件（`selectedTag`と検索欄の文字）で、作品の表示・非表示を切り替え、件数と0件のメッセージを更新する関数 | `'HTML CSS'.split(' ')`→`['HTML', 'CSS']`。`要素.dataset.tags`・`要素.querySelector('h3')`。表示・非表示は`要素.hidden = true / false` |
| 2 | タグのボタンが押されたら、`aria-pressed`を付け替え、`selectedTag`を押したボタンの`data-tag`の値にして`applyFilter()`を呼ぶ | |
| 3 | 検索欄に入力するたびに`applyFilter()`を呼ぶ | |

| 確認する操作 | 確認したいこと |
|---|---|
| 「Python」を押す | 「メモ帳アプリ」「蔵書管理ツール」の2件 |
| そのまま検索欄に「蔵書」と入力する | 「蔵書管理ツール」の1件 |
| 検索欄に「ゲーム」と入力する | 0件になり、「該当する作品はありません」が表示される |
| 「すべて」を押して検索欄を空にする | 6件すべて |

</details>

---

## 制作課題：オリジナルHP（ステップ3）

> [challenge/](challenge/) — 雛形 ｜ [challenge/answer/](challenge/answer/) — 完成例 ｜ 自分のHP：[00_my_homepage/](../00_my_homepage/)

ステップ2までで作ったHPに、`js/script.js`を作って動きを付けます。全ページで同じ`script.js`を読み込み、`if (要素)`で「そのページにある要素だけ」を操作します（05_js_basics 1節の「真偽の判定」）。

制作課題は、毎回次の2段階で進めます。

1. **`challenge/`で練習する**：架空の人物「山田 太郎」のサイトを題材に、ファイルの中のTODOコメントに沿って書きます。書けたら`challenge/answer/`の完成例と見比べます。
2. **自分のHPに反映する**：同じことを、[00_my_homepage/](../00_my_homepage/)の自分のサイトに行います。こちらは文章・配色・レイアウトを自分で考えて作ります。下の「必須要件」は、自分のHPで満たすべき要件です。

### challenge/ の内容

| ファイル | 内容 |
|---|---|
| `*.html` | 04_css_layoutの完成例に、☰ボタン（`#nav-toggle`）・絞り込みボタン（`#filters`）・各入力欄のエラー表示（`<p class="error" id="name-error">`など）・送信後のメッセージ（`#contact-result`）・`<script src="js/script.js">`を足したもの（完成済み） |
| `css/style.css` | 上の要素のスタイル（`.nav-links.open`・`.filters button.active`・`.work-card.hidden`・`.invalid`など）を追加済み |
| `js/script.js` | TODO 1〜3（ハンバーガーメニュー・制作実績の絞り込み・お問い合わせの入力チェック）を書く |

### 必須要件

| 要件 | 使う節 |
|---|---|
| 全ページで`js/script.js`を`</body>`の直前で読み込む | 05_js_basics 0 |
| **ハンバーガーメニュー**：狭い画面ではナビゲーションを折りたたみ、☰ボタンで開閉する。`aria-expanded`も切り替える | 1・2 |
| **一覧の絞り込み**：制作実績（または好きなもの紹介）をカテゴリやタグで絞り込むボタンを付ける。タグが複数ある項目は`data-tags="HTML/CSS JavaScript"`のように空白区切りで持たせ、`split(' ')`と`includes()`で判定する | 05_js_basics 2・3 |
| **お問い合わせの入力チェック**：`submit`で入力をチェックし、問題があれば各欄の下にエラーを表示する。問題が無ければ「送信しました」などのメッセージを表示する（静的なサイトなので、送信自体は`preventDefault()`で止める） | 05_js_basics 1・2 |
| すべてのページを操作しても、Consoleに赤字のエラーが出ない | 05_js_basics 0 |

### 自由課題（1つ以上）

必須要件に加えて、自分のサイトに合う動きを1つ以上考えて付けてみましょう。

| 例 | ヒント |
|---|---|
| ページ上部へ戻るボタン | 300pxスクロールしたら表示し、`window.scrollTo({ top: 0, behavior: 'smooth' })`で戻る（07_js_ui 5節） |
| ダークモードの切り替えボタン | `document.body.classList.toggle('dark')`と、`.dark`のときだけCSS変数を差し替えるCSS |
| よくある質問の開閉 | 質問をクリックしたら、答えの要素に`open`クラスを付け外しする |
| 今日の日付やあいさつの表示 | `new Date().getHours()`で時間帯によってメッセージを変える |
| プロフィールをタブで切り替える | 「基本情報」「スキル」「経歴」をタブにする（07_js_ui 1節） |
| 作品の詳細をモーダルウィンドウで表示する | 作品カードをクリックすると`<dialog>`で詳しい説明を出す（07_js_ui 3節） |
| ホームで作品をスライドショーにする | 前へ・次へと自動再生。ホバー中は止める（07_js_ui 4節） |
| スクロールで要素をふわっと表示する | `IntersectionObserver`で画面に入ったらクラスを付ける（07_js_ui 5節） |
| お問い合わせの送信後に通知を出す | `popover="manual"`と`setTimeout`で、数秒で消える通知（07_js_ui 2節） |
| ナビやボタンにツールチップを付ける | `mouseenter`・`focus`で説明を表示する（2節） |

### 進め方のヒント

1. まずハンバーガーメニューを作る。全ページに効くので、動けばすぐ実感できる
2. 絞り込みは、HTMLの各項目に`data-tags`を付けるところから始める
3. 入力チェックは練習問題3がそのまま使える
4. [challenge/answer/js/script.js](challenge/answer/js/script.js)と比べる

### 動作確認：challenge/

| 確認する操作 | 確認したいこと |
|---|---|
| 幅375pxで☰を押す | メニューが開閉し、Elementsで`aria-expanded`が切り替わる |
| `works.html`で「Python」を押す | 「メモ帳アプリ」「蔵書管理ツール」の2件だけが残る |
| `contact.html`で何も入力せずに送信する | 3つの欄の下にエラーが表示され、枠が赤くなる。正しく入力すると、お礼のメッセージが表示される |
| すべてのページでConsoleを見る | 赤字のエラーが出ていない |

## 次のステップ

続きは [07_js_ui](../07_js_ui/) です。タブ・ポップアップ・モーダルウィンドウ・スライドショー・スクロール動作など、よく使うUIを作ります。

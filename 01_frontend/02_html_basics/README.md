# 02 HTMLの基礎

> フロントエンド編 ／ 前の章：[01_web_basic](../01_web_basic/) ／ 次の章：[03_html_semantic_form](../03_html_semantic_form/)

HTML（HyperText Markup Language）は、文章に**タグで意味付け**をする言語です。「ここは見出し」「ここはリンク」「ここは表」といった**構造と意味**を表し、見た目（色・大きさ・配置）は[04_css_basics](../04_css_basics/)で扱います。

この章では、学習環境と開発者ツールの使い方を確認したうえで、HTML文書の骨組み・文章で使う基本のタグ・表の書き方を学びます。

## 目次

0. [はじめに：学習環境と開発者ツール](#0-はじめに学習環境と開発者ツール)
1. [HTML文書の骨組み](#1-html文書の骨組み)
2. [テキストと基本タグ](#2-テキストと基本タグ)
3. [表（table）](#3-表table)

---

## フォルダ構成

```
01_frontend/02_html_basics/
├── README.md
├── example/                      サンプル（1つのサンプル＝1つのフォルダ）
│   ├── 01_structure/             HTML文書の骨組み（doctype・head・要素・属性）
│   │   └── index.html
│   ├── 02_text/                  テキストと基本タグ（見出し・リンク・リスト・画像・ブロック/インライン）
│   │   ├── index.html
│   │   └── img/sample.png
│   └── 03_table/                 表（thead/tbody・scope・colspan/rowspan）
│       └── index.html
└── question/                     練習問題（3問。問題文はREADMEの各節の最後）
    ├── 01_profile_page/          練習問題1：骨組みから自己紹介ページを作る
    │   └── index.html
    ├── 02_recipe_page/           練習問題2：レシピのページを作る
    │   ├── index.html
    │   └── img/sample.png
    ├── 03_memo_table/            練習問題3：メモの集計表を作る
    │   └── index.html
    └── answer/                   解答（問題と同じ名前のフォルダ。中のファイル構成も問題と同じ）
        ├── 01_profile_page/
        ├── 02_recipe_page/
        └── 03_memo_table/
```

---

## 0. はじめに：学習環境と開発者ツール

### ページの開き方

この章のファイルはすべて、**ブラウザで直接開くだけ**で動きます（Finderでダブルクリック、またはブラウザにドラッグ&ドロップ）。

VS Codeの拡張機能「Live Server」を使うと、ファイルを保存するたびにブラウザが自動でリロードされるので便利です（[00_docs/setup/vscode.md](../../00_docs/setup/vscode.md#htmlcssフロントエンド)を参照）。Pythonの簡易サーバーでも確認できます。

```bash
cd 01_frontend/02_html_basics
python -m http.server 8000
# → http://localhost:8000/example/01_structure/index.html などを開く
```

### 開発者ツール（DevTools）

HTML/CSSの学習で一番使う道具です。ブラウザ上で`F12`（Mac：`Cmd + Option + I`）を押すと開きます。

| パネル | できること |
|---|---|
| Elements（要素） | HTMLの構造をツリーで見る。要素をクリックすると、その要素に当たっているCSSが右側に表示される |
| Styles（スタイル） | 当たっているCSSルールの一覧。**負けたルールには取り消し線**が付く（01_frontend/04_css_basicsの3節で使う）。値をその場で書き換えて試せる |
| Computed（計算済み） | 最終的に決まった値と、ボックスモデル（margin/border/padding/content）の図 |
| デバイスツールバー | `Cmd + Shift + M`（Windows：`Ctrl + Shift + M`）。スマホやタブレットの画面幅を再現する（01_frontend/05_css_layoutの4節で使う） |
| Flex / Grid バッジ | Elementsで`display: flex`/`grid`の要素の横に出るバッジをクリックすると、行・列・隙間が図示される（01_frontend/05_css_layoutの1・2節で使う） |

### 困ったときの調べ方

| 道具 | 用途 |
|---|---|
| [MDN Web Docs](https://developer.mozilla.org/ja/) | HTMLタグ・CSSプロパティの公式級リファレンス。「MDN flex-wrap」のように検索する |
| [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) | HTMLを貼り付けると、閉じ忘れや不正な入れ子を指摘してくれる |
| [Can I use](https://caniuse.com/) | そのCSS機能がどのブラウザで使えるかを調べる |

### 動作確認：開発者ツールが使えるか

| 確認する操作 | 確認したいこと |
|---|---|
| 任意のサンプルを開き、`F12`で開発者ツールを開く | Elementsパネルに`<html>`から始まるツリーが表示される |
| Elementsで`<h1>`をクリックし、Stylesで`color`の値をクリックして`red`に書き換える | ページ上の見出しが赤くなる（リロードすると元に戻る。ファイルは変わらない） |

---

## 1. HTML文書の骨組み

> [example/01_structure/index.html](example/01_structure/index.html)

```html
<!doctype html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ページのタイトル</title>
</head>
<body>
    <h1>見出し</h1>
    <p>段落</p>
</body>
</html>
```

### 骨組みの各部分

| 部分 | 役割 |
|---|---|
| `<!doctype html>` | 「HTML5の文書です」という宣言。必ず1行目。無いとブラウザが古い互換モードで表示する |
| `<html lang="ja">`（HyperText Markup Language） | 文書全体のルート要素。`lang`で言語を伝える（読み上げソフトの発音・翻訳機能・フォント選択に使われる） |
| `<head>` | ページの設定情報（画面には表示されない） |
| `<meta charset="UTF-8">`（metadata：ページについての情報） | 文字コード。無いと日本語が文字化けすることがある |
| `<meta name="viewport" ...>` | スマホで正しい幅で表示させる（01_frontend/05_css_layoutの4節） |
| `<title>` | ブラウザのタブ・ブックマーク・検索結果に表示されるタイトル |
| `<body>` | 画面に表示される内容 |

### 用語：要素・タグ・属性

```
  開始タグ        内容        終了タグ
<a href="/memos">メモ一覧</a>
   └─属性─┘
└──────────── 要素 ────────────┘
```

| 用語 | 説明 |
|---|---|
| 要素 | 開始タグ〜終了タグまでのひとまとまり |
| 属性 | 開始タグに付ける追加情報。`名前="値"`の形 |
| 空要素 | 内容を持たず終了タグが無い要素（`<br>`・`<img>`・`<input>`・`<meta>`・`<link>`など） |
| 入れ子 | 要素の中に要素を入れること。**後に開いたものから先に閉じる**（`<strong><em>…</em></strong>`） |
| 文字参照 | `©`→`&copy;`のように、キーボードで打ちにくい記号を表示する書き方 |

HTMLでは**連続する空白・改行は1つの空白にまとめられます**。ソース上で改行しても画面では改行されません（改行したいなら段落を分けるか`<br>`）。

### 動作確認：骨組みの役割

| 確認する操作 | 確認したいこと |
|---|---|
| `01_structure/index.html`を開く | ブラウザのタブに「HTML文書の骨組み」と表示される（`<title>`） |
| `<meta charset="UTF-8">`を一時的に削除して保存・リロードする（確認後は戻す） | 環境によっては日本語が文字化けする |
| ソース上で改行している段落を見る | 画面では1行につながって表示される |
| 開発者ツールのElementsで`<head>`を開く | `<meta>`や`<title>`は存在するが、画面には表示されていないことがわかる |


### 練習問題1：骨組みから自己紹介ページを作る

> 問題：[question/01_profile_page/index.html](question/01_profile_page/index.html) ｜ 解答：[question/answer/01_profile_page/index.html](question/answer/01_profile_page/index.html)

<details>
<summary>問題の内容を開く</summary>

`01_profile_page/index.html`には、まだ何も書いてありません。骨組み（doctype・`html`・`head`・`body`）から、次の自己紹介ページを自分で書きます。

```
タブ：自己紹介 | 山田 太郎

┌───────────────────────────────────────────┐
│ 山田 太郎の自己紹介                           │  ← 大見出し
│                                             │
│ はじめまして。Webアプリ開発を勉強しています。      │  ← 段落
│                                             │
│ 今の目標は自分のホームページを公開することです。    │  ← 「自分のホームページを公開すること」は重要かつ強調したい部分
│                                             │
│ © 2026 山田 太郎                              │  ← 著作権表示
└───────────────────────────────────────────┘
```

| # | 条件 |
|---|---|
| 1 | 1行目は doctype 宣言にする |
| 2 | `html`要素に、日本語の文書であることを示す属性を付ける |
| 3 | `head`に、文字コード（UTF-8）・スマホ用のviewport・タイトル「自己紹介 \| 山田 太郎」の3つを書く |
| 4 | 「自分のホームページを公開すること」は`strong`と`em`の両方で囲む（入れ子の閉じる順番に注意） |
| 5 | 「©」は、文字参照を使って表示する |
| 6 | 「はじめまして。…」の段落は、ソース上ではわざと「はじめまして。」で改行して2行に分けて書く |

<details>
<summary>ヒント：使うタグ</summary>

| タグ・属性 | 使う場所 |
|---|---|
| `<!doctype html>` | 1行目の宣言 |
| `<html lang="ja">` | 文書全体を囲む |
| `<head>` / `<body>` | 設定情報 / 画面に表示する内容 |
| `<meta charset="UTF-8">` | 文字コード |
| `<meta name="viewport" content="width=device-width, initial-scale=1">` | スマホ用の表示幅 |
| `<title>` | タブに出るタイトル |
| `<h1>` | 大見出し「山田 太郎の自己紹介」 |
| `<p>` | 各段落（3つ） |
| `<strong>` / `<em>` | 「自分のホームページを公開すること」（重要＋強調） |
| `&copy;` | 「©」の文字参照 |

</details>

| 確認する操作 | 確認したいこと |
|---|---|
| ブラウザで開く | タブに「自己紹介 \| 山田 太郎」と表示される |
| 最後の行を見る | 「© 2026 山田 太郎」と、©の記号が表示される |
| 条件6の段落を見る | 画面では1行につながって表示される（改行が空白1つにまとめられる） |
| 開発者ツールのElementsで`<head>`を開く | `meta`や`title`があるのに、画面には表示されていない |
| [W3C Validator](https://validator.w3.org/#validate_by_input)に貼り付ける | エラーが0件 |

</details>

---

## 2. テキストと基本タグ

> [example/02_text/index.html](example/02_text/index.html)

```html
<h1>ページの大見出し</h1>
<h2>節の見出し</h2>
<p><strong>重要</strong>な部分と<em>強調</em>したい部分</p>

<a href="https://developer.mozilla.org/ja/">外部サイト（絶対パス）</a>
<a href="../01_structure/index.html">別のフォルダのページ（相対パス）</a>
<a href="#images">ページ内リンク（id="images" の要素へ）</a>
<a href="https://example.com" target="_blank" rel="noopener noreferrer">新しいタブで開く</a>

<ul><li>順序なしリスト</li></ul>
<ol><li>順序ありリスト</li></ol>
<dl><dt>用語</dt><dd>説明</dd></dl>

<img src="img/sample.png" alt="画像の内容の説明" width="150" height="150">
```

### ポイント

| タグ | 役割 |
|---|---|
| `<h1>`〜`<h6>`（heading） | 見出し。**ページの目次**になる。`h1`は基本1ページに1つ、レベルを飛ばさない（`h2`の次にいきなり`h4`にしない） |
| `<p>`（paragraph） | 段落 |
| `<strong>` / `<em>`（emphasis） | 「重要」「強調」という**意味**。見た目だけ太字にしたいならCSS（`font-weight`） |
| `<a href="...">`（anchor） | リンク。`target="_blank"`で新しいタブ。その場合は`rel="noopener noreferrer"`をセットで付ける（開いた先のページから元のページを操作されるのを防ぐ） |
| `<ul>` / `<ol>` / `<li>`（unordered list / ordered list / list item） | 順序なし／順序ありリスト。入れ子のリストは`<li>`の**中**に書く |
| `<dl>` / `<dt>` / `<dd>`（description list / description term / description details） | 用語と説明のリスト |
| `<img>`（image） | 画像。`alt`は必須（画像が表示できないとき・読み上げソフト用）。`width`/`height`を書くと読み込み中のレイアウトのガタつきを防げる |
| `<div>`（division） / `<span>` | 意味を持たない汎用の箱。`div`は**ブロック要素**、`span`は**インライン要素** |
| `<code>` / `<kbd>`（keyboard） / `<blockquote>` / `<small>` / `<hr>`（horizontal rule） | コード・キー操作・引用・注記・話題の区切り |

### パスの書き方

| 書き方 | 例 | 意味 |
|---|---|---|
| 絶対URL | `https://example.com/a.html` | 外部サイト |
| 相対パス | `img/sample.png` | 今のファイルから見た位置 |
| 親フォルダ | `../01_structure/index.html` | 1つ上のフォルダへ戻ってから、別のフォルダに入る |
| ルート相対 | `/static/style.css` | サイトのルートから（`02_backend/04_flask_basic`以降のFlaskでよく使う） |
| ページ内 | `#images` | 同じページの`id="images"`の要素へ |

### ブロック要素とインライン要素

| 種類 | 代表 | 振る舞い |
|---|---|---|
| ブロック要素 | `div`・`p`・`h1`・`ul`・`section` | 横幅いっぱいに広がり、前後で改行される |
| インライン要素 | `span`・`a`・`strong`・`em`・`img` | 文章の流れの中に収まり、改行されない。`width`/`height`が効かない |

この性質はCSSの`display`で変えられます（01_frontend/04_css_basicsの4節）。

### 動作確認：タグごとの意味と見た目

| 確認する操作 | 確認したいこと |
|---|---|
| `02_text/index.html`を開く | 見出しの大小・リストの記号（`ul`は黒丸、`ol`は数字）・入れ子リストのインデントが表示される |
| 「MDN HTMLリファレンス（新しいタブ）」をクリック | 新しいタブで開く |
| 「このページの『画像』へジャンプ」をクリック | ページ内の「画像」見出しまでスクロールし、URLの末尾に`#images`が付く |
| `<img>`の`src`を存在しない名前に書き換えてリロード（確認後は戻す） | 画像の代わりに`alt`の文字が表示される |
| 2つの`div`と`span`の背景色を見比べる | `div`は横幅いっぱい・改行される、`span`は文字の部分だけに背景が付く |

**正常な状態の見分け方**：レイアウトが崩れる場合、タグの閉じ忘れが最も多い原因です。[W3C Validator](https://validator.w3.org/#validate_by_input)にソースを貼り付けて確認しましょう。


### 練習問題2：レシピのページを作る

> 問題：[question/02_recipe_page/index.html](question/02_recipe_page/index.html) ｜ 解答：[question/answer/02_recipe_page/index.html](question/answer/02_recipe_page/index.html)

<details>
<summary>問題の内容を開く</summary>

次の内容を、この節のタグを使って`02_recipe_page/index.html`の`body`に書きます。CSSは書いてあるので触らなくてOKです（04_css_basicsで学びます）。

```
ホットケーキの作り方                          ← ページの大見出し（1つだけ）
[目次] 材料へ / 作り方へ                       ← ページ内リンク（#ingredients・#steps へ）
(画像：img/sample.png、150×150)            ← 画像の内容を説明する alt を付ける
休日の朝にぴったりの、ふわふわのホットケーキです。焦がさないことが一番大事です。
                                            ↑「焦がさないこと」は重要な部分

材料（2枚分）                                 ← 節の見出し。id="ingredients"
  ・ホットケーキミックス 150g                  ← 順序なしリスト
  ・卵 1個
  ・牛乳 100ml

作り方                                       ← 節の見出し。id="steps"
  1. ボウルに卵と牛乳を入れて混ぜる              ← 順序ありリスト
  2. ホットケーキミックスを加えて、さっくり混ぜる
       ・混ぜすぎない                          ← 2番の中に入れ子の順序なしリスト
       ・粉っぽさが少し残るくらいでOK
  3. 弱火で3分焼き、裏返して2分焼く

用語                                        ← 節の見出し
  さっくり混ぜる： ヘラで切るように、練らずに混ぜること     ← 用語と説明のリスト
  弱火： 炎の先がフライパンの底に当たらない程度の火加減

参考：MDN Web Docs（新しいタブで開く）          ← https://developer.mozilla.org/ja/ へのリンク
```

| # | 条件 |
|---|---|
| 1 | 見出しのレベルを飛ばさない（`h1`の次は`h2`） |
| 2 | 「焦がさないこと」は意味として重要なので、それに合うタグを使う |
| 3 | 入れ子のリストは、2番の`<li>`の**中**に書く |
| 4 | 画像には`alt`・`width`・`height`を書く |
| 5 | 新しいタブで開くリンクには、`target`とセットで付ける属性を忘れない |

<details>
<summary>ヒント：使うタグ</summary>

| タグ・属性 | 使う場所 |
|---|---|
| `<h1>` / `<h2 id="...">` | ページの大見出し / 節の見出し（`id="ingredients"`・`id="steps"`） |
| `<a href="#...">` | 目次のページ内リンク |
| `<a href="..." target="_blank" rel="noopener noreferrer">` | 新しいタブで開くMDNへのリンク |
| `<img src="..." alt="..." width="150" height="150">` | 画像 |
| `<p>` / `<strong>` | 紹介文 / 「焦がさないこと」 |
| `<ul>` / `<li>` | 材料のリスト・2番の中の入れ子リスト |
| `<ol>` / `<li>` | 作り方の手順 |
| `<dl>` / `<dt>` / `<dd>` | 用語と説明 |

</details>

| 確認する操作 | 確認したいこと |
|---|---|
| 「材料へ」「作り方へ」を押す | その見出しまで移動し、URLの末尾に`#ingredients`などが付く |
| MDNのリンクを押す | 新しいタブで開く |
| 画像の`src`を存在しない名前に変える（確認後は戻す） | `alt`の文字が表示される |

</details>

---

## 3. 表（table）

> [example/03_table/index.html](example/03_table/index.html)

```html
<table>
    <caption>今週のメモ件数</caption>
    <thead>
        <tr><th scope="col">カテゴリ</th><th scope="col">件数</th></tr>
    </thead>
    <tbody>
        <tr><th scope="row">家事</th><td>3</td></tr>
        <tr><th scope="row">仕事</th><td>5</td></tr>
    </tbody>
    <tfoot>
        <tr><th scope="row">合計</th><td>8</td></tr>
    </tfoot>
</table>
```

### ポイント

| タグ・属性 | 役割 |
|---|---|
| `<table>` / `<tr>`（table row） / `<th>`（table header） / `<td>`（table data） | 表 / 行 / 見出しセル / データセル |
| `<caption>` | 表のタイトル |
| `<thead>` / `<tbody>` / `<tfoot>`（table head / table body / table foot） | 見出し行 / データ行 / 集計行のグループ |
| `scope="col"` / `scope="row"` | その`th`が「列」の見出しか「行」の見出しか（読み上げソフトがセルと見出しを対応付けられる） |
| `colspan="2"` / `rowspan="2"` | 右方向 / 下方向にセルを結合する。結合された側のセルは**書かない** |

表は**表形式のデータ**のためのものです。昔は表でページのレイアウトを組んでいましたが、今はCSSのFlexbox/Grid（01_frontend/05_css_layoutの1・2節）を使います。表は`02_backend/10_sql`以降でデータベースの中身を一覧表示するときに再登場します。

### 動作確認：セルの結合

| 確認する操作 | 確認したいこと |
|---|---|
| `03_table/index.html`を開く | 「今週のメモ件数」の表の上にキャプションが表示され、見出し行に背景色が付く |
| 時間割の表を見る | 「HTML/CSS」が縦2マス分、「昼休み」が横2マス分を占めている |
| 月曜2限の`<td>`を1つ追加してみる（確認後は戻す） | 表の右側に余計なセルがはみ出す（`rowspan`で使われている場所にはセルを書かない理由がわかる） |


### 練習問題3：メモの集計表を作る

> 問題：[question/03_memo_table/index.html](question/03_memo_table/index.html) ｜ 解答：[question/answer/03_memo_table/index.html](question/answer/03_memo_table/index.html)

<details>
<summary>問題の内容を開く</summary>

次のデータを、`03_memo_table/index.html`に`table`で書きます。CSSは書いてあるので触らなくてOKです。

```
┌────────────────────────────────────────┐
│          カテゴリ別メモ件数（10月）          │  ← caption
├──────────┬───────────┬──────────┬──────┤
│ カテゴリ  │  第1週     │  第2週    │ 合計  │  ← thead
├──────────┼───────────┼──────────┼──────┤
│ 家事      │  3        │  2       │  5   │
│ 仕事      │  4        │  6       │ 10   │  ← tbody
│ 趣味      │  集計中（2列分を結合）  │  -   │
├──────────┼───────────┴──────────┼──────┤
│ 合計      │                       │ 15   │  ← tfoot
└──────────┴──────────────────────┴──────┘
```

| # | 条件 |
|---|---|
| 1 | `caption`で表のタイトルを付ける |
| 2 | `thead`/`tbody`/`tfoot`で行をグループ分けする |
| 3 | 列の見出しは`<th scope="col">`、各行の先頭（カテゴリ名）は`<th scope="row">`にする |
| 4 | 「集計中」のセルと、`tfoot`の真ん中の空白セルは、`colspan`で2列分を結合する |
| 5 | 「集計中」のセルには`class="note"`を付ける（CSSで中央寄せ・灰色になる） |

<details>
<summary>ヒント：使うタグ</summary>

| タグ・属性 | 使う場所 |
|---|---|
| `<table>` | 表全体 |
| `<caption>` | 表のタイトル |
| `<thead>` / `<tbody>` / `<tfoot>` | 見出し行 / データ行 / 合計行のグループ |
| `<tr>` | 1行 |
| `<th scope="col">` / `<th scope="row">` | 列の見出し / 各行の先頭のカテゴリ名 |
| `<td>` | データのセル |
| `colspan="2"` | 「集計中」と`tfoot`の空白セル（2列分を結合） |

</details>

| 確認する操作 | 確認したいこと |
|---|---|
| ブラウザで開く | 見出し行に色が付き、`tbody`の偶数行が縞模様になる（正しいタグで書けている） |
| 「集計中」「合計」の行を見る | セルが2列分に広がり、右端の「合計」列がずれていない |

</details>

---

## 次のステップ

続きは [03_html_semantic_form](../03_html_semantic_form/) です。意味の伝わるページの構造（セマンティックHTML）とフォームを学び、オリジナルHPのHTMLを書きます。

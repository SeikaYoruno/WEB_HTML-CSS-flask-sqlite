# 04 CSSの基礎

> フロントエンド編 ／ 前の章：[03_html_semantic_form](../03_html_semantic_form/) ／ 次の章：[05_css_layout](../05_css_layout/)

CSS（Cascading Style Sheets）は、HTMLの要素に**見た目**を指定する言語です。

```css
セレクタ {
    プロパティ: 値;
    プロパティ: 値;
}
```

「**どの要素に**（セレクタ）」「**何を**（プロパティ）」「**どうする**（値）」の3つで1つのルールになります。

この章では、CSSの書き方・色と単位・セレクタ・「どのルールが勝つか」を決めるカスケード・すべての要素の土台となるボックスモデル・文字や背景の装飾を学びます。レイアウト（要素を横に並べる・格子状に並べる・画面幅に合わせる）は、次の[05_css_layout](../05_css_layout/)で扱います。

> 開発者ツールの使い方は[02_html_basicsの「0. はじめに」](../02_html_basics/#0-はじめに学習環境と開発者ツール)にまとめてあります。この章では特に、**Styles**パネル（取り消し線で負けたルールがわかる）と**Computed**パネル（ボックスモデルの図）をよく使います。

## 目次

1. [CSSの書き方と単位](#1-cssの書き方と単位)
2. [セレクタ](#2-セレクタ)
3. [カスケード・詳細度・継承](#3-カスケード詳細度継承)
4. [ボックスモデルとdisplay](#4-ボックスモデルとdisplay)
5. [文字・色・背景・装飾](#5-文字色背景装飾)

---

## フォルダ構成

```
01_frontend/04_css_basics/
├── README.md
├── example/                      サンプル（1つのサンプル＝1つのフォルダ）
│   ├── 01_css_basics/            CSSの書き方・色・単位（px/%/em/rem/vw）
│   │   ├── index.html
│   │   └── css/style.css
│   ├── 02_selectors/             セレクタ（結合子・属性・疑似クラス・疑似要素）
│   │   └── index.html
│   ├── 03_cascade/               カスケード・詳細度・継承
│   │   └── index.html
│   ├── 04_box_model/             ボックスモデル・box-sizing・マージン相殺・display・overflow
│   │   └── index.html
│   └── 05_typography/            文字・行の高さ・背景・角丸・影
│       └── index.html
└── question/                     練習問題（5問。問題文はREADMEの各節の最後）
    ├── 01_external_css/          練習問題1：style属性のCSSを外部ファイルに移す
    │   ├── index.html
    │   └── css/style.css
    ├── 02_selectors/             練習問題2：プロパティに合うセレクタを書く
    │   └── index.html
    ├── 03_specificity_quiz/      練習問題3：何色になるか予想する（詳細度クイズ）
    │   └── index.html
    ├── 04_box_model/             練習問題4：箱の大きさを計算し、レイアウトを直す
    │   └── index.html
    ├── 05_article_style/         練習問題5：記事ページを読みやすく装飾する
    │   └── index.html
    └── answer/                   解答（問題と同じ名前のフォルダ。中のファイル構成も問題と同じ）
        ├── 01_external_css/
        ├── 02_selectors/
        ├── 03_specificity_quiz/
        ├── 04_box_model/
        └── 05_article_style/
```

---

## 1. CSSの書き方と単位

> [example/01_css_basics/index.html](example/01_css_basics/index.html) ／ [example/01_css_basics/css/style.css](example/01_css_basics/css/style.css)

### CSSを書く3つの場所

```html
<!-- ① 外部ファイル（実務の基本） -->
<link rel="stylesheet" href="css/style.css">

<!-- ② <style>タグ（そのページだけのCSS） -->
<style>
    .from-style-tag { color: #d1723f; }
</style>

<!-- ③ style属性（インラインスタイル） -->
<p style="color: #2f9e44;">...</p>
```

| 書き方 | 使いどころ |
|---|---|
| ① 外部ファイル | **基本はこれ**。複数ページで同じCSSを共有でき、HTMLと見た目を分離できる。Flaskでは`static/style.css`に置く |
| ② `<style>`タグ | 1ページだけのサンプル・試作（この章の`example/`はほぼこれ） |
| ③ `style`属性 | 原則使わない。使い回せず、優先度が強すぎて後から上書きしにくい（3節） |

### 色の書き方

| 書き方 | 例 | 説明 |
|---|---|---|
| 色名 | `royalblue` | 決まった名前の色 |
| 16進数 | `#3f6fd1` | 赤・緑・青を2桁ずつ。最もよく使う |
| `rgb()` | `rgb(63 111 209)`、`rgb(63 111 209 / 0.5)` | `/ 0.5`で半透明 |
| `hsl()` | `hsl(220 62% 53%)` | 色相・彩度・明度。「同じ色で少し明るく」が作りやすい |

### 長さの単位

| 単位 | 基準 | 主な用途 |
|---|---|---|
| `px` | 画面上の1点 | 枠線・細かい余白 |
| `%` | 親要素のサイズ | 幅 |
| `em` | **その要素自身**の文字サイズ（`font-size`に使うと親の文字サイズ） | ボタンの内側余白など、文字の大きさに比例させたいもの |
| `rem` | **ルート（`html`）**の文字サイズ（通常16px） | **文字サイズ**・余白。入れ子の影響を受けないので計算しやすい |
| `vw` / `vh` | 画面の幅 / 高さの1% | 画面いっぱいの要素・流動的なサイズ |

文字サイズを`rem`で指定すると、ブラウザの設定で文字を大きくしたユーザーにも対応できます。

### 動作確認：3つの書き方と単位

| 確認する操作 | 確認したいこと |
|---|---|
| `01_css_basics/index.html`を開く | 3つの段落が青・橙・緑で表示される（それぞれ別の場所に書いたCSSが効いている） |
| `01_css_basics/css/style.css`の`.from-link`の色を`red`に変えて保存・リロード | ①の段落だけ赤くなる（外部ファイルが読み込まれている） |
| ウィンドウ幅を変える | `200px`のバーは変わらず、`50%`と`30vw`のバーは幅が変わる |
| `em`と`rem`の子要素の文字サイズを開発者ツールのComputedで確認 | `1.5em`は30px、`1.5rem`は24pxになっている |


### 練習問題1：style属性のCSSを外部ファイルに移す

> 問題：[question/01_external_css/index.html](question/01_external_css/index.html)・[question/01_external_css/css/style.css](question/01_external_css/css/style.css) ｜ 解答：[question/answer/01_external_css/index.html](question/answer/01_external_css/index.html)・[question/answer/01_external_css/css/style.css](question/answer/01_external_css/css/style.css)

<details>
<summary>問題の内容を開く</summary>

`01_external_css/index.html`は、見た目をすべて`style`属性で書いてあります。同じ見た目のまま、CSSを`css/style.css`に移します。ファイルの中の`TODO 1`〜`TODO 7`の場所に書きます。

| # | 書く場所 | やること |
|---|---|---|
| 1 | `01_external_css/index.html`の`<head>` | `css/style.css`を読み込む`<link>`を書く |
| 2 | `01_external_css/index.html`の`<body>` | `style`属性をすべて削除し、代わりにクラスを付ける：青い部分の`div`→`hero`、その下の`div`→`content`、お知らせの3つの段落→`notice`、通常のボタン→`button`、大きいボタン→`button large`（クラスは空白で区切って2つ付けられる） |
| 3 | `.hero` | 高さを「画面の高さの40%」にする（元は320px固定） |
| 4 | `.hero h1`・`.hero p`・`.content h2` | 文字サイズを`rem`で書く（元は40px・18px・24px。16px＝1rem） |
| 5 | `.notice` | 背景を`#3f6fd1`（＝`rgb(63 111 209)`）の15%の半透明にし、文字色を`#3f6fd1`にする（背景が薄くなったので、白い文字では読めない） |
| 6 | `.button` | 内側の余白を`em`で書く（文字サイズ16pxのとき、上下8px・左右16pxになるように） |
| 7 | `.button.large` | 文字サイズを`1.5rem`にする（余白は書かなくても、`em`なので一緒に大きくなる） |

| 確認する操作 | 確認したいこと |
|---|---|
| ブラウザで開く | `style`属性を消す前とほぼ同じ見た目（ヒーローの高さはウィンドウの高さに合わせて変わり、お知らせは薄い青の背景に青い文字になる） |
| 開発者ツールのComputedで大きいボタンを見る | `padding`が`12px 24px`になっている |
| `css/style.css`の`.notice`の色を`red`に変える（確認後は戻す） | 3つの段落がまとめて変わる（`style`属性だと3か所直す必要があった） |

</details>

---

## 2. セレクタ

> [example/02_selectors/index.html](example/02_selectors/index.html)

セレクタはたくさんありますが、実際のCSSの多くは、**基本**の5つ（要素・クラス・グループ化・子孫・`:hover`）だけで書けます。まず基本を使えるようにしてください。**発展は任意**です。読み飛ばして先に進んで構いません。「こういう選び方もできる」と知っておく程度で十分で、後の章のサンプルや練習問題で見かけたときに、この節に戻って確かめてください。

| | 内容 | 練習問題 |
|---|---|---|
| **基本**（必ず覚える） | 要素・クラス・グループ化・子孫・`:hover`（とIDの扱い） | [練習問題2](#練習問題2プロパティに合うセレクタを書く) |
| **発展**（任意） | 子・兄弟の結合子、複数クラス、属性セレクタ、そのほかの疑似クラス、疑似要素 | なし |

### 基本のセレクタ

| セレクタ | 記法 | 対象 |
|---|---|---|
| 要素（タイプ） | `p` | すべての`<p>` |
| クラス | `.card` | `class="card"`を持つ要素（**最もよく使う**） |
| グループ化 | `h1, h2` | カンマ区切りで複数に同じスタイル |
| 子孫 | `.box p` | `.box`の中にある`p`すべて（孫以下も）。間はスペース |
| `:hover` | `a:hover` | マウスが乗っているとき（疑似クラスの代表） |
| ID | `#title` | `id="title"`の要素（ページ内で1つ）。詳細度が強すぎるのでCSSでは避け、ページ内リンクやJavaScript用に使うことが多い |

```css
p             { line-height: 1.8; }          /* 要素 */
.card         { border: 1px solid #e1e5eb; } /* クラス */
h1, h2        { color: #3f6fd1; }            /* グループ化 */
.menu a       { text-decoration: none; }     /* 子孫：.menu の中の a だけ */
.menu a:hover { background: #3f6fd1; }       /* :hover */
```

### 発展のセレクタ（任意）

読み飛ばして構いません。練習問題もありません。

#### 結合子（コンビネータ）・複数クラス・全称

| 記法 | 名前 | 対象 |
|---|---|---|
| `.box > p` | 子 | `.box`の**直下**の`p`だけ（基本の「子孫」は孫以下も含む） |
| `h3 + p` | 隣接兄弟 | `h3`の**直後**の`p`1つ |
| `h3 ~ p` | 一般兄弟 | `h3`より後ろにある兄弟の`p`すべて |
| `.note.warning` | 複数クラス | 両方のクラスを持つ要素（間にスペースなし） |
| `*` | 全称 | すべての要素 |

#### 属性セレクタ

| 記法 | 対象 |
|---|---|
| `[required]` | `required`属性を持つ要素 |
| `input[type="email"]` | `type`が`email`の`input` |
| `a[href^="https://"]` | `href`が`https://`で**始まる** |
| `a[href$=".pdf"]` | `href`が`.pdf`で**終わる** |

#### 疑似クラス（状態・位置で選ぶ）

| 記法 | 対象 |
|---|---|
| `:focus` / `:focus-visible` | フォーカスされている / **キーボード操作で**フォーカスされている |
| `:first-child` / `:last-child` | 最初の子 / 最後の子 |
| `:nth-child(2)` / `(even)` / `(odd)` / `(3n)` | n番目 / 偶数 / 奇数 / 3の倍数番目 |
| `:not(.done)` | `.done`を**持たない** |
| `:checked` / `:disabled` | チェックされている / 無効化されている |
| `:invalid` / `:user-invalid` | 入力値が不正 / ユーザーが操作した後に不正（05_css_layoutの練習問題4で使う） |

#### 疑似要素（要素の一部・前後を作る）

| 記法 | 対象 |
|---|---|
| `::before` / `::after` | 要素の中身の前 / 後に内容を追加する。`content`プロパティが必須 |
| `::first-letter` / `::first-line` | 最初の1文字 / 1行 |
| `::placeholder` | 入力欄のプレースホルダー |

```css
.box > p        { font-weight: bold; }        /* 子 */
h3 + p          { color: #2f9e44; }           /* 隣接兄弟 */
a[href^="https://"] { color: #d1723f; }       /* 属性 */
.striped li:nth-child(even) { background: #f4f6f9; }  /* 疑似クラス */
.required::before { content: "★ "; }         /* 疑似要素 */
```

### 動作確認：セレクタごとの適用範囲

| 確認する操作 | 確認したいこと |
|---|---|
| 【基本】`02_selectors/index.html`を開き、「結合子」の2つの段落を見比べる | `.box`の中の`p`は、直下も孫も灰色になる（子孫セレクタ）。さらに【発展】直下の`p`だけが太字になる（子セレクタとの違い） |
| 【基本】メニューにマウスを乗せる | `:hover`で背景が青くなる |
| 【発展】`h3`の直後とその次の段落を見比べる | 直後の1つだけ緑色（隣接兄弟） |
| 【発展】ページをクリックしてから`Tab`キーでメニューを移動する | `:focus-visible`で橙色の枠が出る |
| 【発展】縞模様のリストを見る | 偶数番目だけ背景色が付き、最初は太字・最後は薄い色 |
| 【発展】開発者ツールで`<p class="required">`を選ぶ | Elementsに`::before`が表示される（HTMLには書いていないがCSSで追加された） |


### 練習問題2：プロパティに合うセレクタを書く

> 問題：[question/02_selectors/index.html](question/02_selectors/index.html) ｜ 解答：[question/answer/02_selectors/index.html](question/answer/02_selectors/index.html)

<details>
<summary>問題の内容を開く</summary>

上の「基本のセレクタ」（要素・クラス・グループ化・子孫・`:hover`）だけで解けます。`02_selectors/index.html`のHTMLは完成しています。`<style>`の中はプロパティと値だけが書いてあり、セレクタが`TODO`になっています。`(1)`〜`(6)`のルールに、次の「対象」だけに当たるセレクタを書きます。IDセレクタ（`#...`）と`style`属性は使わず、HTMLも変更しません（クラスの追加もしない）。

| # | 対象 | 確認したいこと |
|---|---|---|
| 1 | すべての`p` | すべての段落の行の間隔が広くなる |
| 2 | `h1`と`h2`の両方（1つのルールでまとめて） | `h1`と`h2`が青くなる（`h3`は黒のまま） |
| 3 | `class="memo"`を持つ要素 | 2つのメモが、それぞれ角の丸い枠で囲まれる |
| 4 | `class="date"`を持つ要素 | 日付の2行だけが灰色・小さい文字になる |
| 5 | `.links`の**中にある**`a`だけ（最後の段落のMDNへのリンクは含まない） | 「メモ一覧」「メモを追加」「設定」の3つが、下線の無い丸いボタンの形になる。MDNへのリンクは普通のリンクのまま |
| 6 | `.links`の中の`a`に、マウスが乗っているとき | ボタンにマウスを乗せると、青背景・白文字になる |

確認は表の右の列のとおりです。あわせて、開発者ツールで要素を選び、Stylesパネルで意図したルールだけが当たっていることを確かめます。

</details>

---

## 3. カスケード・詳細度・継承

> [example/03_cascade/index.html](example/03_cascade/index.html)

1つの要素に複数のルールが当たって値がぶつかったとき、**どれが勝つか**を決める仕組みが「カスケード（滝のように上から順に流れ落ちて決まる）」です。CSSで「書いたのに効かない」原因のほとんどはここにあります。

### 勝敗の決まり方（上から順に比べる）

| 順番 | 比べるもの | 説明 |
|---|---|---|
| 1 | `!important` | 付いている方が勝つ。**原則使わない**（後から上書きできなくなる） |
| 2 | `style`属性 | インラインスタイルはどのセレクタより強い |
| 3 | **詳細度** | セレクタの「具体的さ」。高い方が勝つ |
| 4 | 記述順 | 詳細度が同じなら**後に書いた方**が勝つ |

### 詳細度の数え方

`(IDの数, クラス・属性・疑似クラスの数, 要素・疑似要素の数)`の3桁で数え、**左の桁から**比べます。基本のセレクタだけなら、`(IDの数, クラスと:hoverの数, 要素の数)`と覚えれば十分です（属性・疑似要素は[2節の発展](#発展のセレクタ任意)のセレクタです）。

| セレクタ | 詳細度 |
|---|---|
| `p` | (0, 0, 1) |
| `.text` | (0, 1, 0) |
| `:hover`（疑似クラス） | (0, 1, 0) |
| `div p.text` | (0, 1, 2) |
| `.specificity .text` | (0, 2, 0) |
| `#special` | (1, 0, 0) |

`(0, 1, 2)`と`(0, 2, 0)`では、2桁目で決着するので`(0, 2, 0)`の勝ちです。要素セレクタをいくつ足しても、クラス1個の差は覆りません。

```css
.order { color: red; }
.order { color: blue; }          /* 同じ詳細度 → 後に書いた方（青）が勝つ */

.specificity p.text { color: green; }   /* (0,2,1) */
.specificity .text  { color: orange; }  /* (0,2,0) → 負ける */
```

### 継承

一部のプロパティは、親に指定した値が子に**引き継がれます**。

| 継承される | 継承されない |
|---|---|
| `color`・`font-*`・`line-height`・`text-align`・`letter-spacing`など文字に関するもの | `margin`・`padding`・`border`・`background`・`width`・`display`など箱に関するもの |

継承は「その要素に直接当たるルールが1つもないとき」だけ使われます。**どんなに詳細度の低いルールでも、直接当たっていれば継承より優先**されます。

### 実務でのコツ

- セレクタは**クラス1〜2個**程度に抑え、詳細度を低く揃える（上書きしやすくなる）
- IDセレクタ・`!important`・`style`属性はCSSの設計では使わない
- 「効かない」ときは開発者ツールのStylesで**取り消し線**が付いたルールを探し、何に負けているかを確認する

### 動作確認：勝ったルール・負けたルール

| 確認する操作 | 確認したいこと |
|---|---|
| `03_cascade/index.html`を開く | 各段落の色が説明どおり（青・灰・緑・紫・茶…）になっている |
| 開発者ツールで「→ 緑」の段落を選び、Stylesパネルを見る | `.specificity .text`の`color: orange`と`p`の`color: gray`に取り消し線が付いている |
| 「3. 継承」の`span`を選ぶ | Stylesに「Inherited from section.inherit」と表示され、親の`color`を継承している |
| `.inherit`の中の最初の`p`を選ぶ | 親の青ではなく灰色（直接当たる`p { color: gray }`が継承より優先） |


### 練習問題3：何色になるか予想する（詳細度クイズ）

> 問題：[question/03_specificity_quiz/index.html](question/03_specificity_quiz/index.html) ｜ 解答：[question/answer/03_specificity_quiz/index.html](question/answer/03_specificity_quiz/index.html)

<details>
<summary>問題の内容を開く</summary>

`03_specificity_quiz/index.html`の`<style>`には、9つのルールが書いてあります。HTMLの段落Q1〜Q6の文字色を、ブラウザで**開く前に**予想し、各段落の直前のコメント「予想：」の後ろに書き込みます。

| 確認する操作 | 確認したいこと |
|---|---|
| 予想を書き終えてからブラウザで開く | 予想と実際の色を比べる |
| 外れた段落を開発者ツールで選び、Stylesパネルを見る | どのルールが勝って、どのルールに取り消し線が付いているかがわかる |

使っているのは、2節の基本のセレクタ（要素・クラス・子孫・ID）だけです。

ヒント：詳細度は`(IDの数, クラスの数, 要素の数)`。左の桁から比べ、同じ詳細度のときだけ後に書いた方が勝ちます。

</details>

---

## 4. ボックスモデルとdisplay

> [example/04_box_model/index.html](example/04_box_model/index.html)

CSSでは、すべての要素が**箱（ボックス）**として扱われます。

```
┌─────────────── margin（外側の余白・背景色は付かない） ───────────────┐
│  ┌───────────── border（枠線） ─────────────────┐                     │
│  │  ┌───────── padding（内側の余白・背景色が付く） ─────────┐  │       │
│  │  │              content（中身：width / height）        │  │       │
│  │  └──────────────────────────────────────────────────┘  │       │
│  └────────────────────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────────┘
```

### box-sizing: border-box

デフォルト（`content-box`）では`width`は**中身だけ**の幅で、実際の見た目は`padding`と`border`の分だけ広がります。

```css
.box {
    width: 200px;
    padding: 20px;
    border: 4px solid #3f6fd1;
    /* 見た目の幅 = 200 + 20×2 + 4×2 = 248px */
}
```

`box-sizing: border-box`にすると`width`に`padding`と`border`が含まれ、サイズ計算が直感的になります。実務では**CSSファイルの最初に次のリセットを書く**のが定番です。

```css
*, *::before, *::after {
    box-sizing: border-box;
}
```

### 省略記法

```css
padding: 16px;                 /* 4辺すべて */
padding: 8px 24px;             /* 上下 | 左右 */
padding: 4px 24px 16px;        /* 上 | 左右 | 下 */
padding: 4px 8px 16px 32px;    /* 上 | 右 | 下 | 左（時計回り） */
margin: 0 auto;                /* 上下0・左右自動 → 幅のあるブロック要素の中央寄せ */
```

### 覚えておきたい挙動

| 挙動 | 説明 |
|---|---|
| `margin: 0 auto` | `width`（または`max-width`）を持つブロック要素を左右中央に寄せる |
| `max-width` | 「これ以上広がらない」上限。`width`より柔軟で、狭い画面では自然に縮む |
| マージンの相殺 | 上下に隣接する`margin`は**足し算されず、大きい方だけ**になる（左右では起きない） |
| `overflow` | 中身がはみ出したときの扱い。`visible`（はみ出す）・`hidden`（切る）・`auto`（必要ならスクロール） |

### display

| 値 | 振る舞い |
|---|---|
| `block` | 横幅いっぱい・前後で改行。`width`/`height`/上下`margin`が効く |
| `inline` | 文章の中に並ぶ。`width`/`height`が**効かない** |
| `inline-block` | 横に並びつつ`width`/`height`も効く（ボタン・バッジ向き） |
| `none` | 表示しない（場所も取らない） |
| `flex` / `grid` | 子要素のレイアウト方式を切り替える（05_css_layout 1・2節） |

### 動作確認：箱の大きさを測る

| 確認する操作 | 確認したいこと |
|---|---|
| `04_box_model/index.html`を開き、2つの箱を見比べる | 同じ`width: 200px`なのに、上（`content-box`）の方が広い |
| 開発者ツールで上の箱を選び、Computedのボックス図を見る | 中身200・padding20・border4が図示され、要素にマウスを乗せると248px幅でハイライトされる |
| 「マージンの相殺」の2つの箱の間隔を開発者ツールで確認 | 間隔は50pxではなく30px |
| `.center`の`margin: 0 auto`を開発者ツールで無効化する | 中央にあった箱が左に寄る |


### 練習問題4：箱の大きさを計算し、レイアウトを直す

> 問題：[question/04_box_model/index.html](question/04_box_model/index.html) ｜ 解答：[question/answer/04_box_model/index.html](question/answer/04_box_model/index.html)

<details>
<summary>問題の内容を開く</summary>

**前半：予想する（A1〜A4）**

`04_box_model/index.html`の`<style>`の「前半」のルールを読んで、HTMLのA1〜A4の直前のコメント「予想：」の後ろに答えを書き込みます。書き終えたらブラウザで開き、開発者ツールのComputedのボックス図や、要素にマウスを乗せたときのサイズ表示で答え合わせをします。

| # | 予想すること |
|---|---|
| A1 | 見た目の幅（`border`の外側から外側まで）は何pxか |
| A2 | 見た目の幅は何pxか。そのとき中身（content）の幅は何pxか |
| A3 | 2つの箱の間隔は何pxか |
| A4 | 上・右・下・左の`padding`はそれぞれ何pxか |

後半のB1を書くとA1も`border-box`に変わってしまうので、前半の答え合わせはB1を書く**前に**行います。

**後半：書く（B1〜B6）**

`<style>`の「後半」の`TODO B1`〜`TODO B6`を埋めます。HTMLは変更しません。

| # | やること | 確認したいこと |
|---|---|---|
| B1 | すべての要素（`::before`・`::after`も含む）の`box-sizing`を`border-box`にする | `.card`の幅が600pxからはみ出さない |
| B2 | `.page`を最大幅600px・左右中央寄せ・左右の内側余白16pxにする | 広い画面で、ページが中央に置かれる |
| B3 | `.badge`を、横に並んだまま幅と高さが効くようにし、28px × 28pxにする | 「3」「12」のバッジが丸になる（`span`なので、そのままでは幅が効かない） |
| B4 | `.hidden-note`を表示しない（場所も取らない） | 「（このメモは非表示です）」が消え、その場所も詰まる |
| B5 | `.log`を高さ100pxにし、はみ出した中身は必要なときだけスクロールできるようにする | ログの欄の中でスクロールできる |
| B6 | `.card`の内側の余白を「上16px・左右24px・下32px」にする（1行の省略記法で） | Computedのボックス図で、`padding`が指定どおりになっている |

</details>

---

## 5. 文字・色・背景・装飾

> [example/05_typography/index.html](example/05_typography/index.html)

```css
body {
    font-family: "Hiragino Sans", "Noto Sans JP", "Yu Gothic", sans-serif;
    font-size: 1rem;
    line-height: 1.7;
    color: #262b33;
    background: #f4f6f9;
}

.card {
    border-radius: 8px;
    box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);   /* 横のずれ 縦のずれ ぼかし 色 */
}

.tag {
    border-radius: 999px;   /* ピル型 */
}
```

### ポイント

| プロパティ | 説明 |
|---|---|
| `font-family` | 候補を左から順に並べる（フォントスタック）。最後は総称ファミリー（`sans-serif`＝ゴシック体、`serif`＝明朝体）で終える |
| `font-size` / `font-weight` | 文字サイズ（`rem`推奨）/ 太さ（`400`＝標準、`700`＝太字） |
| `line-height` | 行の高さ。**単位なしの数値**で書く（文字サイズの何倍か）。日本語の本文は1.5〜1.8が読みやすい |
| `text-align` / `text-decoration` / `letter-spacing` | 揃え位置 / 下線など / 字間 |
| `white-space: nowrap` + `overflow: hidden` + `text-overflow: ellipsis` | 1行に収まらない文字を「…」で省略する3点セット |
| `background` | 背景色・`linear-gradient()`でグラデーション |
| `border-radius` | 角丸。`999px`でピル型、`50%`で（正方形なら）正円 |
| `box-shadow` | 影。薄く・小さくするほど上品に見える |

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| `05_typography/index.html`を開く | ゴシック体と明朝体、行間の広い段落と狭い段落の読みやすさの違いがわかる |
| 「はみ出した文字の省略」を見る | 長いタイトルの末尾が「…」になっている |
| 開発者ツールで`.s-medium`の`box-shadow`の値を書き換える | 影の大きさ・濃さがその場で変わる |


### 練習問題5：記事ページを読みやすく装飾する

> 問題：[question/05_article_style/index.html](question/05_article_style/index.html) ｜ 解答：[question/answer/05_article_style/index.html](question/answer/05_article_style/index.html)

<details>
<summary>問題の内容を開く</summary>

`05_article_style/index.html`のHTMLは完成しています。`<style>`の`TODO 1`〜`TODO 12`を埋めて、次の完成イメージにします。

```
┌─────────────────────────────────────────────┐
│ ▓▓▓ 青→紫のグラデーションの帯 ▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ← .hero（白い文字・中央揃え）
│      CSSで読みやすい文章を作る               │
│      2026年10月3日（字間を広めに）            │
└─────────────────────────────────────────────┘
  ┌───────────────────────────────────────┐
  │ 白いカード（角丸・薄い影）               │  ← .article
  │ (#HTML) (#CSS)  ← ピル型のタグ           │
  │ 本文（行間が広く読みやすい）              │
  │ ┃ ポイント：…  ← 左に青い線・薄い青背景    │  ← .point
  │ 関連記事：とても長いタイトルが1行で…       │  ← .related（はみ出しを「…」で省略）
  └───────────────────────────────────────┘
```

| # | 書く場所 | やること |
|---|---|---|
| 1 | `body` | フォントスタック。`"Hiragino Sans"`・`"Noto Sans JP"`・`"Yu Gothic"`の順に並べ、最後はゴシック体の総称ファミリー |
| 2 | `body` | 文字サイズは`1rem`、行の高さは文字サイズの1.8倍（単位なしの数値で） |
| 3 | `.hero` | 背景を、左上から右下（`135deg`）へ`#3f6fd1`→`#7a5af8`のグラデーションにする |
| 4 | `.hero` | 文字は白・中央揃え |
| 5 | `.hero h1` | 文字サイズ`2rem`・太さ`700`・行の高さ`1.3`（見出しは本文より詰める） |
| 6 | `.hero time` | 字間を`0.15em`空ける |
| 7 | `.article` | 角丸12px |
| 8 | `.article` | 影（横0・縦4px・ぼかし12px・黒の10%の半透明） |
| 9 | `.tag` | 両端が丸い「ピル型」にする |
| 10 | `.point` | 左側だけに4pxの青（`#3f6fd1`）の実線、背景は薄い青（`#eef3ff`） |
| 11 | `.article a` | 下線を「点線」にする（`text-decoration`に線の種類も書ける） |
| 12 | `.related` | 1行に収まらない部分を「…」で省略する（3点セット） |

| 確認する操作 | 確認したいこと |
|---|---|
| ブラウザで開く | 完成イメージのとおりに表示される |
| ウィンドウの幅を狭くする | 「関連記事」の行は折り返さず、末尾が「…」になる |

</details>

---

## 次のステップ

続きは [05_css_layout](../05_css_layout/) です。Flexbox・Gridでのレイアウトとレスポンシブ対応を学び、オリジナルHPに見た目を付けます。

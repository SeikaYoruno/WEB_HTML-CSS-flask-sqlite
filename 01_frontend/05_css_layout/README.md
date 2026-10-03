# 05 CSSのレイアウトとレスポンシブ

> フロントエンド編 ／ 前の章：[04_css_basics](../04_css_basics/) ／ 次の章：[06_js_basics](../06_js_basics/)

この章のゴールは、**レイアウトを自力で組めるようになる**ことです。要素を1列に並べるFlexbox・格子状に並べるGrid・重ねたり固定したりするposition・画面幅に合わせて切り替えるレスポンシブ対応、そして配色をまとめて管理するCSS変数を学びます。

章の最後の制作課題では、[03_html_semantic_form](../03_html_semantic_form/)で書いたオリジナルHPのHTMLに`style.css`を書いて、見た目を付けます。

> 開発者ツールの**デバイスツールバー**（画面幅の切り替え）と、Elementsパネルの**Flex / Grid バッジ**をよく使います（[02_html_basicsの0節](../02_html_basics/#0-はじめに学習環境と開発者ツール)）。

## 目次

1. [Flexbox](#1-flexbox)
2. [Grid](#2-grid)
3. [position（重ねる・固定する）](#3-position重ねる固定する)
4. [レスポンシブ対応](#4-レスポンシブ対応)
5. [CSS変数とトランジション](#5-css変数とトランジション)
- [制作課題：オリジナルHP（ステップ2）](#制作課題オリジナルhpステップ2)
- [参考リンク](#参考リンク)

---

## フォルダ構成

```
01_frontend/05_css_layout/
├── README.md
├── example/                      サンプル（1つのサンプル＝1つのフォルダ）
│   ├── 01_flexbox/               Flexbox（主軸/交差軸・配置・折り返し・伸び縮み・実用パターン）
│   │   ├── index.html
│   │   └── img/sample.png
│   ├── 02_grid/                  Grid（fr・minmax・auto-fill/auto-fit・span・template-areas）
│   │   └── index.html
│   ├── 03_position/              position（relative/absolute/fixed/sticky・z-index）
│   │   └── index.html
│   ├── 04_responsive/            レスポンシブ（viewport・モバイルファースト・clamp）
│   │   ├── index.html
│   │   └── img/sample.png
│   └── 05_variables_transition/  CSS変数・ダークモード・トランジション
│       └── index.html
├── question/                     練習問題（4問。問題文はREADMEの各節の最後）
│   ├── 01_flexbox/               練習問題1：Flexboxでヘッダーとプロフィールカードを作る
│   │   ├── index.html
│   │   └── img/sample.png
│   ├── 02_position/              練習問題2：バッジ・閉じるボタン・固定ヘッダー・固定ボタンを作る
│   │   └── index.html
│   ├── 03_grid_dashboard/        練習問題3：Gridでレスポンシブなダッシュボードを作る
│   │   └── index.html
│   ├── 04_form_style/            練習問題4：フォームを装飾する
│   │   └── index.html
│   └── answer/                   解答（問題と同じ名前のフォルダ。中のファイル構成も問題と同じ）
│       ├── 01_flexbox/
│       ├── 02_position/
│       ├── 03_grid_dashboard/
│       └── 04_form_style/
└── challenge/                         制作課題（オリジナルHP）ステップ2：HTMLは完成済み、css/style.css にTODOを書く
    └── answer/                        完成例
```

---

## 1. Flexbox

> [example/01_flexbox/index.html](example/01_flexbox/index.html)

Flexboxは、子要素を**1方向（横 または 縦）**に並べるレイアウト方式です。`display: flex`を付けた要素が**flexコンテナ**、その**直下の子**が**flexアイテム**になります。

```
flex-direction: row のとき
          主軸（main axis）→ justify-content で配置
     ┌──────────────────────────────────────┐
  交 │ ┌────┐ ┌────┐ ┌────┐                    │
  差 │ │ 1  │ │ 2  │ │ 3  │                    │
  軸 │ └────┘ └────┘ └────┘                    │
  ↓  └──────────────────────────────────────┘
  align-items で配置
```

```css
nav {
    display: flex;
    align-items: center;   /* 交差軸（縦）方向を中央揃え */
    gap: 16px;             /* アイテム同士の間隔 */
}

nav .push-right {
    margin-left: auto;     /* この要素以降を右端に押し出す */
}
```

### コンテナに指定するプロパティ

| プロパティ | 主な値 | 説明 |
|---|---|---|
| `flex-direction` | `row`（既定）/ `column` | 主軸の向き。`column`にすると縦に並び、主軸と交差軸が入れ替わる |
| `justify-content` | `flex-start` / `center` / `flex-end` / `space-between` / `space-around` | **主軸**方向の配置 |
| `align-items` | `stretch`（既定）/ `flex-start` / `center` / `flex-end` | **交差軸**方向の配置 |
| `flex-wrap` | `nowrap`（既定）/ `wrap` | 入りきらないときに折り返すか |
| `gap` | `16px`など | アイテム同士の間隔（外側には付かない） |

### アイテムに指定するプロパティ

| プロパティ | 説明 |
|---|---|
| `flex: 1` | 余った幅を分け合う（`flex: 2`の要素は`flex: 1`の2倍もらう） |
| `flex: 1 1 180px` | 「伸びる比率 縮む比率 基本の幅」。`flex-wrap: wrap`と組み合わせると「最小180pxで、入らなければ折り返す」列が作れる |
| `flex-shrink: 0` | 画面が狭くなっても縮ませない（アイコン画像など） |
| `margin-left: auto` | その要素の左の余白を最大まで取り、右端に寄せる |

### よく使う3パターン

| パターン | 書き方 |
|---|---|
| ナビゲーション（左にロゴ、右端にログイン） | `display: flex; align-items: center; gap` ＋ 右端の要素に`margin-left: auto` |
| 上下左右中央 | `display: flex; justify-content: center; align-items: center;` |
| 画像＋文章（メディアオブジェクト） | `display: flex; gap` ＋ 画像に`flex-shrink: 0` |

### 動作確認：主軸と交差軸

| 確認する操作 | 確認したいこと |
|---|---|
| `01_flexbox/index.html`を開く | 各`justify-content`・`align-items`の値で、アイテムの位置がどう変わるかが並んで表示される |
| 開発者ツールで`.container.row`の横に出る`flex`バッジをクリック | アイテムと隙間（`gap`）が図示される |
| 「4. flex-wrap」の`.wrap`の`flex-wrap`を無効化する | アイテムが折り返さずに縮んで1行に詰め込まれる |
| 「A. ナビゲーション」の`.push-right`の`margin-left: auto`を無効化する | 「ログイン」が右端から離れ、「新規作成」のすぐ右に来る |


### 練習問題1：Flexboxでヘッダーとプロフィールカードを作る

> 問題：[question/01_flexbox/index.html](question/01_flexbox/index.html) ｜ 解答：[question/answer/01_flexbox/index.html](question/answer/01_flexbox/index.html)

<details>
<summary>問題の内容を開く</summary>

`01_flexbox/index.html`のHTMLは完成しています。`<style>`の`TODO 1`〜`TODO 8`を埋めて、次の完成イメージにします。

```
(1) ヘッダー
    ┌──────────────────────────────────────────────────┐
    │ メモ帳   一覧  新規作成                 [ログイン] │
    └──────────────────────────────────────────────────┘
      ↑左寄せ                                   ↑右端

(2) プロフィールカード（上下左右中央に配置）
              ┌─────────────────────┐
              │ (画像)  山田 太郎     │
              │         メモ 42件     │
              │ [フォロー] [メッセージ]│ ← ボタンは横並びで同じ幅
              └─────────────────────┘

(3) フッター：3つの列を横に並べ、画面が狭いと折り返す
```

| # | 書く場所 | やること |
|---|---|---|
| 1 | `.site-header` | 子要素を横並びにし、縦方向は中央揃え、間隔は20px |
| 2 | `.login` | この要素だけを右端に寄せる（ヒント：`margin-left`） |
| 3 | `.stage` | 中の`.profile`を上下左右の中央に配置する |
| 4 | `.profile-top` | 画像と名前を横並びにし、縦方向は中央揃え、間隔は12px |
| 5 | `.actions` | ボタンを横並び、間隔8px |
| 6 | `.actions button` | 2つのボタンが余った幅を均等に分け合うようにする |
| 7 | `.site-footer` | 3つの列を横に並べ、画面が狭いときは折り返す。間隔は24px |
| 8 | `.site-footer section` | 各列は「最小180px・余ったら均等に伸びる」ようにする（ヒント：`flex: 1 1 180px`） |

| 確認する操作 | 確認したいこと |
|---|---|
| ブラウザで開く | 完成イメージのとおりに表示される |
| ウィンドウの幅を狭くする | フッターの列が折り返して、縦に並ぶ |
| 開発者ツールのElementsで`flex`バッジを押す | 並び方と隙間が図示される |

</details>

---

## 2. Grid

> [example/02_grid/index.html](example/02_grid/index.html)

Gridは、子要素を**行と列の2方向**で格子状に並べるレイアウト方式です。

```css
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.page {
    display: grid;
    grid-template-columns: 200px 1fr;
    grid-template-areas:
        "header header"
        "side   main"
        "footer footer";
}
.page header { grid-area: header; }
```

### ポイント

| 書き方 | 説明 |
|---|---|
| `grid-template-columns: 100px 200px 100px` | 3列をそれぞれの幅で |
| `1fr 2fr 1fr` | `fr`＝余った幅を比率で分ける単位 |
| `repeat(4, 1fr)` | 同じ指定を繰り返す（4等分） |
| `200px 1fr` | 固定幅のサイドバー＋残り全部 |
| `minmax(160px, 1fr)` | 最小160px・最大1fr |
| `repeat(auto-fill, minmax(160px, 1fr))` | 入るだけ列を作る。**メディアクエリなしで列数が自動で変わる** |
| `auto-fill` と `auto-fit` の違い | アイテムが少ないとき、`auto-fill`は空の列を残し、`auto-fit`は空の列を潰してアイテムを広げる |
| `grid-column: span 2` / `grid-row: span 2` | 横 / 縦に2マス分使う |
| `grid-column: 1 / -1` | 1本目の線から最後の線まで（横幅いっぱい） |
| `grid-template-areas` + `grid-area` | 領域に名前を付け、文字の「絵」でレイアウトを描く |
| `place-items: center` | 中身を上下左右中央に（Gridでの中央寄せ） |

### Flexbox と Grid の使い分け

| | Flexbox | Grid |
|---|---|---|
| 方向 | 1方向（行 **または** 列） | 2方向（行 **と** 列） |
| 得意なもの | ナビ・ボタンの並び・カードの中身 | カード一覧・ページ全体の骨組み |
| 考え方 | 中身の大きさに合わせて並べる | 先に枠（格子）を決めて、そこに配置する |

実際のページでは**両方を組み合わせる**のが普通です（ページの骨組みはGrid、ヘッダーの中はFlexbox）。

### 動作確認：列の自動調整

| 確認する操作 | 確認したいこと |
|---|---|
| `02_grid/index.html`を開き、ウィンドウ幅を変える | `auto-fill`・`auto-fit`の行で列数が自動で増減する |
| 広い画面で`auto-fill`と`auto-fit`を見比べる | `auto-fill`はアイテム2つが左に寄って空きが残り、`auto-fit`は2つが横幅いっぱいに広がる |
| 開発者ツールで`.page`の`grid`バッジをクリック | 領域名（header/side/main/footer）が図示される |
| ウィンドウ幅を600px以下にする | `.page`が縦1列（header→main→aside→footer）に組み替わる |

---

## 3. position（重ねる・固定する）

> [example/03_position/index.html](example/03_position/index.html)

`position`は、要素を通常の並び（文書の流れ）から**ずらす・重ねる・固定する**ためのプロパティです。`top`/`right`/`bottom`/`left`で位置を指定します。

```css
.card {
    position: relative;     /* 子の absolute の基準になる */
}

.badge {
    position: absolute;     /* .card の右上に重ねる */
    top: -10px;
    right: -10px;
}

.site-header {
    position: sticky;       /* スクロールしても上端に貼り付く */
    top: 0;
    z-index: 10;
}
```

### ポイント

| 値 | 基準 | 元の場所 | よくある用途 |
|---|---|---|---|
| `static`（既定） | — | — | 通常の並び。`top`などは効かない |
| `relative` | 元の位置 | 空いたまま残る | 少しずらす / **子の`absolute`の基準**にする |
| `absolute` | `position`が`static`以外の**一番近い祖先** | 詰められる（流れから外れる） | バッジ・閉じるボタンを重ねる |
| `fixed` | 画面（ビューポート） | 詰められる | 右下の固定ボタン・固定ヘッダー |
| `sticky` | スクロールする親 | 残る | スクロールすると貼り付くヘッダー・表の見出し |

`z-index`は重なり順です。大きいほど手前に表示されます（`position`が`static`以外の要素で効く）。

> 「親に`position: relative`、子に`position: absolute`」はセットで覚えましょう。親に`relative`が無いと、子はページ全体を基準にして思わぬ場所に飛んでいきます。

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| `03_position/index.html`を開いて下にスクロールする | 青いヘッダーが上端に貼り付き、右下の緑のボタンは同じ位置に残り続ける |
| 「absolute」の親`.parent`の`position: relative`を開発者ツールで無効化する | 橙色の箱が、親の右下ではなくページ（画面）の右下を基準に移動する |
| 「バッジ」のカードを見る | 「NEW」がカードの右上の角からはみ出すように重なっている |


### 練習問題2：バッジ・閉じるボタン・固定ヘッダー・固定ボタンを作る

> 問題：[question/02_position/index.html](question/02_position/index.html) ｜ 解答：[question/answer/02_position/index.html](question/answer/02_position/index.html)

<details>
<summary>問題の内容を開く</summary>

`02_position/index.html`のHTMLは完成しています。`<style>`の`TODO 1`〜`TODO 6`を埋めて、次の完成イメージにします。

```
┌──────────────────────────────────────────┐
│ メモ帳                                    │ ← スクロールしても上端に貼り付く
└──────────────────────────────────────────┘
  ┌──────────────────────────────────┐
  │ お知らせ：新機能を追加しました    [×] │ ← × はお知らせの右上の角に重ねる
  └──────────────────────────────────┘
  ┌────────────┐ ┌────────────┐
  │ 買い物リスト │(NEW)          │    ← NEW はカードの右上の角から少しはみ出す
  │            │ │            │
  └────────────┘ └────────────┘
                                       ┌───┐
                                       │ ↑ │ ← 画面の右下に固定。スクロールしても動かない
                                       └───┘
```

| # | 書く場所 | やること |
|---|---|---|
| 1 | `.site-header` | スクロールしても画面の上端（0px）に貼り付くようにし、手前に表示する（`z-index: 10`） |
| 2 | `.notice` | 子の`.close`の基準にする（これ自体は動かさない） |
| 3 | `.close` | `.notice`の右上に重ねる（上から8px・右から8px） |
| 4 | `.card` | 子の`.badge`の基準にする |
| 5 | `.badge` | カードの右上の角から、上に10px・右に10pxはみ出すように重ねる（ヒント：マイナスの値） |
| 6 | `.to-top` | 画面（ビューポート）の右下に固定する（下から24px・右から24px） |

ヘッダーに`z-index`が無いと、`position: relative`のカードがスクロールしたときにヘッダーの上に重なってしまいます。

| 確認する操作 | 確認したいこと |
|---|---|
| 下にスクロールする | ヘッダーが上端に貼り付き、カードがその下にもぐる。右下の「↑」は同じ位置に残る |
| 開発者ツールで`.card`の`position: relative`を無効にする | 「NEW」がカードではなく、ページ全体を基準にした場所に飛んでいく |
| 「↑」を押す | ページの先頭に戻る |

</details>

---

## 4. レスポンシブ対応

> [example/04_responsive/index.html](example/04_responsive/index.html)

画面の幅（スマホ・タブレット・PC）に応じてレイアウトを切り替えることを**レスポンシブ対応**と呼びます。

### `<meta name="viewport">`

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

このタグが無いと、スマホのブラウザは「PC用のページだろう」と判断して、約980px幅で描画したものを縮小表示します。文字が極小になり、メディアクエリも意図通りに効きません。**すべてのページに必ず書きます**。

### メディアクエリとモバイルファースト

```css
/* まずスマホ用（1列）を書く */
.box-grid {
    display: grid;
    grid-template-columns: 1fr;
}

/* 600px「以上」になったら2列 */
@media (min-width: 600px) {
    .box-grid { grid-template-columns: repeat(2, 1fr); }
}

/* 900px「以上」になったら3列 */
@media (min-width: 900px) {
    .box-grid { grid-template-columns: repeat(3, 1fr); }
}
```

| 書き方 | 考え方 |
|---|---|
| **モバイルファースト**（`min-width`） | 小さい画面用を基本に書き、広い画面用を**足していく**。シンプルなレイアウトに要素を足す方が書きやすく、現在の主流 |
| デスクトップファースト（`max-width`） | PC用を基本に書き、狭い画面用で**打ち消していく** |

ブレークポイント（切り替わる幅）は「この幅でレイアウトが崩れ始めたら」で決めます。目安として600px前後（スマホ/タブレット）・900px前後（タブレット/PC）がよく使われます。

### メディアクエリ以外の道具

| 書き方 | 説明 |
|---|---|
| `max-width: 960px; margin: 0 auto; padding: 0 16px;` | 広い画面では中央に寄せ、狭い画面では左右に余白を残す「コンテナ」 |
| `img { max-width: 100%; height: auto; }` | 画像を親の幅からはみ出させない定番の指定 |
| `font-size: clamp(1.5rem, 4vw + 1rem, 2.75rem)` | 最小・推奨・最大を指定し、画面幅に応じてなめらかに変化させる |
| `repeat(auto-fill, minmax(200px, 1fr))` | 2節の自動列数。メディアクエリなしでレスポンシブになる |

### 動作確認：ブレークポイント

| 確認する操作 | 確認したいこと |
|---|---|
| `04_responsive/index.html`を開き、デバイスツールバー（`Cmd + Shift + M`）で幅を375px→700px→1000pxと変える | 黄色の表示が「スマホ幅：1列」→「タブレット幅：2列」→「PC幅：3列」に変わり、箱の列数も変わる |
| 同じ操作でナビゲーションを見る | スマホ幅では縦並び、600px以上で横並びになる |
| 見出しの大きさを見ながら幅を変える | 段階的ではなく、なめらかに大きさが変わる（`clamp`） |
| 一番下の画像を見る | `width="1200"`なのに画面からはみ出さない |
| `<meta name="viewport">`をコメントアウトし、デバイスツールバーのスマホ幅で確認（確認後は必ず戻す） | ページ全体が縮小表示され、3列のまま小さく表示される |


### 練習問題3：Gridでレスポンシブなダッシュボードを作る

> 問題：[question/03_grid_dashboard/index.html](question/03_grid_dashboard/index.html) ｜ 解答：[question/answer/03_grid_dashboard/index.html](question/answer/03_grid_dashboard/index.html)

<details>
<summary>問題の内容を開く</summary>

2節（Grid）と4節（レスポンシブ）を組み合わせる問題です。`03_grid_dashboard/index.html`のHTMLは完成しています。「モバイルファースト」で、まずスマホ用を書き、`@media (min-width)`で広い画面用を追加します。

```
スマホ（〜767px）         PC（768px〜）
┌──────────┐              ┌──────────────────────────────┐
│  header  │              │            header            │
├──────────┤              ├────────┬─────────────────────┤
│  stats   │              │        │        stats        │
├──────────┤              │  side  ├─────────────────────┤
│  memos   │              │        │        memos        │
├──────────┤              ├────────┴─────────────────────┤
│  side    │              │            footer            │
├──────────┤              └──────────────────────────────┘
│  footer  │                 side の幅は 220px 固定
└──────────┘
```

| # | 書く場所 | やること |
|---|---|---|
| 1 | `.layout` | `display: grid`にし、`grid-template-areas`でスマホ用の5段を定義する |
| 2 | `.layout`の下 | 各要素に`grid-area`で名前を付ける（`header` / `stats` / `memos` / `side` / `footer`） |
| 3 | `.stats` | `display: grid`で2列（`repeat(2, 1fr)`）、間隔12px |
| 4 | `.memo-list` | `auto-fill`＋`minmax(180px, 1fr)`で自動的に列数が変わるグリッドにする。間隔12px |
| 5 | 「PC用（768px以上）」 | `@media (min-width: 768px)`を書き、`.layout`の列を「`220px 1fr`」にして`grid-template-areas`をPC用に変える。`.stats`は4列にする |

| 確認する操作 | 確認したいこと |
|---|---|
| デバイスツールバーで幅375pxにする | 5つの領域が縦に1列で並び、数値カードは2列 |
| 幅を1000pxにする | `side`が左に220pxで並び、数値カードは4列 |
| 幅を少しずつ変える | メモのカードの列数が、メディアクエリ無しで自動的に変わる |

</details>

---

## 5. CSS変数とトランジション

> [example/05_variables_transition/index.html](example/05_variables_transition/index.html)

### CSS変数（カスタムプロパティ）

```css
:root {
    --color-primary: #3f6fd1;
    --radius: 8px;
}

.button {
    background: var(--color-primary);
    border-radius: var(--radius);
}
```

| 書き方 | 説明 |
|---|---|
| `--名前: 値;` | 変数の定義。`:root`（＝`html`要素）に書くとページ全体で使える |
| `var(--名前)` | 変数の値を使う。`var(--名前, 代わりの値)`で未定義のときの値も指定できる |
| 要素ごとの上書き | `.card.accent { --color-primary: #d1723f; }`のように書くと、その要素の中だけ値が変わる |

色をあちこちに直接書くと、配色を変えるときに全部探して直す必要があります。変数にまとめておけば**1か所の変更で済み**、ダークモードも変数の差し替えだけで作れます。

```css
@media (prefers-color-scheme: dark) {
    :root {
        --color-bg: #16181d;
        --color-text: #e6e8ec;
    }
}
```

### トランジション

```css
.card {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgb(0 0 0 / 0.12);
}
```

| プロパティ | 説明 |
|---|---|
| `transition: 対象 時間 イージング` | 値が変わるときにアニメーションさせる。`:hover`と組み合わせることが多い |
| `transform: translateY(-4px)` / `scale(0.96)` | 位置をずらす / 拡大縮小する。周りのレイアウトに影響しないので動かしても軽い |
| `@media (prefers-reduced-motion: reduce)` | OSで「視差効果を減らす」を設定した人には動きを止める（アクセシビリティ） |

### 動作確認

| 確認する操作 | 確認したいこと |
|---|---|
| `05_variables_transition/index.html`を開き、カードにマウスを乗せる | カードがなめらかに浮き上がる |
| 開発者ツールで`:root`の`--color-primary`を`green`に書き換える | 全部のボタンの色が一度に変わる（ただし`.accent`の中は上書きしているので変わらない） |
| OSの外観をダークモードにする（またはDevToolsのRendering → Emulate CSS media feature `prefers-color-scheme: dark`） | 背景・文字・カードの色が暗い配色に切り替わる |


### 練習問題4：フォームを装飾する

> 問題：[question/04_form_style/index.html](question/04_form_style/index.html) ｜ 解答：[question/answer/04_form_style/index.html](question/answer/04_form_style/index.html)

<details>
<summary>問題の内容を開く</summary>

[03_html_semantic_formの練習問題2](../03_html_semantic_form/#練習問題2ユーザー登録フォームのhtmlを書く)で作ったユーザー登録フォームのHTMLが、そのまま入っています。`<style>`の`TODO 1`〜`TODO 5`を埋めて、`02_backend/15_login`の「ユーザー登録」画面として使える見た目にします。白いカードの中に、横幅いっぱいの入力欄がラベルの下に並び、登録ボタンは横幅いっぱいの青いボタンにします。

| # | やること |
|---|---|
| 1 | `.field`の中の`label`をブロック要素にし、太字・下に4pxの余白 |
| 2 | `type`が`text` / `email` / `password`の`input`を、横幅いっぱい・`padding` 8px・枠線`1px solid var(--color-border)`・角丸6pxにする（属性セレクタを使う） |
| 3 | 入力欄にフォーカスしたとき（`:focus`）、枠線の色を`var(--color-primary)`にし、`outline`を消して`box-shadow: 0 0 0 3px rgb(63 111 209 / 0.25)`を付ける |
| 4 | ユーザーが操作した後に不正な値だったとき（`:user-invalid`）、枠線の色を`var(--color-error)`にする（`:invalid`だとページを開いた瞬間から赤くなってしまう。違いを試してみる） |
| 5 | 登録ボタンを横幅いっぱい・背景`var(--color-primary)`・白文字・枠線なし・`padding` 10px・角丸6px・`cursor: pointer`にし、`:hover`で`opacity: 0.85`にする |

| 確認する操作 | 確認したいこと |
|---|---|
| `Tab`キーで入力欄を移動する | フォーカス中の入力欄の枠が青くなり、外側に薄い青の輪が出る |
| パスワードを3文字で入力して、欄の外をクリックする | 枠が赤くなる |
| ページを開いた直後に見る | まだ何も入力していないので、どの枠も赤くない |
| 開発者ツールで`:root`の`--color-primary`を`green`に変える | フォーカスの枠とボタンの色が一度に変わる |

</details>

---

## 制作課題：オリジナルHP（ステップ2）

> [challenge/](challenge/) — 雛形 ｜ [challenge/answer/](challenge/answer/) — 完成例 ｜ 自分のHP：[00_my_homepage/](../00_my_homepage/)

ステップ1で書いたHPのHTMLに、`css/style.css`を作って見た目を付けます。**HTMLはなるべく変えずにCSSで見た目を作る**のが基本です（クラスを追加するのは構いません）。

制作課題は、毎回次の2段階で進めます。

1. **`challenge/`で練習する**：架空の人物「山田 太郎」のサイトを題材に、ファイルの中のTODOコメントに沿って書きます。書けたら`challenge/answer/`の完成例と見比べます。
2. **自分のHPに反映する**：同じことを、[00_my_homepage/](../00_my_homepage/)の自分のサイトに行います。こちらは文章・配色・レイアウトを自分で考えて作ります。下の「必須要件」は、自分のHPで満たすべき要件です。

### challenge/ の内容

| ファイル | 内容 |
|---|---|
| `*.html` | 03_html_semantic_formの完成例に、`<link rel="stylesheet" href="css/style.css">`を足したもの（完成済み） |
| `css/style.css` | TODOコメントだけが、上から節の順に並んでいる。ここに書き込んでいく |

### 必須要件

| 要件 | 使う節 |
|---|---|
| 全ページで同じ`css/style.css`を`<link>`で読み込む（`<style>`タグや`style`属性は使わない） | 04_css_basics 1 |
| `:root`にCSS変数で配色を定義し、色は変数を通して使う（メインカラー・背景・文字・枠線の4色以上） | 5 |
| `*, *::before, *::after { box-sizing: border-box; }`のリセットを書く | 04_css_basics 4 |
| ヘッダーのサイト名とナビゲーションを**Flexbox**で横に並べる | 1 |
| カードなどの一覧を**Grid**で並べる（制作実績・スキルなど） | 2 |
| **モバイルファースト**で書き、`@media (min-width: ...)`で広い画面のレイアウトを足す。幅375px・768px・1100pxのどれでも横スクロールが出ない | 4 |
| リンクとボタンに`:hover`と`:focus-visible`のスタイルを付ける | 04_css_basics 2 |
| フォームの入力欄を横幅いっぱいにし、`:focus`で枠の色を変える | 04_css_basics 2・4 |
| 開発者ツールで、意図しないルールが**取り消し線**で負けていないか確認する | 04_css_basics 3 |

### 進め方のヒント

1. 配色を3〜5色決めて、`:root`に変数として書く（配色に迷ったら、メインカラー1色＋白・グレー系で十分）
2. 全ページ共通の部分（`body`・ヘッダー・フッター・`.container`）から書き、1ページずつ仕上げる
3. デバイスツールバーで、こまめにスマホ幅を確認する。崩れたら、その幅で「どの要素がはみ出しているか」をElementsで探す
4. [challenge/answer/css/style.css](challenge/answer/css/style.css)は、どの部分にどの節の内容を使っているかの参考にする

### 動作確認：challenge/

| 確認する操作 | 確認したいこと |
|---|---|
| `challenge/index.html`を開く | `challenge/answer/index.html`とほぼ同じ見た目になっている（色や余白は違っていてよい） |
| デバイスツールバーで375px・768px・1100pxに切り替える | どの幅でも横スクロールが出ない。768px以上でホームのプロフィール欄が2列になる |
| 4ページを行き来する | 1つの`style.css`で、全ページの見た目がそろっている |

---

## 参考リンク

| リンク | 内容 |
|---|---|
| [MDN：CSS リファレンス](https://developer.mozilla.org/ja/docs/Web/CSS/Reference) | すべてのCSSプロパティの説明 |
| [MDN：CSS レイアウト入門](https://developer.mozilla.org/ja/docs/Learn/CSS/CSS_layout) | Flexbox・Grid・position・レスポンシブをさらに詳しく |
| [Flexbox Froggy](https://flexboxfroggy.com/#ja) / [Grid Garden](https://cssgridgarden.com/#ja) | カエルや畑を動かしながら Flexbox / Grid を練習できるゲーム |
| [Can I use](https://caniuse.com/) | そのCSS機能がどのブラウザで使えるか |

## 次のステップ

続きは [06_js_basics](../06_js_basics/) です。ページに動きを付けるJavaScriptの基本文法を学びます。

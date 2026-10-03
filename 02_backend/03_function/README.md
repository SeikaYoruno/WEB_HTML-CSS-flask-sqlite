# 03 関数とデコレータ

> バックエンド編 ／ 前の章：[02_memo_app_frontend](../02_memo_app_frontend/) ／ 次の章：[04_flask_basic](../04_flask_basic/)

Pythonの関数の基本（定義・呼び出し・引数・戻り値・スコープ）を学んだうえで、Flaskの`@app.route()`の仕組みを理解するために、Pythonの**デコレータ**を段階的に学びます。Flaskはまだ使いません。

## この章の進め方

各節は、次の順に進めます。

1. **読む**：節の説明を読む
2. **サンプルを動かす**：節の最初にある「サンプル」を実行し、「動作確認」の表のとおりに表示されるか確かめる。コメントを外したり値を変えたりして、動きを試す
3. **練習問題を解く**：節の最後に「練習問題」があれば、`question/`のファイルを開く。問題文はファイルの先頭に書いてあるので、その下にコードを書いて実行する。できたら`question/answer/`の解答と見比べる

| 節 | サンプル（`example/`） | 練習問題（`question/`） |
|---|---|---|
| [1. 組み込み関数](#1-組み込み関数built-in-functions) | ex01_builtin_functions | — |
| [2. 関数の定義と呼び出し](#2-関数の定義と呼び出し) | ex02_call | — |
| [3. 引数の種類](#3-引数の種類) | ex03_default_args・ex04_variable_args | 1 デフォルト引数・2 位置引数とキーワード引数・3 `*args`・4 `**kwargs` |
| [4. 戻り値の詳細](#4-戻り値の詳細) | ex05_return_values | — |
| [5. Noneとは](#5-noneとは) | ex06_none | 5 戻り値（4・5節のまとめ） |
| [6. 変数のスコープ](#6-変数のスコープ) | ex07_local_scope・ex08_global_read・ex09_global_write | 6 スコープを予想する |
| [7. 関数はオブジェクト](#7-関数はオブジェクト) | ex10_pass_function・ex11_function_object | 7 関数を渡す |
| [8. 関数内関数（クロージャ）](#8-関数内関数クロージャ) | ex12_closure | — |
| [9. デコレータ構文（@）](#9-デコレータ構文) | ex13_decorator | 8 デコレータを作る |
| [10. 可変長引数付きデコレータ](#10-可変長引数付きデコレータ) | ex14_decorator_args | 9 戻り値を使うデコレータ |

1〜6節は、関数の基本です。7〜10節は、`@app.route()`のようなデコレータの仕組みを、1段ずつ積み上げて理解します。

---

## フォルダ構成

```
02_backend/03_function/
├── README.md
├── example/                         サンプル（節の順に番号が付いている）
│   ├── ex01_builtin_functions.py    1. 組み込み関数
│   ├── ex02_call.py                 2. 位置引数・キーワード引数での呼び出し
│   ├── ex03_default_args.py         3. デフォルト引数
│   ├── ex04_variable_args.py        3. 可変長引数（*args・**kwargs）
│   ├── ex05_return_values.py        4. 複数の戻り値・早期return・Noneが返る場合
│   ├── ex06_none.py                 5. None と空のリストの違い
│   ├── ex07_local_scope.py          6. ローカル変数
│   ├── ex08_global_read.py          6. グローバル変数を読む
│   ├── ex09_global_write.py         6. グローバル変数を書き換える（global）
│   ├── ex10_pass_function.py        7. 関数を引数に渡す
│   ├── ex11_function_object.py      7. 関数は値として扱える
│   ├── ex12_closure.py              8. 関数を返す関数（クロージャ）
│   ├── ex13_decorator.py            9. デコレータ（@）
│   └── ex14_decorator_args.py       10. 引数のある関数に使えるデコレータ
└── question/                        練習問題（問題文は各ファイルの先頭）
    ├── question01_default_args.py 〜 question09_decorator_args.py
    └── answer/                      解答（answer01_default_args.py 〜 answer09_decorator_args.py）
```

サンプルは、先頭のコメントに「どの節の内容か」「ねらい」「実行のしかた」を書いています。練習問題は、先頭のコメントに問題文と期待する出力を書いています。コマンドは、リポジトリの一番上のフォルダで、仮想環境を有効にしてから実行します（[00_docs/setup/backend.md](../../00_docs/setup/backend.md)）。

---

## 1. 組み込み関数（built-in functions）

> サンプル：[example/ex01_builtin_functions.py](example/ex01_builtin_functions.py) — importしなくても使える関数と、「画面に出す関数」「値を返す関数」の違い

Pythonが最初から用意している関数で、importせずにそのまま使えます。

| 関数名 | 概要 | 使用例 |
|---|---|---|
| `print()` | 画面に出力する | `print("Hello")` |
| `len()` | 要素数を返す | `len("abc")` → 3 |
| `type()` | データ型を返す | `type(123)` → `<class 'int'>` |
| `int()` | 整数に変換 | `int("10")` → 10 |
| `str()` | 文字列に変換 | `str(100)` → `"100"` |
| `list()` | リストに変換 | `list("abc")` → `['a','b','c']` |
| `range()` | 整数の範囲を生成（for文でよく使用） | `range(3)` → 0,1,2 |
| `sum()` | 合計を計算 | `sum([1, 2, 3])` → 6 |
| `max()` | 最大値を返す | `max([1, 5, 3])` → 5 |
| `min()` | 最小値を返す | `min([1, 5, 3])` → 1 |
| `abs()` | 絶対値を返す | `abs(-5)` → 5 |
| `input()` | 入力を受け取る（文字列） | `input("名前は？")` |

全部で70個以上あります（一覧は`import builtins`→`print(dir(builtins))`で見られます）。関数の使い方がわからないときは、`help(print)`のように`help()`で説明を表示できます。

### 動作確認

```bash
python 02_backend/03_function/example/ex01_builtin_functions.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `3`・`<class 'int'>`・`6`の3行が表示される |
| ファイルの中の`len('abc')`の行（`print`で包んでいない行）を見る | この行の結果は画面に表示されていない。`len()`は値を**返す**だけで、表示するには`print()`が必要 |

---

## 2. 関数の定義と呼び出し

> サンプル：[example/ex02_call.py](example/ex02_call.py) — 同じ関数を、位置引数・キーワード引数の3通りで呼び出す

```python
def func_name(arg1, arg2, ...):
    # process
    return return_value
```

| キーワード | 意味 |
|---|---|
| `def` | define（定義する） |
| `func_name` | スネークケースで記載する |
| `(arg1, arg2, ...)` | 引数（省略可） |
| `return return_value` | 戻り値（省略可。省略時は`None`が返される） |

### 命名のスタイル

| 用途 | 命名スタイル | 例 |
|---|---|---|
| 変数名 | スネークケース（小文字＋アンダースコア） | `user_name` |
| 関数名 | スネークケース | `calc_sum()` |
| クラス名 | キャメルケース（単語の先頭が大文字） | `MyClass` |
| 定数 | アッパーケース＋`_` | `MAX_SPEED`, `PI` |
| 特殊メソッド | ダブルアンダースコア（ダンダー） | `__init__` |

### 関数の呼び出し方

```python
def add(a, b):
    print(a + b)

add(1, 2)
add(a=1, b=2)  # キーワード指定も可能
add(b=2, a=1)  # キーワード指定は順不同でも可
```

### 動作確認

```bash
python 02_backend/03_function/example/ex02_call.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `3`が**3行**表示される（3通りの呼び出し方が同じ結果になる） |
| コメントアウトされている`add(b=2, 1)`を有効にして実行する（確認後は戻す） | 実行前に`SyntaxError`になる（キーワード引数の後に位置引数は置けない） |

---

## 3. 引数の種類

> サンプル：[example/ex03_default_args.py](example/ex03_default_args.py) — 省略した引数が、デフォルト値で補われる<br>
> サンプル：[example/ex04_variable_args.py](example/ex04_variable_args.py) — 数が決まっていない引数を、`*args`はタプル、`**kwargs`は辞書で受け取る

| 種類 | 書き方 | 説明 | 例 |
|---|---|---|---|
| 位置引数 | `def func(a, b)` | 順番で渡す | `func(1, 2)` |
| デフォルト引数 | `def func(a=10)` | 省略可能。右側から指定する | `func()` → a=10 |
| キーワード引数 | `def func(a, b)` | 名前を指定して渡す（順番不問） | `func(b=2, a=1)` |
| 可変長位置引数 | `def func(*args)` | 複数の位置引数をタプルで受け取る | `func(1, 2, 3)` |
| 可変長キーワード引数 | `def func(**kwargs)` | 複数のキーワード引数を辞書で受け取る | `func(x=1, y=2)` |
| キーワード専用引数 | `def func(*, a)` | `*`より後はキーワード指定のみ | `func(a=1)` |
| 位置専用引数 | `def func(a, /)` | `/`より前は位置引数のみ | `func(1)` |

```python
# デフォルト引数
def add1(a=1, b=2):
    print(a + b)

add1()      # 3（両方デフォルト値）
add1(3, 2)  # 5

# デフォルト引数は右側から準備する（下記はSyntaxError）
# def add(a=1, b):
#     print(a + b)
```

```python
# 可変長位置引数（*args） — 複数の位置引数をタプルとして受け取る
def show_args(*args):
    print(args)

show_args(1, 2, 3)  # (1, 2, 3)

# 可変長キーワード引数（**kwargs） — 複数のキーワード引数を辞書として受け取る
def show_kwargs(**kwargs):
    print(kwargs)

show_kwargs(x=1, y=2)  # {'x': 1, 'y': 2}
```

### 動作確認

```bash
python 02_backend/03_function/example/ex03_default_args.py
python 02_backend/03_function/example/ex04_variable_args.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| `ex03`を実行する | `3`・`5`・`5`・`5`の4行が表示される（省略した引数だけが、デフォルト値で補われる） |
| `ex04`を実行する | `show_args(1, 2, 3)`で`(1, 2, 3)`と`<class 'tuple'>`、引数なしで空のタプル`()`が表示される |
| `ex04`の後半の出力を見る | `show_kwargs(x=1, y=2)`で`{'x': 1, 'y': 2}`と`<class 'dict'>`、`show_both(1, 2, x=3, y=4)`で`args: (1, 2)`と`kwargs: {'x': 3, 'y': 4}`のように、位置引数とキーワード引数が別々に受け取られている |

### 練習問題1：デフォルト引数

> 問題：[question/question01_default_args.py](question/question01_default_args.py) ｜ 解答：[question/answer/answer01_default_args.py](question/answer/answer01_default_args.py)
>
> ねらい：引数を省略したときに使われる値（デフォルト値）を決められるようになる

### 練習問題2：位置引数とキーワード引数

> 問題：[question/question02_positional_keyword.py](question/question02_positional_keyword.py) ｜ 解答：[question/answer/answer02_positional_keyword.py](question/answer/answer02_positional_keyword.py)
>
> ねらい：位置引数とキーワード引数を混ぜるときの「並べ方のルール」がわかるようになる

### 練習問題3：可変長位置引数（`*args`）

> 問題：[question/question03_args.py](question/question03_args.py) ｜ 解答：[question/answer/answer03_args.py](question/answer/answer03_args.py)
>
> ねらい：いくつ渡されるかわからない値を、`*args`でまとめて受け取れるようになる

### 練習問題4：可変長キーワード引数（`**kwargs`）

> 問題：[question/question04_kwargs.py](question/question04_kwargs.py) ｜ 解答：[question/answer/answer04_kwargs.py](question/answer/answer04_kwargs.py)
>
> ねらい：名前付きの値をいくつでも、`**kwargs`で辞書として受け取れるようになる

---

## 4. 戻り値の詳細

> サンプル：[example/ex05_return_values.py](example/ex05_return_values.py) — 複数の値を返す・途中で`return`して抜ける・`return`が無いと`None`が返る

### 複数の値を返す

```python
def min_max(numbers):
    return min(numbers), max(numbers)  # タプルとして返される

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)  # 出力: 1 5
```

### 早期return

条件を満たさない場合に関数を早く抜けます。

```python
def divide(a, b):
    if b == 0:
        return None  # 早期returnでゼロ除算を防ぐ
    return a / b
```

### Noneが返る条件

`return`を書かない、または`return`だけ書いた場合は`None`が返ります。

```python
def greet(name):
    print(f"Hello, {name}")  # returnなし

result = greet("Alice")
print(result)  # 出力: None
```

### 動作確認

```bash
python 02_backend/03_function/example/ex05_return_values.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `1 5`（複数の値を2つの変数で受け取った）、`None`（0で割ろうとしたので早期return）、`5.0`、`Hello, Alice`に続けて`None`（`greet`には`return`が無い）の順で表示される |

---

## 5. Noneとは

> サンプル：[example/ex06_none.py](example/ex06_none.py) — 「値が無い」`None`と、「中身が空のリスト」`[]`の違い

`None`はPythonの特殊な値で「何もない」「値が存在しない」ことを表します。

```python
x = None
print(x)        # 出力: None
print(type(x))  # 出力: <class 'NoneType'>
```

| 項目 | 内容 |
|---|---|
| 型 | `NoneType` |
| 真偽値 | `False`として扱われる |
| 比較 | `== None`より`is None`を使うのが慣例 |

```python
result = None

if result is None:
    print("値がありません")

if result is not None:
    print("値があります")
```

### Noneと空リスト`[]`の違い

どちらも「何もない」ように見えますが意味が異なります。

| | `None` | `[]` |
|---|---|---|
| 意味 | 値そのものが存在しない | リストは存在するが中身が空 |
| 型 | `NoneType` | `list` |
| 要素追加 | できない（エラー） | `append()`で追加できる |
| よく使う場面 | 関数が値を返せなかった時 | これから要素を追加する予定のリスト |

### 動作確認

```bash
python 02_backend/03_function/example/ex06_none.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `True`・`<class 'NoneType'>`・`False`・`0`の順に表示される（空のリストは`None`ではない） |
| `result.append('メモ')`の行のコメントを外して実行する（確認後は戻す） | `AttributeError`になる（`None`には要素を追加できない） |

### 練習問題5：戻り値（複数の値・早期return）

> 問題：[question/question05_return.py](question/question05_return.py) ｜ 解答：[question/answer/answer05_return.py](question/answer/answer05_return.py)
>
> ねらい：関数から複数の値を返し、条件に合わないときは途中で`None`を返せるようになる（4・5節のまとめ）

---

## 6. 変数のスコープ

> サンプル：[example/ex07_local_scope.py](example/ex07_local_scope.py) — 関数の中で作った変数は、外からは使えない<br>
> サンプル：[example/ex08_global_read.py](example/ex08_global_read.py) — 関数の外の変数を、中から「読む」ことはできる<br>
> サンプル：[example/ex09_global_write.py](example/ex09_global_write.py) — 外の変数を「書き換える」には`global`が必要

### ローカル変数（local variable）

```python
def greet():
    name = "Alice"  # ローカル変数: 関数の中でのみ有効
    print("Hello,", name)

greet()
# print(name)  # エラー！関数の外からはアクセスできない
```

### グローバル変数（global variable）

```python
message = "こんにちは"  # グローバル変数: プログラム全体で有効

def greet():
    print(message)  # 関数の中から参照できる

greet()  # 出力: こんにちは
```

関数の中でグローバル変数を**変更**するには`global`宣言が必要です。

```python
count = 0

def increment():
    global count   # globalをつけないとUnboundLocalError
    count += 1

increment()
print(count)  # 出力: 1
```

### グローバル変数を避けるべき理由

| 理由 | 説明 |
|---|---|
| 予測しにくい | どこからでも変更できるため、バグの原因になりやすい |
| テストがしづらい | 特定の値に依存した関数は再利用性が下がる |
| 可読性が低くなる | 外部の変数が関数に影響することで、理解しにくいコードになる |

### 動作確認

```bash
python 02_backend/03_function/example/ex07_local_scope.py
python 02_backend/03_function/example/ex08_global_read.py
python 02_backend/03_function/example/ex09_global_write.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| `ex07`を実行する。次に`print(name)`のコメントを外して実行する（確認後は戻す） | `Hello, Alice`と表示される。コメントを外すと`NameError`になる |
| `ex08`を実行する | `こんにちは`と表示される（読むだけなら`global`は不要） |
| `ex09`を実行する。次に`increment_wrong()`のコメントを外して実行する（確認後は戻す） | `0`・`1`と表示される。コメントを外すと`UnboundLocalError`になる（`global`が無いと、代入した時点でローカル変数として扱われる） |

「読むのはOK、書き換えるには`global`が必要」という違いがわかれば十分です。

### 練習問題6：スコープを予想する

> 問題：[question/question06_scope.py](question/question06_scope.py) ｜ 解答：[question/answer/answer06_scope.py](question/answer/answer06_scope.py)
>
> ねらい：ローカル変数とグローバル変数のどちらが使われるかを、実行する前に予想できるようになる

---

## 7. 関数はオブジェクト

> サンプル：[example/ex10_pass_function.py](example/ex10_pass_function.py) — 関数を、別の関数の引数として渡して実行する<br>
> サンプル：[example/ex11_function_object.py](example/ex11_function_object.py) — `()`を付けると「実行」、付けないと「関数そのもの」

ここから先は、`@app.route()`のようなデコレータの仕組みを理解するための内容です。Pythonでは関数もオブジェクトであり、変数への代入や引数として渡すことができます。

```python
def a():
    print("A")

def b(func):
    print("---Start---")
    func()          # 引数として受け取った関数を実行
    print("---End---")

b(a)
```

| 書き方 | 動作 |
|---|---|
| `x = a` | 関数オブジェクトを変数に代入（実行しない） |
| `x = a()` | 関数を実行してその戻り値を代入 |
| `b(a)` | 関数オブジェクトを引数として渡す |
| `b(a())` | 関数を実行した戻り値を引数として渡す |

### 用語：第一級オブジェクト・高階関数

| 用語 | 説明 |
|---|---|
| **第一級オブジェクト** | 変数への代入・引数への受け渡し・戻り値として返すことができる値。Pythonの関数は第一級オブジェクト |
| **高階関数** | 関数を引数として受け取ったり、戻り値として返したりする関数 |

### 動作確認

```bash
python 02_backend/03_function/example/ex10_pass_function.py
python 02_backend/03_function/example/ex11_function_object.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| `ex10`を実行する | `---Start---`・`A`・`---End---`の3行が表示される（渡した関数`a`が`b`の中で実行された） |
| `ex11`を実行する | `print(x)`・`print(a)`では`<function a at 0x...>`（関数そのもの）、`print(a())`では`A`の次に`None`（実行した結果の戻り値）が表示される |

### 練習問題7：関数を渡す

> 問題：[question/question07_pass_function.py](question/question07_pass_function.py) ｜ 解答：[question/answer/answer07_pass_function.py](question/answer/answer07_pass_function.py)
>
> ねらい：関数を「値」として別の関数に渡し、受け取った側で実行できるようになる

---

## 8. 関数内関数（クロージャ）

> サンプル：[example/ex12_closure.py](example/ex12_closure.py) — 関数の中で作った関数を返すと、「前後に処理が付いた新しい関数」を作れる

関数の中に関数を定義し、それを戻り値として返すクロージャのパターンです。

### なぜ「関数を返す」必要があるのか

7節の`b(func)`は関数を受け取って**その場で実行**していました。これでは`b(a)`を呼んだ瞬間しか前後処理を挟めません。

```python
# 7 の方法：呼び出すたびに b() を経由する必要がある
b(a)   # ---Start--- A ---End---
a()    # A（前後処理なし）
```

`a()`を呼ぶだけで常に前後処理が実行されるようにするには、`a`自体を「前後処理付きの新しい関数」に置き換える必要があります。そのために「関数を返す」パターンを使います。

```python
def outer(func):
    def inner():
        print("---Start---")
        func()
        print("---End---")
    return inner         # inner 関数を返す（実行はしない）

result = outer(a)        # result = inner（前後処理付きの新しい関数）
result()                 # ---Start--- A ---End---
a = outer(a)             # a 自体を置き換えれば a() だけで前後処理が走る
```

### 用語：クロージャ

| 用語 | 説明 |
|---|---|
| **クロージャ** | 外側の関数の変数（ここでは`func`）を記憶しながら、内側の関数を戻り値として返すパターン |

`outer(a)`を呼ぶと`inner`関数が返ります。`inner`は`func`（= `a`）を覚えたまま後から実行できます。これがデコレータの核心的な仕組みです。

### 動作確認

```bash
python 02_backend/03_function/example/ex12_closure.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `---Start---`・`A`・`---End---`の3行のあとに、`<function outer.<locals>.inner at 0x...>`と表示される（`result`は`a`ではなく、`outer`が返した`inner`という別の関数） |

この節の内容は、次の9節の練習問題8（デコレータを作る）で使います。

---

## 9. デコレータ構文（@）

> サンプル：[example/ex13_decorator.py](example/ex13_decorator.py) — `@outer`と書くだけで、関数に前後の処理が付く

クロージャを`@`構文で簡潔に書いたものがデコレータです。`@app.route()`の仕組みと同じです。

```python
@outer
def a():
    print("A")

# 上記は以下と同等
# a = outer(a)
```

### 用語：デコレータ・シンタックスシュガー

| 用語 | 説明 |
|---|---|
| **デコレータ** | 関数に処理を追加・変更する仕組み。`@関数名`の形で適用する |
| **シンタックスシュガー** | 同じ動作をより簡潔に書けるようにした構文。`@outer`は`a = outer(a)`の糖衣構文 |

`@app.route("/")`も同じ仕組みで、Flaskがビュー関数をラップしてルーティング情報を登録しています。

### 動作確認

```bash
python 02_backend/03_function/example/ex13_decorator.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `a()`・`b()`のどちらも、`---Start---`→`A`（または`B`）→`---End---`の3行が表示される |
| `a`の上の`@outer`をコメントアウトして実行する（確認後は戻す） | `a()`では`A`だけが表示される（デコレータが`a = outer(a)`という置き換えをしていたことがわかる） |

### 練習問題8：デコレータを作る

> 問題：[question/question08_decorator.py](question/question08_decorator.py) ｜ 解答：[question/answer/answer08_decorator.py](question/answer/answer08_decorator.py)
>
> ねらい：前後に処理を付けるデコレータを、自分で書けるようになる

---

## 10. 可変長引数付きデコレータ

> サンプル：[example/ex14_decorator_args.py](example/ex14_decorator_args.py) — `inner`が`*args`・`**kwargs`を受け取ると、引数の違う関数にも同じデコレータを使える

`*args` / `**kwargs`を使い、任意の引数を持つ関数にも対応したデコレータです。

```python
def outer(func):
    def inner(*args, **kwargs):
        print("---Start---")
        func(*args, **kwargs)
        print("---End---")
    return inner
```

`inner`が`*args` / `**kwargs`を受け取ることで、引数の数や種類を問わず任意の関数に適用できる汎用デコレータになります。

### 動作確認

```bash
python 02_backend/03_function/example/ex14_decorator_args.py
```

| 確認する操作 | 確認したいこと |
|---|---|
| 実行する | `show_sum`（引数1つ）で`150`、`show_info`（引数1つ＋キーワード引数`unit`）で3人分の情報が、それぞれ`---Start---`と`---End---`に挟まれて表示される |
| `ex13`の`outer`（`inner()`が引数を受け取らない）を`show_sum`に付けて実行してみる | `TypeError`になる（`*args`・`**kwargs`が無いと、引数のある関数には使えない） |

### 練習問題9：戻り値を使うデコレータ

> 問題：[question/question09_decorator_args.py](question/question09_decorator_args.py) ｜ 解答：[question/answer/answer09_decorator_args.py](question/answer/answer09_decorator_args.py)
>
> ねらい：引数と戻り値のある関数にも使えるデコレータを書けるようになる（Flaskの`@app.route()`と同じ形）

---

## 次のステップ

続きは [04_flask_basic](../04_flask_basic/) です。この章で学んだデコレータを使って、Flaskの`@app.route()`でURLと関数を結びつけます。

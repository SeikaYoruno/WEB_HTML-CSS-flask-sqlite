"""
解答6：スコープを予想する

ねらい：ローカル変数とグローバル変数のどちらが使われるかを、実行する前に予想できるようになる
"""

x = "グローバル"


def show():
    print(x)              # Q1 正解：グローバル（関数の中に x が無いので、外の x を読む）


def show_local():
    x = "ローカル"        # 関数の中で代入した x は、別のローカル変数
    print(x)              # Q2 正解：ローカル


def change():
    global x              # 外の x を書き換えると宣言する
    x = "書き換えた"


show()
show_local()
print(x)                  # Q3 正解：グローバル（show_local の x はローカルなので、外の x は変わっていない）
change()
print(x)                  # Q4 正解：書き換えた（global 宣言をした change() が書き換えた）

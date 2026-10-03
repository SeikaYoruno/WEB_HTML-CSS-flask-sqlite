"""
サンプル：デフォルト引数（README「3. 引数の種類」）

ねらい：引数を省略したときに、デフォルト値で補われることを確かめる
実行：python 02_backend/03_function/example/ex03_default_args.py
見てほしい出力：3、5、5、5 の4行
"""

# 例1：すべての引数にデフォルト値がある
def add1(a=1, b=2):
    print(a + b)


add1()        # 3：両方省略 → a=1, b=2
add1(3, 2)    # 5：両方指定


# 例2：一部の引数だけにデフォルト値がある
def add2(a, b=2):
    print(a + b)


add2(3)       # 5：b を省略 → b=2
add2(a=3)     # 5：キーワード引数で a だけ指定

# デフォルト値は右側の引数から付ける。次の書き方は SyntaxError になる
# def add3(a=1, b):
#     print(a + b)

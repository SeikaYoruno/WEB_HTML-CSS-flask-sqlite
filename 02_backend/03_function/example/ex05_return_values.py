"""
サンプル：戻り値（README「4. 戻り値の詳細」）

ねらい：複数の値を返す・途中で return して抜ける・return が無いと None が返る、の3つを確かめる
実行：python 02_backend/03_function/example/ex05_return_values.py
見てほしい出力：1 5、None、5.0、Hello, Alice の次に None
"""

# 複数の値を返す（タプルとして返り、2つの変数に分けて受け取れる）
def min_max(numbers):
    return min(numbers), max(numbers)


lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)            # 1 5


# 早期 return：条件に合わないときは、途中で関数を抜ける
def divide(a, b):
    if b == 0:
        return None      # 0 で割らないように、ここで終わる
    return a / b


print(divide(10, 0))     # None
print(divide(10, 2))     # 5.0


# return が無い関数は None を返す
def greet(name):
    print(f'Hello, {name}')


result = greet('Alice')  # Hello, Alice（関数の中の print が表示する）
print(result)            # None（戻り値）

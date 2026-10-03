"""
解答7：関数を渡す

ねらい：関数を「値」として別の関数に渡し、受け取った側で実行できるようになる
"""

def hello():
    print("こんにちは")


def repeat(func, times):     # 関数と回数を受け取る
    for _ in range(times):
        func()               # 受け取った関数を実行する


repeat(hello, 3)             # hello に () を付けずに渡す（付けると、渡す前に実行してしまう）

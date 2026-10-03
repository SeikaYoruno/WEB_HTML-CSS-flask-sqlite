"""
解答8：デコレータを作る

ねらい：前後に処理を付けるデコレータを、自分で書けるようになる
"""

def log(func):
    def inner():
        print("=== 開始 ===")
        func()
        print("=== 終了 ===")
    return inner


@log                 # greet = log(greet) と同じ
def greet():
    print("Hello!")


greet()

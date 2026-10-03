"""
サンプル：デコレータ（@）（README「9. デコレータ構文（@）」）

ねらい：@outer と書くだけで、関数に前後の処理が付くことを確かめる（a = outer(a) と同じ）
実行：python 02_backend/03_function/example/ex13_decorator.py
見てほしい出力：a() と b() のどちらも、---Start--- と ---End--- に挟まれて表示される
"""

def outer(func):
    def inner():
        print('---Start---')
        func()
        print('---End---')
    return inner


@outer               # a = outer(a) と同じ意味
def a():
    print('A')


@outer               # b = outer(b) と同じ意味
def b():
    print('B')


a()
b()

"""
サンプル：関数を返す関数（クロージャ）（README「8. 関数内関数（クロージャ）」）

ねらい：関数の中で作った関数を返すと、「前後に処理が付いた新しい関数」を作れることを確かめる
実行：python 02_backend/03_function/example/ex12_closure.py
見てほしい出力：---Start---、A、---End--- の3行と、result が inner という別の関数であること
"""

def outer(func):
    def inner():                 # 関数の中で関数を作る
        print('---Start---')
        func()                   # outer が受け取った func を覚えている
        print('---End---')
    return inner                 # inner を返す（まだ実行しない）


def a():
    print('A')


result = outer(a)    # result には「前後処理付きの a」＝ inner が入る
result()             # ---Start--- A ---End---
print(result)        # <function outer.<locals>.inner at 0x...>

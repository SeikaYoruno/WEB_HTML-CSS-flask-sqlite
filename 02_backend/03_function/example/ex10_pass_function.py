"""
サンプル：関数を引数に渡す（README「7. 関数はオブジェクト」）

ねらい：関数を、別の関数の引数として渡し、その中で実行できることを確かめる
実行：python 02_backend/03_function/example/ex10_pass_function.py
見てほしい出力：---Start---、A、---End--- の3行
"""

def a():
    print('A')


def b(func):            # 関数を引数として受け取る
    print('---Start---')
    func()              # 受け取った関数を、ここで実行する
    print('---End---')


b(a)                    # a に () を付けずに渡す（関数そのものを渡す）

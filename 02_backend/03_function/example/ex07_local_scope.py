"""
サンプル：ローカル変数（README「6. 変数のスコープ」）

ねらい：関数の中で作った変数は、関数の外からは使えないことを確かめる
実行：python 02_backend/03_function/example/ex07_local_scope.py
見てほしい出力：Hello, Alice
"""

def greet():
    name = 'Alice'    # ローカル変数：この関数の中だけで使える
    print('Hello,', name)


greet()
# print(name)         # コメントを外すと NameError：関数の外からは name を使えない

"""
サンプル：グローバル変数を読む（README「6. 変数のスコープ」）

ねらい：関数の外で作った変数は、関数の中から「読む」ことはできることを確かめる
実行：python 02_backend/03_function/example/ex08_global_read.py
見てほしい出力：こんにちは
"""

message = 'こんにちは'   # グローバル変数：ファイル全体で使える


def greet():
    print(message)        # 読むだけなら、関数の中からも使える


greet()

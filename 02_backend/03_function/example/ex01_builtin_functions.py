"""
サンプル：組み込み関数（README「1. 組み込み関数」）

ねらい：import しなくても使える関数があること、そして「画面に出す関数」と「値を返す関数」の違いを確かめる
実行：python 02_backend/03_function/example/ex01_builtin_functions.py
見てほしい出力：3、<class 'int'>、6 の3行。len() や sum() は print() で包まないと何も表示されない
"""

print(len('abc'))       # 3：文字数（要素の数）を返す
print(type(123))        # <class 'int'>：データの型を返す
print(sum([1, 2, 3]))   # 6：合計を返す

len('abc')              # 値を返すだけなので、画面には何も出ない

# 使える組み込み関数の一覧（70個以上ある）を見たいときは、次の2行のコメントを外す
# import builtins
# print(dir(builtins))

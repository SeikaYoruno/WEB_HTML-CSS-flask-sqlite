"""
サンプル：グローバル変数を書き換える（README「6. 変数のスコープ」）

ねらい：関数の中でグローバル変数を「書き換える」には global 宣言が必要なことを確かめる
実行：python 02_backend/03_function/example/ex09_global_write.py
見てほしい出力：0 と 1
"""

count = 0


def increment_wrong():
    count += 1        # UnboundLocalError：global なしで外の変数に代入しようとしている


def increment():
    global count      # 「この count は外の変数」と宣言する
    count += 1


print(count)   # 0
increment()
print(count)   # 1
# increment_wrong()   # コメントを外すと UnboundLocalError

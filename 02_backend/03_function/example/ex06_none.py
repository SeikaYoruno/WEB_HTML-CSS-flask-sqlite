"""
サンプル：None（README「5. Noneとは」）

ねらい：「値が無い」ことを表す None と、「中身が空のリスト」[] の違いを確かめる
実行：python 02_backend/03_function/example/ex06_none.py
見てほしい出力：True、<class 'NoneType'>、False、0
"""

result = None
print(result is None)        # True：None かどうかは is で調べるのが慣例
print(type(result))          # <class 'NoneType'>

empty_list = []
print(empty_list is None)    # False：空のリストは None ではない（リストは存在している）
print(len(empty_list))       # 0：中身の数は 0

empty_list.append('メモ')    # 空のリストには追加できる
# result.append('メモ')      # コメントを外すと AttributeError：None には追加できない

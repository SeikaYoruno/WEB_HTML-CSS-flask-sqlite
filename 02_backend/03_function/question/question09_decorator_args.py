"""
練習問題9：戻り値を使うデコレータ

add(a, b) と multiply(a, b) の両方に使える、結果を表示するデコレータ show_result を作ってください。

期待する出力：
add の結果 → 8
multiply の結果 → 15

ヒント：
- inner は *args・**kwargs で引数を受け取り、元の関数に渡す
- 元の関数の戻り値を result = func(*args, **kwargs) で受け取ってから表示する
- 関数の名前（'add' など）は func.__name__ で取り出せる
- inner の最後で result を return しておくと、デコレータを付けても元の関数と同じように戻り値を使える
"""

# ここにデコレータ show_result を定義する


@show_result
def add(a, b):
    return a + b


@show_result
def multiply(a, b):
    return a * b


add(3, 5)
multiply(3, 5)

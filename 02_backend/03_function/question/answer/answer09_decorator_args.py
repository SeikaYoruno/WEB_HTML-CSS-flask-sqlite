"""
解答9：戻り値を使うデコレータ

ねらい：引数と戻り値のある関数にも使えるデコレータを書けるようになる（Flaskの @app.route() と同じ形）
"""

def show_result(func):
    def inner(*args, **kwargs):           # add(3, 5) の 3, 5 を受け取る
        result = func(*args, **kwargs)    # 元の関数を実行して、戻り値を受け取る
        print(f"{func.__name__} の結果 → {result}")   # func.__name__ は関数の名前（'add' など）
        return result                     # 戻り値も、元の関数と同じように返しておく
    return inner


@show_result
def add(a, b):
    return a + b


@show_result
def multiply(a, b):
    return a * b


add(3, 5)
multiply(3, 5)

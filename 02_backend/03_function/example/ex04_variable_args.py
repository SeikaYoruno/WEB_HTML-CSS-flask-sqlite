"""
サンプル：可変長引数（*args・**kwargs）（README「3. 引数の種類」）

ねらい：引数の数が決まっていないとき、*args はタプル、**kwargs は辞書として受け取ることを確かめる
実行：python 02_backend/03_function/example/ex04_variable_args.py
見てほしい出力：(1, 2, 3) と <class 'tuple'>、{'x': 1, 'y': 2} と <class 'dict'>、args と kwargs に分かれた出力
"""

def show_args(*args):
    print(args)         # タプルとして受け取る
    print(type(args))   # <class 'tuple'>


show_args(1, 2, 3)      # (1, 2, 3)
show_args()             # 引数が無ければ空のタプル ()


def show_kwargs(**kwargs):
    print(kwargs)        # 辞書として受け取る
    print(type(kwargs))  # <class 'dict'>


show_kwargs(x=1, y=2)   # {'x': 1, 'y': 2}
show_kwargs()           # 引数が無ければ空の辞書 {}


# *args と **kwargs は、同じ関数の中で一緒に使える（この順番で書く）
def show_both(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


show_both(1, 2, x=3, y=4)   # args: (1, 2)  kwargs: {'x': 3, 'y': 4}

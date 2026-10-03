"""
サンプル：引数のある関数に使えるデコレータ（README「10. 可変長引数付きデコレータ」）

ねらい：inner が *args・**kwargs を受け取ると、引数の数や種類が違う関数にも同じデコレータを使えることを確かめる
実行：python 02_backend/03_function/example/ex14_decorator_args.py
見てほしい出力：show_sum で 150、show_info で3人分の情報が、それぞれ ---Start--- と ---End--- に挟まれて表示される
"""

def outer(func):
    def inner(*args, **kwargs):      # どんな引数でも受け取れる
        print('---Start---')
        func(*args, **kwargs)        # 受け取った引数を、そのまま元の関数に渡す
        print('---End---')
    return inner


@outer
def show_sum(nums):                  # 引数が1つ（タプル）
    total = 0
    for num in nums:
        total += num
    print(total)


@outer
def show_info(users, unit='歳'):     # 引数が1つ＋キーワード引数
    for name, age in users.items():
        print(f'{name}：{age}{unit}')


show_sum((10, 20, 30, 40, 50))
show_info({'Tom': 30, 'Ken': 40, 'John': 50}, unit='才')

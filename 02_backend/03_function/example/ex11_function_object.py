"""
サンプル：関数は値として扱える（README「7. 関数はオブジェクト」）

ねらい：() を付けると「実行」、付けないと「関数そのもの」になる違いを確かめる
実行：python 02_backend/03_function/example/ex11_function_object.py
見てほしい出力：<function a at 0x...> と A、print(a()) では A の次に None
"""

def a():
    print('A')


print('--- ポイント1：関数は変数に代入できる ---')
x = a        # () を付けない → 関数そのものを代入（まだ実行しない）
print(x)     # <function a at 0x...>
x()          # A：x に入っている関数を実行する

print('--- ポイント2：print(a) と print(a()) の違い ---')
print(a)     # 関数そのものを表示する
print(a())   # a() を実行（A が表示される）してから、その戻り値 None を表示する

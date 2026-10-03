"""
解答4：可変長キーワード引数（**kwargs）

ねらい：名前付きの値をいくつでも、**kwargs で辞書として受け取れるようになる
"""

def show_user(**info):             # name=…, age=… が、辞書 info に入る
    for key, value in info.items():
        print(f"{key}：{value}")


show_user(name="太郎", age=20, hobby="ゲーム")

"""
解答3：可変長位置引数（*args）

ねらい：いくつ渡されるかわからない値を、*args でまとめて受け取れるようになる
"""

def show_foods(*foods):          # 渡された値がすべて、タプル foods に入る
    print("好きな食べ物：")
    for food in foods:
        print(food)


show_foods("カレー", "寿司", "ラーメン")

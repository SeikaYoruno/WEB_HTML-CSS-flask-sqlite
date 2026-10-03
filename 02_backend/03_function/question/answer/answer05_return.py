"""
解答5：戻り値（複数の値・早期return）

ねらい：関数から複数の値を返し、条件に合わないときは途中で None を返せるようになる
"""

def total_and_average(scores):
    if len(scores) == 0:
        return None                    # 空なら平均を計算できないので、ここで抜ける（早期return）
    total = sum(scores)
    return total, total / len(scores)  # 2つの値を返す（タプルになる）


print(total_and_average([80, 90, 70]))   # (240, 80.0)
print(total_and_average([]))             # None

total, average = total_and_average([80, 90, 70])   # 2つの変数に分けて受け取ることもできる

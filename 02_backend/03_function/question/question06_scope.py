"""
練習問題6：スコープを予想する

下のコードの4つの print（Q1〜Q4）の出力を、実行する「前に」予想して、
各行の「予想：」の後ろに書き込んでください。
書き終えたら実行して、答え合わせをします。
"""

x = "グローバル"


def show():
    print(x)              # Q1 予想：


def show_local():
    x = "ローカル"
    print(x)              # Q2 予想：


def change():
    global x
    x = "書き換えた"


show()
show_local()
print(x)                  # Q3 予想：
change()
print(x)                  # Q4 予想：

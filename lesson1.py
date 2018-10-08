"""
猜数游戏
created by 2018-09-27
author 武文
version:1.0
"""

for i in range(1, 11):

    name = int(input("COM: Guess what I think?"))

    if name < 10:
        print("COM: Your answer is too small.")
        i = i + 1
    elif name > 10:
        print("COM: Your answer is too large.")
        i = i + 1
    elif name == 10:
        print("bingo!")
        break

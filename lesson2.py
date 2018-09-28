'''
猜数游戏
created by 2018-09-27
author 武文
version 1.1
'''

while(True):
    name = eval(input("COM: Guess what I think?"))
    if name < 10:
        print("COM: Your answer is too small.")
    elif name > 10:
        print("COM: Your answer is too large.")
    elif name == 10:
        print("bingo!")
        break

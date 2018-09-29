'''
猜数游戏
created by 2018-09-27
author 武文
version 1.2
'''
from random import randint

number=randint(1,10)

while(True):
    name = eval(input("COM: Guess what I think?"))
    if name < number:
        print("COM: Your answer is too small.")
    elif name > number:
        print("COM: Your answer is too large.")
    elif name == number:
        print("bingo!")
        break

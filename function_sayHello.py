# coding=utf-8
"""
    通过sayhello学习函数的应用
"""


def sayhi():
    print("你好")
    print("hello,world")


sayhi()


def sayhi(x):
    if x == 'dog':
        print("汪，汪!")
    elif x == 'cat':
        print("喵,喵")


sayhi('dog')


def sayhi():
    global x
    print("x is ", x)
    print("x is ", x)


x = 50
sayhi()

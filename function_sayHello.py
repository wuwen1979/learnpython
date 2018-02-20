#coding=utf-8
"""
    sayhello
    函数的应用
"""


def sayHello():
    print("你好")
    print("hello,world")
sayHello()


def sayHi(x):
    if x=='dog':
        print("汪，汪!")
    elif x=='cat':
        print("喵,喵")
sayHi('dog')

def sayHi():
    global x
    print("x is ",x)
    print("x is ",x)
x=50
sayHi()

#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def foo():
    num = 10    #局部变量——定义在函数内的变量是局部变量，局部变量的作用范围只能是函数内部范围内，它不能在函数外引用。
print(num)      #NameError: name 'num' is not defined

# fix
num = 10        #定义在模块最外层的变量是全局变量，它是全局范围内可见的。
def foo():
    print(num)


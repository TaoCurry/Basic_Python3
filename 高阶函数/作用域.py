#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#public函数和变量：abc,PI,xyz
#特殊变量：__xxx__
#private函数和变量：_xxx/__xxx,不应该被直接引用。
def _private1(name):
    return 'Hello, %s' % name
def _private2(name):
    return 'Hi, %s' % name
def greeting(name):     #在模块里公开greeting()函数
    if len(name) > 3:
        return _private1()     #内部逻辑用private函数隐藏起来
    else:
        return  _private2()      #
#调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法



#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#动态创建一个class Hello
from hello import Hello     #从hello模块中引入Hello类
h = Hello()
h.hello()
#Hello World！
print(type(Hello))
#<class 'type'>
print(type(h))
#<class 'hello.Hello'>

#使用type()函数动态创建class Hello
def fn(self, name='world'):     #定义函数
    print('Hello, %s!!' % name)
Hello = type('Hello', (object,), dict(hello=fn))     #创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
#type() -> built in class
#class X(object):
#    a = 1
#X = type('X', (object,), dict(a=1))
#要创建一个class对象，type()函数依次传入3个参数：
#1.class的名称； Hello
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，使用tuple的单元素写法；(object,)
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

#metaclass
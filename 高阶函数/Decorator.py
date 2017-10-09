#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#装饰器(Decorator)——在代码运行期间动态增加功能的方式，decorator就是一个返回函数的高阶函数.
import logging
def log(func):
    def wrapper(*args, **kw):
        logging.warning('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log   #@语法糖
def now():
    print('2017-09-28')
recall = now()

#Decerator 本身需要传入参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('Run')
def now():
    print('2017-09-28')
recall = now()



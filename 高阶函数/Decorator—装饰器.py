#!/usr/bin/env python3
#-*- coding:utf-8 -*
import logging      #使用logging模块打印日志
def use_logging(func):
    def wrapper():
        logging.warning('%s is running' % func.__name__)
        return func()   #把foo当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('zen of python')
#foo = use_logging(foo)    #foo = wrapper
#foo()                     # = wrapper()

@use_logging
def foo():
    print('zen of python')
foo()
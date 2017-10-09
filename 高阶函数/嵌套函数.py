#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#定义在函数里面的函数称之为嵌套函数（nested function）
def nested_func():   #外围函数
    text = 'zen of python'
    def printer():   #嵌套函数
        print(text)  #对于嵌套函数，它可以访问到其外层作用域中声明的非局部（non-local）变量.
    printer()

nested_func()
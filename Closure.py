#!/bin/env python
# -*- coding: utf-8 -*-
#闭包:如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）。

def nested_func():   #	外围函数
    text = 'zen of python'
    def printer():   #	嵌套函数
        print(text)  #	对于嵌套函数，它可以访问到其外层作用域中声明的非局部（non-local）变量.
    return printer
another = nested_func()     #	another就是一个闭包，闭包本质上是一个函数.
another()                   #	闭包使得这些变量的值始终保存在内存中。(text = 'zen of python')



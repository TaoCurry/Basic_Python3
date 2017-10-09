#!/usr/bin/env python3
#-*- coding:utf-8 -*-

""""a test module"""    #模块的文档注释

__author__ = 'Curry'    #使用__author__变量把作者写进去
import sys      #导入该模块，有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) ==2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':      #这个还是有点搞不懂！！！
    test()
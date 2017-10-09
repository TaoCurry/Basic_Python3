#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#闭包:如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）。

# why f1(), f2(), f3() returns 9, 9 ,9 rather than 1, 4, 9
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
#print(f1())
#print(f2())
#print(f3())

print(f1(), '\n', f2(), '\n', f3())

# fix:
def count2():
    fs = []
    def f(j):
        def g():
            return j * j    #绑定当前循环变量当前的值。
        return g
    for i in range(1, 4):
        fs.append(f(i))   #f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count2()
print(f1(), '\n', f2(), '\n', f3())
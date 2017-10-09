#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#__str__
class Student(object):
    def __init__(self, name):
        self.name = name
print(Student('Curry'))
#<__main__.Student object at 0x000001EA098CD080>

#Update
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):      #
        return 'Student object (name：%s)' % self.name
print(Student('Curry'))
#Student object (name：Curry)    -用户看到的字符串

#不使用print
s = Student('Curry')
s
#<__main__.Student object at 0x109afb310> - 程序开发者看到的字符串
#原因:直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

#Update1
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name：%s)' % self.name
    __repr__ = __str__
s = Student('Curry')
s

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1       #初始化两个计数器a，b
    def __iter__(self):             #实例本身就是迭代对象，故返回自己
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b    #计算下一个值
        if self.a > 1000:       #退出循环的条件
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)

#__getitem__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            return StopIteration()
        return self.a
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a
f = Fib()
print(f[0])
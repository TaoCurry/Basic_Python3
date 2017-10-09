#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#
class Student(object):
    pass
s = Student()
s.name = 'Curry'    #动态给实例绑定一个属性
print(s.name)

#限制实例的属性，只允许添加指定的属性
class Student(object):
    __slots__ = ('name', 'score')       #用tuple定义允许绑定的属性名称
s = Student()
s.name = 'Curry'
s.score = 30
print(s.name)
print(s.score)
#s.age = 25   #AttributeError: 'Student' object has no attribute 'age'

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.age = 25
print(g.age)    #25
#!/usr/bin/env python3
#-*- coding:utf-8 -*-#
#定义实例属性
class Student(object):
    def __init__(self, name, score):    #创建实例属性
        self.name = name
        self.score = score
#定义类属性
class Student(object):
    name = 'Student'        #定义一个类属性，归类所有，但是所有属性都可以访问到。
s = Student()  #创建一个实例
print(s.name)           #打印实例属性，因为实例并没有name属性，所以会继续查找class的name属性
#Student
print(Student.name)     #打印类属性
#Student
s.name = 'Curry'        #给实例绑定name属性
print(s.name)           #由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
#Curry
print(Student.name)     #类属性只是被屏蔽掉，并未消失
#Student
del s.name              #删除实例属性
print(s.name)           #再次调用，由于实例的name属性没有找到，类的name属性就显示出来了
#Student
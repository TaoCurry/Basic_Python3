#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Student(object):      #Student类, object 继承类
    def __init__(self, name, score):  #对Student类绑定属性->__init__方法,第一个参数永远为创建实例本身-self.
        self.name = name        #Student类有name和score属性
        self.score = score
    def print_score(self):      #定义一个方法，第一个参数必须是self
        print('%s: %s ' % (self.name, self.score))      #数据封装起来.
    def get_grade(self):        #新增一个方法
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)      #创建一个实例，类名+()
lisa = Student('Lisa Simpson', 91)
bart.print_score()
bart.get_grade()
lisa.print_score()
lisa.get_grade()
print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
print(bart.name)


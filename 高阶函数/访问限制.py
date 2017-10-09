#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Student():
    def __init__(self, name, score):
        self.__name = name      #私有变量，private
        self.__score = score    #确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))
    def get_grate(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    #外部代码要获取内部属性__name,__score,可以添加新的方法。
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    #外部代码要修改属性的方法：
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise  ValueError('bad score')
bart = Student('Bart Simpson', 57)
lisa = Student('Lisa Simpson', 98)
#bart.__name     # -> 'Student' object has no attribute '__name'.无法访问内部属性
print(bart.get_name(), bart.get_score())
bart.set_score(97)
print(bart.get_name(), bart.get_score())

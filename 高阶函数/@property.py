#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Student(object):
    pass
    def get_score(self):
        return self.__score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self.__score = value
s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(101)
#Traceback (most recent call last):
#...
#ValueError: score must between 0-100

class Student(object):
    @property       #将get_score方法变成属性，写
    def score(self):
        return self.__score
    @score.setter   #将set_score方法变成属性，读
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self.__score = value
s = Student()
s.score = 60
print(s.score)
#s.score = 101
#print(s.score)
##s.set_score(101)
#Traceback (most recent call last):
#...
#ValueError: score must between 0-100

#
class Student(object):
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self, value):
        self.__value = value
    @property       #age只能读，age可以根据birth和当前时间计算出来。
    def age(self):
        return 2017 - self.__birth
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width * self.__height
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)







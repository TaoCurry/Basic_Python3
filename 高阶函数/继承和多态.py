#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Animal(object):       #Animal-Subclass, object-Base class,Supper class
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
cat = Cat()
dog.run()       #Animal is running...
cat.run()       #Animal is running...
class Dog(Animal):
    def run(self):      #子类和父类有相同的方法时，子类的方法会覆盖了父类的方法-多态
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
dog1 = Dog()
cat1 = Cat()
dog1.run()      #Dog is running...
cat1.run()      #Cat is running...
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
#Animal is running...
#Animal is running...
run_twice(Dog())
#Dog is running...
#Dog is running...
run_twice(Cat())
#Cat is running...
#Cat is running...
#“开闭”原则:对扩展开放;对修改封闭。
#动态语言的“鸭子类型”
class Timer(object):
    def run(self):
        print('Time is Money')
timer = Timer()
timer.run()

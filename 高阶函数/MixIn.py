#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#多重继承
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#需要加上某些功能
class RunnalbeMixIn(object):
    def run(self):
        print('Running...')
class FlyableMixIn(object):
    def fly(self):
        print('Flying...')
#对于需要Runnable功能的动物，就多继承一个Runnable
class Dog(Mammal, RunnalbeMixIn):
    pass
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Bat(Bird, FlyableMixIn):       #MixIn
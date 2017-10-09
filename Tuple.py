#!/usr/bin/env pyhton 3
# -*- coding: utf-8 -*-
#定义一个tuple的关键是逗号，
tuple1 = (1,2,3,4,5,6,,7,8,9)
tuple1[1]
tuple1[:4]
tuple1[4:]
tuple2 = tuple1[:]#copy
temp = (1)
type(temp)
temp1 = (1,)#<class 'int'>
type(temp1)#<class 'tuple'>
temp2 = 2,3,4,5
type(temp2)#<class 'tuple'>
8 *(8)
8* (8,)

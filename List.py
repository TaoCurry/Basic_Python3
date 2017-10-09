#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#list操作可以分为添加和删除两大类，添加和删除又可以细分。
classmates = ['Micheal','Jordan','Curry']
print('classmates =',classmates)
print('len(classmates)=',len(classmates))  
classmates[-1]#取最后一个元素
#classmates
#print(classmates)
classmates[-2]#取倒数第二个元素
#print(classmates)
classmates.append('30')#末尾加一个元素
print(classmates)
classmates,extend(['KD','Green'])#extend将扩展，可以插入多个元素至list，但是必须以list形式。
classmates.extend('KD')#若扩展为一个字符串，打印出来的结果将为单个字符形式。
classmates.insert(2,'SC')#指定插入一个元素
print(classmates)
classmates.pop()#删除末尾元素
print(classmates)
classmates.pop(0)#根据索引index，指定删除一个元素
classmates[0]='MC'
classmates.remove('KD')#删除指定元素
del classmates[0]#删除指定index的元素
del classmates#删除整个语句，打印classmates，会提示name 'classmates' is not defined。
print(classmates)
L=[123,456,'789,987',654,321]
L[2][0]
L[2][1]
L=[123,456[789,987],654,321]
L[2][0]
L[2][1]

#序列相加
[1,2,3] + [4,5,6]
'Hello' + 'World'
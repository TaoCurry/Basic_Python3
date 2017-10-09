#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#try...except...finally
#try机制
try:
    print('try...')
    r = 10 / 0          #发生错误时，print('result:', r)不会执行
    print('result:', r)
except ZeroDivisionError as e:      #except捕获到ZeroDivisionError
    print('except:', e)
finally:
    print('finally...')
print('END')

#No Error
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

#Varialble Error
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No Error!')
finally:
    print('finally...')
print('END')

#所有的错误都是从BaseException类派生的
#！/usr/bin/env python 3
# -*- coding: utf-8 -*-
def discount(price,rate):					#price,rate为局部变量
	final_price = price * rate
	return final_price 						#final_price为局部变量
old_price = float(input('请输入原价：'))	#old_price全局变量
rate = float(input('请输入折扣率：'))		#rate全局变量
new_price = discount(old_price,rate)		#new_price全局变量
print('打完折的价格是：',new_price)	
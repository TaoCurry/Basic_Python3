def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
number = int(input('请输入一个正整数：'))
result = fact(number)
print('%d 的阶乘是：%d' % (number,result))

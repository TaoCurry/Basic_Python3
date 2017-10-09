def fibo(n):
    if n < 1:
        print('输入有误')
        return -1
    elif n ==1 or n ==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
result = fibo(35)
if result != -1:
    print('一共有%d小兔崽子'% result)

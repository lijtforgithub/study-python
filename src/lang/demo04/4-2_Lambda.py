# Python 使用 lambda 来创建匿名函数。

x = lambda a: a + 10
print(x(5), '\n')

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
print()


def lambda_func(n):
    return lambda a: a * n


l1 = lambda_func(2)
l2 = lambda_func(3)
print(l1(11))
print(l2(11))

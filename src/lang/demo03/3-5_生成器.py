# 使用了 yield 的函数被称为生成器（generator）。yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的迭代器，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。

import sys


def count_down(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
generator = count_down(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1
print()


# 生成器函数 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

# 实现__iter__和__next__方法就是迭代器 StopIteration 异常用于标识迭代的完成
# 节约内存
from collections.abc import Iterator
from itertools import count

counter = count(start=100)
for i in range(5):
    print(next(counter))
print(isinstance(counter, Iterator))
print(isinstance([], Iterator))

list = [1, 2, 3, 4]
# 把可迭代对象转变为迭代器对象
it = iter(list)

for x in it:
    print(x, end=" ")
print("\n")
print('第一次迭代结束')

for x in it:
    print(x, end=" ")
print("\n")
print('第二次迭代结束')


# print(next(it))
# print(next(it))


# it1 = iter(list)
# while True:
#     try:
#         print(next(it1))
#     except StopIteration:
#         sys.exit()


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 8:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_num = MyNumbers()
# print(next(my_num))

my_it = iter(my_num)
# print(next(my_it))

for x in my_it:
    print(x)


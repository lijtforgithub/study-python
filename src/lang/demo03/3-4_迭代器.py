# StopIteration 异常用于标识迭代的完成

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))

for x in it:
    print(x, end=" ")
print("\n")
print()


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
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_num = MyNumbers()
my_it = iter(my_num)

for x in my_it:
    print(x)

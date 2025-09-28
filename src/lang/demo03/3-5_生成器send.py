
def demo():
    print("Hello")
    t = yield 5
    print("World")
    print(t)


f = demo()
# 预激活生成器 print(f.send(None))
print(next(f))
try:
    f.send('test')
except StopIteration as e:
    print('异常', e.value)


def countdown(n):
    print('counting down from', n)
    while n >= 0:
        new_value = yield n
        if new_value is not None:
            n = new_value
        else:
            n -= 1


c = countdown(10)

for x in c:
    print(x)
    if x == 10:
        print(c.send(3))
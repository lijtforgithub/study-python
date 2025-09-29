
def ww():
    print('汪汪')

class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}正在吃'.format(self.name))

    def sleep(self):
        print('{}正在睡'.format(self.name))


dog = Dog('二哈')
attr = input('请输入要执行的方法名称：')
print(hasattr(dog, attr))

if hasattr(dog, attr):
    try:
        func = getattr(dog, attr)
        func()
    except TypeError as e:
        print(getattr(dog, attr))
else:
    print('你输入的方法名不存在', attr)

attr = input('请输入要添加的属性名称：')
value = input('请输入的要添加的属性值：')
if value.isdigit():
    setattr(dog, attr, int(value))
else:
    setattr(dog, attr, value)


talk = 'talk'

setattr(dog, talk, ww)
getattr(dog, talk)()

delattr(dog, talk)

print(dir(dog))
class Student(object):
    __isinstance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def __init__(self, name):
        print('我是 {}'.format(name))


stu1 = Student('张三')
stu2 = Student('李四')

print(stu1)
print(stu2)

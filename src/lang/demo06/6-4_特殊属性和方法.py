class Student:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Student(self.name + other.name, self.age + other.age)

    def __len__(self):
        return len(self.name)

    # __str__优先级高于__repr__
    def __str__(self):
        return f'str: {self.name}, {self.age}'

    def __repr__(self):
        return f'repr: {self.name}, {self.age}'

    def __del__(self):
        print(f'析构函数 销毁对象: {id(self)}')

    def __getattribute__(self, item):
        try:
            print('访问属性 {}'.format(item))
            return super().__getattribute__(item)
        except AttributeError as e:
            print('访问未定义属性 {}'.format(item))
            return 'default'

    # 访问不存在的属性才会被调用 __getattribute__ 不能捕获异常
    def __getattr__(self, item):
        print('访问未定义属性 {}'.format(item))

    def __setattr__(self, key, value):
        if key == 'age':
            if value < 18:
                raise Exception('age的值必须大于18')
            else:
                self.__dict__[key] = value
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        pass


stu1 = Student("张三", 20)
stu2 = Student("李四", 30)
print(stu1)
print(stu2)
print(stu1 + stu2)
print(len(stu1))
stu1.__dict__['xx'] = 'OO'
print(stu1.xx)

print(dir(Student))
print(Student.__dict__)
print(Student.__class__)
print(Student.__bases__)
print(stu1.__dict__)
print(__file__)

del stu1

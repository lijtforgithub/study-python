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
    def __str__(self):
        return f'{self.name}, {self.age}'


stu1 = Student("张三", 20)
stu2 = Student("李四", 30)
print(stu1)
print(stu2)
print(stu1 + stu2)
print(len(stu1))

print(dir(Student))
print(Student.__dict__)
print(Student.__class__)
print(Student.__bases__)
print(stu1.__dict__)

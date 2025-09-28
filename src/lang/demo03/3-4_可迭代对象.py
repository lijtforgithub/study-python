# 实现__iter__或__getitem__方法就是可迭代对象
from collections.abc import Iterable

class Student(object):
    pass


print(isinstance(Student, Iterable))
print(hasattr(Student, '__getitem__'))
print(hasattr([], '__getitem__'))


class Employee:
    def __init__(self, employee):
        self.employee = employee

    # item是解释器帮我们维护的索引值 当再for循环中时 自动从0开始计数
    def __getitem__(self, item):
        return self.employee[item]


emp = Employee(['张三', '李四', '王五'])
for i in emp:
    print(i)
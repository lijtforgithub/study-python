# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(issubclass(bool, int))
print(True == 1, True + 1)
print(False == 0, False + 1)
# 布尔类型的整数表现
print(int(True))  # 1
print(int(False))  # 0

# del语句删除单个或多个对象
del a
del b, c

# / 返回一个浮点数，// 返回一个整数
x, y = 10, 2
print(x // y)
print(x / y)

# 布尔逻辑运算
print(True and False)  # False
print(True or False)  # True
print(not True)

# 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 0、空字符串、空列表、空元组等被视为 False
# 使用 bool() 函数进行转换
print(bool(0))  # False
print(bool(42))  # True
print(bool(''))  # False
print(bool('Python'))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True

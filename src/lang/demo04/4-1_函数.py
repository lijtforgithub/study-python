# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

# 不可变参数 strings, tuples, 和 numbers
def un_change(num):
    print(id(num))  # 指向的是同一个对象
    num = 10
    print(id(num))  # 一个新对象


num = 1
print(id(num))
un_change(num)
print()


# 可变参数 list,dict 等
def change(list):
    list.append([1, 2, 3, 4])
    print("函数内取值: ", list)
    return


list = [10, 20, 30]
change(list)
print("函数外取值: ", list)
print()


# 关键字和默认参数
def param_key_def(name, age=10):
    print(name, "年龄: ", age)
    return


param_key_def(age=50, name="关键字")
param_key_def(name="默认值")
print()


# 可变参数 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def variable_param1(arg1, *var_tuple):
    print(arg1)
    print(var_tuple)


variable_param1(70, 60, 50)
variable_param1(10)
print()


# 两个星号 ** 的参数会以字典的形式导入
def variable_param2(arg1, **var_dict):
    print(arg1)
    print(var_dict)


variable_param2(1, a=2, b=3)


def fun1(a, b, c):
    print(a, b, c)

list1 = [1, 2, 3]
fun1(*list1)

dict1 = {"c": 3, "b": 2, "a": 1}
fun1(**dict1)

# * 号后面的参数必须使用关键字传参
def fun2(a, b, *, c):
    print(a, b, c)
fun2(1, 2, c=3)

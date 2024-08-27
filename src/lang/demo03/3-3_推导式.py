# 列表推导式
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典推导式
list_demo = ['Google', 'Runoob', 'Taobao']
new_dict = {key: len(key) for key in list_demo}
print(new_dict)

dic = {x: x ** 2 for x in (2, 4, 6)}
print(dic)

# 集合推导式
new_set = {i ** 2 for i in (1, 2, 3)}
print(new_set)

# 元组推导式（生成器表达式）
a = (x for x in range(1, 10))
print(a)
print(tuple(a))

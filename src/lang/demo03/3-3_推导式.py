# 列表推导式
list = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_list = [name.upper() for name in list if len(name) > 3]
print(new_list)
print()

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
print()

# 字典推导式
list = ['Google', 'Runoob', 'Taobao']
new_dict = {key: len(key) for key in list}
print(new_dict)
print({x: x ** 2 for x in (2, 4, 6)})
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# 集合推导式
new_set = {i ** 2 for i in (1, 2, 3)}
print(new_set)
print({x for x in 'abracadabra' if x not in 'abc'})
print()

# 元组推导式（只有元祖返回的是生成器）
a = (x for x in range(1, 10))
print(a)
print(tuple(a))

t = 12345, 54321, 'hello!'
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
print()

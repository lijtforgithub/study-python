'''
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型
'''



map = {}
map['one'] = "1 - 菜鸟教程"
map[2] = "2 - 菜鸟工具"

tiny_dict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(map['one'])  # 输出键为 'one' 的值
print(map[2])  # 输出键为 2 的值
print(tiny_dict)  # 输出完整的字典
print(tiny_dict.keys())  # 输出所有键
print(tiny_dict.values())  # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典
d1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(d1)
print(dict(Runoob=1, Google=2, Taobao=3))


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
print()

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# 字典生成式
keys = ['a', 'b', 'c']
vals = [1, 2, 3, 4]
dict = {k.upper():v for k, v in zip(keys, vals)}
print(dict.get('a'))
# KeyError
print(dict['a'])
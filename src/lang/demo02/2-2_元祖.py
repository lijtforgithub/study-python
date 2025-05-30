# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tiny_tuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tiny_tuple * 2)  # 输出两次元组
print(tuple + tiny_tuple)  # 连接元组

# 如果你想创建只有一个元素的元组，需要注意在元素后面添加一个逗号，以区分它是一个元组而不是一个普通的值，这是因为在没有逗号的情况下，Python会将括号解释为数学运算中的括号，而不是元组的表示。
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
not_a_tuple = (42)
print(type(tup2))
print(type(not_a_tuple))
# string、list 和 tuple 都属于 sequence（序列）。

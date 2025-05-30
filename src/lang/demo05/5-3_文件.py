path = '/Users/lijingtang/Downloads/python/python.txt'

f = open(path, 'w')
f.write('Python 是一个非常好的语言。\n是的，的确非常好!!\n')
f.close()

f1 = open(path, 'r')
s1 = f1.read(6)
print(s1)
print(f1.read())

f2 = open(path, 'r')
s2 = f2.readline()
print(s2)

f3 = open(path, 'r')
print(f3.readlines())
print()

f = open(path, 'r+')
value = ('www.runoob.com', 14)
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换
s = str(value)
f.write(s)
print(f.tell())
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾 from_what 值为默认为0，即文件开头
f.seek(0)
print(f.readline())
f.close()

# 在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位
f = open(path, 'rb+')
f.seek(2, 1)
print(f.read(14))


# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
with open(path, 'r') as f:
    read_data = f.read()
print(f.closed)

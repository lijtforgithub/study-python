'''
字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
'''
str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次 星号 * 是重复操作
print(str + '你好')  # 连接字符串
print(".".join('join效率更好'))

print("我叫 %s 今年 %d 岁!" % ('小明', 10))

print("{1} {0} {1}".format("hello", "world"))
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


# 传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

# 使用大括号 {} 来转义大括号
print("{} 对应的位置是 {{0}}".format("runoob"))

print("{:.2f}".format(3.1415926))
print('{:b}'.format(11))

print("{:>10d}".format(13))
print("{:-^10d}".format(13))

print("{:.2%}".format(0.25))

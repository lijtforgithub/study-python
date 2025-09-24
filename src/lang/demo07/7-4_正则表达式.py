import re

# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 None
print(re.match('www', 'www.runoob.com').span())

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    # 返回对应括号组匹配的字符串
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("No match!!")

print()

# re.search 扫描整个字符串并返回第一个成功的匹配
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

phone = "2004-959-559 # 这是一个电话号码"

num = re.sub(r'#.*$', "", phone)
print("删除注释 : ", num)
num = re.sub(r'\D', "", phone)
print("移除非数字 : ", num)
print()


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub(r'(?P<value>\d+)', double, s))
print(re.findall(r'\d+', 'runoob 123 google 456'))

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

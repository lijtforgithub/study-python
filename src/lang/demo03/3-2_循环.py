# while 循环使用 else 语句 如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
# 在 Python 中，for...else 语句用于在循环结束后执行一段代码。
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d \n" % (n, sum))

count = 5
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")
print()

for x in range(6):
    print(x)
else:
    print("Finally finished! \n")

for i in range(0, 10, 3):
    print(i)
print()

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
print()

print(list(range(5)))
print()

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

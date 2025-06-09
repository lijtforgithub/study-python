import random
import string

print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))


# 随机数
def generate_password(length):
    # 定义密码可用字符集合
    chars = string.ascii_letters + string.digits + string.punctuation

    # 随机选择字符生成密码
    password = ''.join(random.choice(chars) for _ in range(length))

    return password


print(generate_password(4))
print(generate_password(6))

print(2 ** 3)
print(5 / 4)
print(5 // 4)
print(-5 // -4)
# 一正一负向下取整
print(-5 // 4)


a = b = 1000
c = 1000
print(a == b)
print(a is b)
print(a is c)
print(id(a))
print(id(c))

'''
在 Python3 中，bytes 类型表示的是不可变的二进制序列（byte sequence）。
创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：
此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码
'''

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(z)

# ord() 函数用于将字符转换为相应的整数值
b = bytes("hello", encoding="utf-8")
if x[0] == ord("h"):
    print("The first element is 'h'")
print(b)
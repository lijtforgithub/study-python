import sys

# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
a, b, c = 1, 2.0, '三'
print(a, b, c)

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
if True:
    print("True")
    print("1")
else:
    print("False")

# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
s = "one " + \
        "two " + \
        "three"
print(s)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
arr = ['1',
         "2",
         "3"]
print(arr)

# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
ch = 'c'
# 使用三引号(''' 或 """)可以指定一个多行字符串
paragraph = """这是一个段落，
可以由多行组成"""
print(paragraph)

# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义  r 指 raw，即 raw string，会自动将反斜杠转义
print('hello\npython')
print(r'\n')
print(r'hello\npython3')

# Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割
x = '同一行中使用多条语句'; sys.stdout.write(x + '\n')

# 不换行输出
print('第一句', end=" ")
print('第二句', end=" ")

# 等待用户输入
# input("\n\n按下 enter 键后退出。")

# 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 定义一个列表
tiny_list = [123, 'runoob']

print(list)  # 打印整个列表
print(list[0])  # 打印列表的第一个元素
print(list[1:3])  # 打印列表第二到第四个元素（不包含第四个元素）
print(list[2:])  # 打印列表从第三个元素开始到末尾
print(tiny_list * 2)  # tinyList
print(list + tiny_list)  # 打印两个列表拼接在一起的结果


def reverse_words(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    input_words = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    input_words = input_words[-1::-1]

    # 重新组合字符串
    output = ' '.join(input_words)
    return output


input = 'I like runoob'
rw = reverse_words(input)
print(rw)


# list.sort()
# list.sort(reverse=True)
# print(list)

# 列表生成式
list_range = [i * i for i in range(1, 10)]
print(list_range)

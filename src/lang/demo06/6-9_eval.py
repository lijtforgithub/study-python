# eval会返回值
# exec 不会返回值

x = 10


def func_eval():
    y = 20
    a = eval('x + y')
    print('a = ', a)

    b = eval('x + y', {'x': 1, 'y': 2})
    print('x = ', x, ' y = ', y)
    print('b = ', b)

    c = eval('x + y', {'x': 1, 'y': 2}, {'x': 3, 'y': 4})
    print('x = ', x, ' y = ', y)
    print('c = ', c)


# func_eval()


def func_exec():
    # exec 默认在哪个命名空间执行，就修改哪个命名空间。避免在函数中使用 exec 修改变量
    y = exec('x = 1 + 1')
    print('x = ', x)
    print('y = ', y)

    exec('a=[]\na.append(2)')
    # print(a)


func_exec()

exec('x = 1 + 1')
print('x = ', x)

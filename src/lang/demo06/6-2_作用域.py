import builtins
print(dir(builtins))


g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
        print(g_count, o_count, i_count)
    inner()
outer()

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
if True:
    msg = '好奇怪'
print(msg)
print()

g = 1


def scope_local():
    print('局部访问全局变量', g)


scope_local()


def scope_global():
    global g  # 需要使用 global 关键字声明 才可以修改
    print(g)
    num = 123
    print(g)


scope_global()
print(g)


def scope_nonlocal():
    l = 10

    def inner():
        nonlocal l  # nonlocal关键字声明
        num = 100
        print(l)

    inner()
    print(l)


scope_nonlocal()

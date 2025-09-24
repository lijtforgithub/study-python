
func_list = []

for i in range(3):
    # 闭包可以用来在一个函数与一组私有变量之间创建关联关系。在给定函数被多次调用的过程中，这些私有变量能够保持其持久性
    def closure(j):
        def func(a):
            return a + j
        return func
    func_list.append(closure(i))

for f in func_list:
    print(f(1))
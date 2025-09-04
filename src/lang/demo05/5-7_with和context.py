
"""
MyContext实现了__enter__和__exit__符合上下文管理器
"""
class MyContext(object):
    def __enter__(self):
        print('enter')
        return self
    def __exit__(self, type, value, traceback):
        print('exit')
    def show(self):
        print('show')

with MyContext() as ctx:
    ctx.show()
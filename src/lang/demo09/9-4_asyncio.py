import asyncio
from collections.abc import Generator, Coroutine


# @asyncio.coroutine
async def hello(name):
    print('hello', name)


c = hello('world')
print(isinstance(c, Coroutine))
print(isinstance(c, Generator))

'''
event_loop: 事件循环。asyncio中开启的一个无限的事件循环，asyncio会自动在满足条件时去调用响应的协程对象，我们只需要将协程对象注册到该事件循环上即可。
corotutine: 协程对象。指一个用async来定义的函数，它在调用时不会立即执行，而是返回一个协程对象。协程对象需要注册到事件循环，由事件循环进行调用。
future对象：代表将来执行或没有执行的任务的结果。它和我们下面要讲的task对象没有本质区别。
task对象：一个协程对象就是一个原生可以挂起的函数，而任务则是对协程的进一步封装，其中包含任务的各种状态。task对象是future对象的子类，它可以将corotutine和future联系在一起，
将coretutine封装为一个future对象。
async/await: python3.5之后用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口，其作用类似于yield。
'''

loop = asyncio.get_event_loop()
# task = loop.create_task(c)
task = asyncio.ensure_future(c)
loop.run_until_complete(task)
import asyncio

async def hello(x):
    # time.sleep(x) 是一个同步操作
    await asyncio.sleep(x)
    return '暂停了 {}秒'.format(x)


coro = hello(4)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coro)
loop.run_until_complete(task)
print(task.result())


def callback(future):
    print('第二种方式 {}'.format(future.result()))

coro1 = hello(5)
task1 = asyncio.ensure_future(coro1)
task1.add_done_callback(callback)
loop.run_until_complete(task1)

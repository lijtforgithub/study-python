import asyncio
import time


async def do_some_work(x):
    print('开始： ', x)
    await asyncio.sleep(x)
    print('结束： ', x)
    return '等待时间： {}'.format(x)

coro1 = do_some_work(1)
coro2 = do_some_work(2)
coro3 = do_some_work(3)


tasks = [asyncio.ensure_future(coro1), asyncio.ensure_future(coro2), asyncio.ensure_future(coro3)]

loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.gather(*tasks))

for task in tasks:
    print(task.result())
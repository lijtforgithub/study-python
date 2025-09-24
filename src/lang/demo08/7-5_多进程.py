# 多进程适用场景：对于计算密集型热内，比较适合多进程
# 多线程适用场景：适合IO密集型任务，比如文件读取以及爬虫等操作。
import multiprocessing
import os
import time


def func(p1, p2):
    print(f'当前进程={os.getpid()} 父进程={os.getppid()} p1={p1} p2={p2}')


class MyProcess(multiprocessing.Process):
    def run(self):
        print(f'当前进程={os.getpid()} 父进程={os.getppid()}')


if __name__ == '__main__':
    print(f'主进程={os.getpid()}')
    # 直接使用构造函数开启进程 必须放到main下
    proc1 = multiprocessing.Process(target=func, name='t1', args=('参数p1', '参数p2'))
    proc2 = multiprocessing.Process(target=func, name='t2', args=('', ''))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()
    time.sleep(5)

    proc3 = MyProcess()
    proc4 = MyProcess()
    proc3.start()
    proc4.start()
    proc3.join()
    proc4.join()



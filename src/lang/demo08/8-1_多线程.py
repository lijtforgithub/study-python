import sys
import threading
import time


def func(p1, p2):
    print(f'当前线程={threading.current_thread().name} p1={p1} p2={p2}')


# 直接使用构造函数开启线程
t1 = threading.Thread(target=func, name='t1', args=('参数p1', '参数p2'))
t2 = threading.Thread(target=func, name='t2', args=('', ''))

t1.start()
t2.start()

t1.join()
t2.join()
time.sleep(5)

exit_flag = 0


# 使用线程类继承开启线程
class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, delay):
        # threading.Thread.__init__(self)
        super().__init__()
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.thread_name)
        print_time(self.thread_name, self.delay, 5)
        print("退出线程：" + self.thread_name)


def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            sys.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
print(thread1.is_alive())

thread1.join()
thread2.join()
print("退出主线程")

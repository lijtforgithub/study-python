import sys
import threading
import time

exit_flag = 0


class myThread(threading.Thread):
    def __init__(self, thread_id, thread_name, delay):
        threading.Thread.__init__(self)
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
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
print(thread1.is_alive())

thread1.join()
thread2.join()
print("退出主线程")

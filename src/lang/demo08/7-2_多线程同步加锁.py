import threading

# GIL 全局解释器锁

num = 0
count = 100_0000
lock = threading.Lock()


def put():
    for i in range(count):
        global num
        lock.acquire()
        num += 1
        lock.release()


def get():
    for i in range(count):
        global num
        with lock:
            num -= 1


t1 = threading.Thread(target=put)
t2 = threading.Thread(target=get)
t1.start()
t2.start()

t1.join()
t2.join()

print(num)
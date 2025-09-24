import queue
import threading
import time

kind = ("豆腐", "豆沙", "猪肉", "青菜")


def product(q: queue.Queue):
    print("生产者生产包子开始")
    for i in range(4):
        time.sleep(0.5)
        q.put(kind[i % 4])
    time.sleep(0.5)
    print("生产者生产包子结束")


def consume(q: queue.Queue):
    while True:
        k = q.get()
        print(f"消费者消费一个 {k} 包")


q = queue.Queue()
t1 = threading.Thread(target=consume, args=(q,))
t2 = threading.Thread(target=product, args=(q,))
t3 = threading.Thread(target=product, args=(q,))

t1.start()
time.sleep(2)
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

import threading
import time


# threading.Barrier 类似JDK的栅栏 CyclicBarrier
# event = threading.Event

# 重置代码中的event对象 使得所有该event事件都处于待命状态
# event.clear()

# 阻塞线程 等待event指令
# event.wait()

# 发送event指令 使用所有设置该event事件的线程执行
# event.set()

class MyThread(threading.Thread):
    def __init__(self, event: threading.Event):
        super().__init__()
        self.event = event

    def run(self):
        print(f"线程{self.name} 已经准备完成，随时准备启动")
        self.event.wait()
        print(f"线程{self.name} 开始执行")


if __name__ == "__main__":
    event = threading.Event()
    threads = []
    [threads.append(MyThread(event)) for _ in range(1, 11)]

    event.clear()
    [t.start() for t in threads]
    time.sleep(5)
    event.set()
    [t.join() for t in threads]

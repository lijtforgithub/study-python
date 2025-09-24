import threading


class WoLong(threading.Thread):
    def __init__(self, name, cond: threading.Condition):
        threading.Thread.__init__(self, name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()

        print(f"{self.name} : 一支穿云箭")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 山无棱 天地合 乃敢与君绝")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 紫薇")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 是你")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 有钱吗，借点？")
        self.cond.notify()
        self.cond.release()


class FengChu(threading.Thread):
    def __init__(self, name, cond: threading.Condition):
        threading.Thread.__init__(self, name=name)
        self.cond = cond

    def run(self):
        self.cond.acquire()
        self.cond.wait()

        print(f"{self.name} : 千军万马来相见")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 海可枯 石可烂 激情永不散")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 尔康")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 是我")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name} : 滚")
        self.cond.release()


if __name__ == '__main__':
    condition = threading.Condition()
    wl = WoLong("卧龙", condition)
    fc = FengChu("凤雏", condition)

    fc.start()
    wl.start()

import threading

local_data = threading.local()
local_data.name = '主线程'


class MyThread(threading.Thread):
    def run(self):
        print(f"赋值前 {self.name} -> {local_data.__dict__}")
        local_data.name = '子线程'
        print(f"赋值后 {self.name} -> {local_data.name}")


print(local_data.name)
my_thread = MyThread()
my_thread.start()
my_thread.join()

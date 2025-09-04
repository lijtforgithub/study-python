import copy

class Cpu:
    pass
class Disk(object):
    pass
class Computer():
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

cpu = Cpu()
disk = Disk()
computer = Computer(cpu, disk)
print(computer, computer.cpu, computer.disk)

# 浅拷贝
computer2 = copy.copy(computer)
print(computer2, computer2.cpu, computer2.disk)

# 深拷贝
computer3 = copy.deepcopy(computer)
print(computer3, computer3.cpu, computer3.disk)
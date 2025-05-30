# 导入模块
from module import m1
import module.m2

m1.print1('模块导入')
module.m2.print2('模块导入')
print(m1.__name__)
m2 = module.m2.print2
m2('赋给一个本地的名称')

print()
import sys
print(sys.path)
print(dir(sys))
print(dir())

import module.using_name

print(__name__)
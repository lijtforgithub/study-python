# os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
# sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。
# time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。
# datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。
# random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
# math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。
# re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
# json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。
# urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。

# 操作系统接口
import os
current_dir = os.getcwd()
print("当前工作目录:", current_dir)
files = os.listdir(current_dir)
print("目录下的文件:", files)
print(dir(os))
# print(help(os))


import shutil
print(shutil.disk_usage(current_dir))
# shutil.copyfile('/Users/lijingtang/Downloads/python序列化', '/Users/lijingtang/Downloads/python1')
# shutil.move('/Users/lijingtang/Downloads/python序列化', '/Users/lijingtang/Downloads/python2')

# 文件通配符
import glob
print(glob.glob('*.py'))

# 命令行参数
import sys
print(sys.argv)
sys.stderr.write('红色一直在最后面\n')
# sys.exit()
print()

# 字符串正则匹配
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

# 数学
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

# random 提供了生成随机数的工具
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))
print()

# 访问互联网
from urllib.request import urlopen
for line in urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if '.百度' in line:  # look for Eastern Time
        print(line)

# 日期和时间
import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

current_date = datetime.date.today()
print(current_date)

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)

# 数据压缩 支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t).decode('utf-8'))
print(zlib.crc32(s))
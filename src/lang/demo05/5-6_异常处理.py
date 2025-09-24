import traceback

try:
    i = input('请输入')
    print(10 / int(i))
except:
    traceback.print_exc()
else:
    print('try-else')


# 自定义异常
class CustomerException(Exception):
    pass


try:
    raise CustomerException('自定义异常')
except CustomerException:
    traceback.print_exc()
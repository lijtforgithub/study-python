import traceback

try:
    i = input('请输入')
    print(10 / int(i))
except:
    traceback.print_exc()
else:
    print('try-else')

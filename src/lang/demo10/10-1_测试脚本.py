import itertools
import math
import os
import sys

# x = 0
# assert x

run_times = os.environ.get('RunCount', -1)
print(run_times)
run_times = 0 if run_times <= 0 else run_times
count = int(os.environ.get('Count', -1))
count = 50 if run_times <=0 else count
print(run_times, count)

sys.exit(0)

# 从列表中选取3个元素进行组合
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sum = 0
for i in range(1, 12):
    combinations = list(itertools.combinations(items, i))
    sum += len(combinations)
    print(combinations)
print(sum)

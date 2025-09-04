import itertools
import math

# 从列表中选取3个元素进行组合
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sum = 0
for i in range(1, 12):
    combinations = list(itertools.combinations(items, i))
    sum += len(combinations)
    print(combinations)
print(sum)

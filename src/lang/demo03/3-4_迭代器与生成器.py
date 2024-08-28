import sys

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))

for x in it:
    print(x, end=" ")
print("\n")

it1 = iter(list)
while True:
    try:
        print(next(it1))
    except StopIteration:
        sys.exit()

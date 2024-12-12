
from functools import reduce


def add(a, b):
    return a+b


l1 = [1, 2, 3, 4, 5, 6, 7]

x = reduce(add, l1)
print(x)

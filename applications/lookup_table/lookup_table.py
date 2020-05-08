import math
import random

cache = {}

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    v = math.pow(x, y)
    if v not in cache:
        cache[v] = math.factorial(v)
    v = cache[v]
    v //= (x + y)
    v %= 982451653

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


# import math
# ​
# cache = {}
# ​
# def build_lookup_table():
#     for i in range(1, 1000):
#         inv_square_root(i)
# ​
# def inv_square_root(n):
#     if n not in cache:
#         cache[n] = 1 / math.sqrt(n)
# ​
#     return cache[n]
# ​
# for i in range(1, 6):
#     print(inv_square_root(i))

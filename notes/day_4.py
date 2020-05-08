# applications of hash tables -> Important, likely what the sprint challenge is like

# dictionary or hash table you wrote

# what problems are hash table solving for us? -> find stuff FAST 
# data that you're trying to GET

# If you have a small number of elements, it doesn't matter (still 0(n))

# speed trade-offs

# cache's uses hash table to hash data -> network is slow

# memoization -> expensive calculation, do it once, save result

# Hash Table Applications
# =======================
# Speed of search
# ---------------
# Linear search through an array
# Network caching
# Memoization--expensive calculation
# Indexing
# --------
# Alice: 30
# Bob:   40
# Charlie: 20
# Dave: 20
# Beej: 20
# "Show me all the people who are age 30."
# What do I want to look up by?  <-- that's the key
# 30: [Alice]
# 40: [Bob]
# 20: [Charlie, Dave, Beej]
# Given a list of records, need to convert into a hashtable first O(n)
# THEN we can do quick lookups
# Removing Duplicates
# -------------------
# h = {}
# for i in data:
#     # Have we seen this data before?
#     if h[i]:     # same as checking for existence in the set
#         continue
#     # We've seen it now:
#     h[i] = True  # same as adding to a set
#     print(i)
# for i in data: O(n)
#     for j in data: O(n)
#         replace with hash table O(1)
# Counting Elements
# -----------------
# 1
# 5
# 5
# 7
# 9
# 2
# 3
# 9
# 5
# h = {}
# for i in data:
#     if i not in h:
#         h[i] = 1
#     else:
#         h[i] += 1
# Aside
# -----
# The key in a dict can be any immutable type, including tuples.
# h = {
#     (1,2): "value1",
#     (3,4,5): "value2"


# fib
# added cache
# cache = {}
# def fib(n):
#     if n <= 1:
#         return n 
    
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)

#     return cache[n]


# for i in range(10000):
#     print(fib(i))

# 100 -> 99th and 98th
# 99th -> 98th and 97th
# #cacheeee

# import math 

# # used apparently?

# cache = {}

# def inv_square_root(n):
#     if n not in cache:
#         cache[n] = 1 / math.sqrt(n)

#     return cache[n]

# for i in range(1,6):
#     print(inv_square_root(i))

# how to sort a dict

# by key
# d = {
#     "foo": 12,
#     "bar": 17,
#     "qux": 2
# }

# items = list(d.items())

# items.sort()

# print(items)

# by value

# d = {
#     "foo": 12,
#     "bar": 17,
#     "qux": 2
# }

# items = list(d.items())

# # 
# items.sort(key=lambda e: e[1])

# print(items)



# encode_table = {
#     'A': 'H', 'B': 'Z', 'C': 'Y', 'D': 'W', 'E': 'O', 'F': 'R', 'G': 'J',
#     'H': 'D', 'I': 'P', 'J': 'T', 'K': 'I', 'L': 'G', 'M': 'L', 'N': 'C',
#     'O': 'E', 'P': 'X', 'Q': 'K', 'R': 'U', 'S': 'N', 'T': 'F', 'U': 'A',
#     'V': 'M', 'W': 'B', 'X': 'Q', 'Y': 'V', 'Z': 'S'
# }
​
# decode_table = {}
# ​
# for k, v in encode_table.items():
#     decode_table[v] = k
# ​
# def encode(s):
#     r = ""
# ​
#     for c in s:
#         r += encode_table[c]
# ​
#     return r
# ​
# def decode(s):
#     r = ""
# ​
#     for c in s:
#         r += decode_table[c]
# ​
#     return r
# ​
# print(encode("ATTACKATDAWN"))
# ​
# print(decode("HZYW"))
# Collapse
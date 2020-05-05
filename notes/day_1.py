# don't worry about collisions today

["lorem", "ipsum", "dolor", "sit", "amet", "onsectetur"] 

# iterate, or call by index
# iterate => O(N)

# goal: input string -> return number (index?)
# f("lorem") -> 0

# encode allows us to get bytes of strings

# new_bytes = "maris".encode()
# for i in new_bytes:
#     print(i)

# 1. Get bytes for the key
# 2. Make up a function that returns an index for those bytes
#     * Adding the bytes
#     * Modding with the hash table size

hash_table_size = 10
#repeated list of None's
hash_table = [None] * hash_table_size

def my_hash(s):
    all_bytes = s.encode()
    total = 0

    for i in all_bytes:
        total += i

    return total

def hash_index(s):
    h = my_hash(s)

    return h % hash_table_size

def put(key, value):
    # get the index into the hash table list
    # calling hash index (which calls my_hash) func
    # key is str
    index = hash_index(key)
    # set the index (arr position) to passed value
    hash_table[index] = value 

def get(key):
    # hash value
    index = hash_index(key)
    return hash_table[index]
    # print 

def delete(key):
    index = hash_index(key)
    hash_table[index] = None 
# print(hash_index("mauricio"))
# print(hash_index("maris"))

print('hash_table:', hash_table)
put("Alyssa", 37)
print('hash_table:', hash_table)
# print(get("Alyssa"))
# print(get("mau"))
delete("Alyssa")
print("hash table:", hash_table)
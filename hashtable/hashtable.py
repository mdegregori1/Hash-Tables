class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity 
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            # No node at the index? Create one
            self.storage[index] = HashTableEntry(key, value)
        else:
            # storage contains a node
            # node = head, previous -> None
            node = self.storage[index]
            previous = None
            # must loop
            while True:
                # if node present, but only cointains None (no key), then set new key at head and return
                if node is None: 
                    previous.next = HashTableEntry(key, value)
                    return 
                elif node.key == key:
                    # if keys match, then replace
                    node.value = value
                    return
                elif node is not None and node.key != key:
                    # if node has a value and the keys aren't equal, then string to old node
                    previous = node
                    node = node.next


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        if self.storage[index] is None:
            print(f'{key} was not found')
            return None
        else:
            node = self.storage[index]
            previous = None
            # if there is a node with value none, then its already deleted
            while node is not None:
                if node.key == key:
                    node.value = None
                if previous:
                    previous.next = None
                    return
                elif not previous or node.key != key:
                    previous = node
                    node = node.next
     


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            print(f'{key} was not found')
            return None
        else:
            node = self.storage[index]
            # if node has val none, then it's useless to return None value
            while node is not None:
                if node.key == key:
                    # if key, then return
                    return node.value
                else:
                    # else, search for next node
                    node = node.next
 


   
    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        prev_storage = self.storage
        self.storage = [None] * self.capacity * 2

        for i in range(len(prev_storage)):
            node = prev_storage[i]

            while node is not None:
                self.put(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

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
            # storage is not empty
            # must check is storage contains key, or not
            # set previous because linkedlist
            node = self.storage[index]
            previous = None
            if node is not None and node.key == key:
                    # linked list isn't empty and keys are equal
                    # replace values
                node.value = value
                return
                    # if key is not found, create a node with that key in current node
            elif node is not None and node.key != key:
                previous.next = HashTableEntry(key, value)
                return

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
            # if node with key exists, change its value to none
            if node.key == key: 
                node.value = None 


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
            if node.key == key:
                return node.value
            else:
                node = node.next

   
    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        old_storage = self.storage
        self.storage = [None] * self.capacity * 2
        # for value in old_storage:
        for i in range(len(old_storage)):
            node = old_storage[i]

            if node is not None:
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

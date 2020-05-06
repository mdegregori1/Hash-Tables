'''
 Ways to deal with collision:

 linked list
 open addressing -> general class o collision resolution : Linear Probing

 "foo" hashes to index 1
 "bar" hashes to index 2 < 
 "baz" hashes to index 2 <

 put("foo", 12)
 put("bar, 30)
 put("baz, 99)

    0   1    2   3
 [None, ("foo",12), ("bar", 30), (try to put 99 here, which was None)]



NOTE: will have to resize. otherwise, heavier inputs really slow things down.  

Something that is not none and something that isn't deleted in place during linear probing -> how to mark it as deleted? (None, 30)

Put: Scan forward from the hash value until we find eitehr the key, or None
If we find a deleted slot along the way, keep it it mind 
put the value there 

Get: Scan forward from the hash index until we find either the key, or None
Return that 

Delete: Scan forward from the has index until we find either the key, or None

If we find the key, mark it as deleted
'''


# Chaining 
'''
Collisio Resolution By Chaining 

Each slot of the hash table holds a linked list 
Collisions are handled by adding multiple items to the same linked list 

Slot Index  Chain
---------   ------
0 --------> None
1
2        -> ("bar", 30) -> ("baz", 999)
3

Put:

Search the list for the key
If it's there, replace the value
If it's not, append a new record to the list 

Get: 
Find the hash index
Search the list for the key
If found, return the value 
Else return None

Delete:
Find the hash index
Search the list for the key
If found, delete the node from the list
Else return none 
'''

# Linked Lists Refresher 
'''
(1) -> (2) -> (3) -> None
^
head


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = None (at the beginning, empty linked list)

Insert (at head)
Append (at tail)
Find
Delete

(99)->(1) -> (2) -> (3) -> None
^
head
(99 being inserted)

def insert_at_head(value):
    n = Node(value)
    n.next = head
    head = n 

    return n 

def find(value):
    cur = head

    while cur is not None:
        if cur.value == value:
            return value
        
        cur cur.next

    return None 


def append_at_tail(value):
    n = Node(value)
    cur = head

    while cur.next is not None:
        cur = cur.next
    
    cur.next = n
    
'''
'''
Perfect hashing 

0 -> D
1 -> H
2 -> A -> I
3 -> C -> J
4 -> G
5 -> B
6 -> E

The more stuff added, the worse the performance.

Load Factor: 

number of elements in the list // number of slots 

(counter// len)
'''
# part 1 of assignment -> keep track of the load factor
# 

When you double the length, you must rehash 

Old Table

0 -> D
1 -> H
2 -> A -> I
3 -> C -> J
4 -> G
5 -> B
6 -> E

New Table 
0
1
2
3
4
5
6
7
8
9
10
11
12

Resize

Step 1: Make a new, bigger table/array 
Step 2: Go through all of the old elements, and hash into the new list


Rules:
- If you resize bigger, double the size
- If you resize smaller, halve the size

Automatic Resizing:

Put -> Check -> whenever it grows
If the load > 0.7:
double the size of the hashtable

Delete -> Check -> whenever you delete
If the load < 0.2:
if size > minimum (8)
halve the size of the hashtable down to some minimum at most 




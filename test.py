# print('testing shell')

# add up and print the sum of the all of the minimum elements of each inner array:
# ```
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# ```

# pass in the whole array of arrays in a function 
# have access to each index in the list, each index being a sub-list
# loop through the indeces of an indiviual index
# conditional statement, where you print out the max in that sub-array

# def min_sum(array_1):
#     for a in array_1:
#         for b in a:
#         # b is index of subarr
#             if min(b):
#                 print(b)
#     print sum(b)

# array_1 = [8, 3, 2, 5, 1, 9, 12]
# # find max of arr
# print(max(array_1))
        
# array_1 = [8, 3, 2, 5, 1, 9, 12]
# # find sum of arr
# print(sum(array_1))





# def test_problem(array_1):
#     total_sum = 1
#     for x in array_1:
#         for y in x:
#             if max(x):
#                 total_sum += y

# array_1 = [[1,2], [3, 4], [5, 6], [7,8]]
#expected result = 6
def find_min(array_1):
    total = 0
    for i in array_1:
        min_val = min(i)
        total += min_val
        print(total)
        
array_1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
find_min(array_1)





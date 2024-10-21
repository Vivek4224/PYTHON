"""
Write a Python function that takes a list and returns a new list with unique
elements of the first list.
"""

original_list = [1,2,2,3,3,3,4,5,66,6,6,7,8,9]
unique_list = list(set(original_list))

print("original_list: ", original_list)
print("unique_list: ", unique_list)
"""
Write a Python program to remove an empty tuple(s) from a list of tuples.
"""

tuples_list = [(1,2), (), (3,4), (), (5,6), (), (7,8)]


for tuple in tuples_list:
    if not tuple:
        tuples_list.remove(tuple)


print("Original list of tuples:", tuples_list)

"""
Write a Python program to unzip a list of tuples into individual lists.
"""

zip_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

list1 = []
list2 = []

for item in zip_list:
    list1.append(item[0])
    list2.append(item[1])

print(list1)
print(list2)
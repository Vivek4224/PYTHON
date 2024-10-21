"""
Write a Python program to remove duplicates from a list.
"""

list = ["a","b","a"]
unique_list = []

for items in list:
    if items not in unique_list:
        unique_list.append(items)
print(unique_list)
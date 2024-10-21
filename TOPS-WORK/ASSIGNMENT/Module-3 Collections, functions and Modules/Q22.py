"""
Write a Python program to check whether an element exists within a
tuple.
"""

items = (10,60,40,50,80)

check_items = 60

if check_items in items:
    print(f"{check_items} exists in the tuple")
else:
    print(f"{check_items} does not exist in the tuple")
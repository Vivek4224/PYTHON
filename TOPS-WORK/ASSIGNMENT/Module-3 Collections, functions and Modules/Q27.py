"""
Write a Python program to find the repeated items of a tuple
"""

items = (10,20,30,20,40,50,30)

repeated_items = {}

for item in items:
    if item in repeated_items:
        repeated_items[item] += 1
    else:
        repeated_items[item] = 1
    
print("Repeated items in the tuple:", repeated_items)

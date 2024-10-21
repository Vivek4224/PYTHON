"""
Write a Python program to replace last value of tuples in a list.
"""

og_tuple = ((1,2),(3,4),(5,6))
new_value = 3
update_tuple = []

for og in og_tuple:
    tuple_list = list(og)
    tuple_list[-1] = new_value
    update_tuple.append(tuple(tuple_list))

print("og tuple is ", og_tuple)
print("Updated tuple is ", update_tuple)

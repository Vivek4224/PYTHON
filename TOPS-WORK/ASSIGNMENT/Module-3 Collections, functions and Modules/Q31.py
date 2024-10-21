"""
How will you create a dictionary using tuples in python?
"""

tuples_list = [('name', 'vivek'), ('age', 21)]

my_dict = {}

for key, value in tuples_list:
    my_dict[key] = value  

print("Dictionary:", my_dict)

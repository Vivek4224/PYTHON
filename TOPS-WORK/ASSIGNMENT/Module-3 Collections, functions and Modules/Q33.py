"""
Write a Python script to concatenate following dictionaries to create a
new one.
"""

dict1 = {'name': 'vivek', 'age': 21}
dict2 = {'city': 'surat', 'country': 'india'}

updated_dict = {}

for item in dict1, dict2:
    updated_dict.update(item)

print(updated_dict)
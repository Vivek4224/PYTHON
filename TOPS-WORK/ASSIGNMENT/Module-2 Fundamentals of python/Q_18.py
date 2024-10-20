"""
 Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.
"""

input_str = input("Enter a string: ")

if len(input_str) < 3:
    result = input_str
elif input_str.endswith('ing'):
    result = input_str + 'ly'
else:
    result = input_str + 'ing'

print(result)

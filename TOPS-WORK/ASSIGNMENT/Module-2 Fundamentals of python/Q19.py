"""
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""

input_string = input("Enter a string: ")

poor_index = input_string.find('poor')
not_index = input_string.find('not')

if poor_index != -1 and not_index != -1 and not_index > poor_index:
    result = input_string[:poor_index] + 'good' + input_string[not_index + 3:]
else:
    result = input_string

print(result)

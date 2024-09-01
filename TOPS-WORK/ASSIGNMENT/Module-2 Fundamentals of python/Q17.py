"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string
"""

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) >= 2:
    swapped_string1 = string1[1] + string1[0] + string1[2:]
else:
    swapped_string1 = string1  

if len(string2) >= 2:
    swapped_string2 = string2[1] + string2[0] + string2[2:]
else:
    swapped_string2 = string2  

result = swapped_string1 + ' ' + swapped_string2

print(result)


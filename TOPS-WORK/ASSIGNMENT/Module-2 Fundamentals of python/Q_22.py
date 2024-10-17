"""
Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.
"""

str = input("Enter a string:- ")

if len(str) < 2:
    result = ""
else:
    first_char = str[:2]
    lastr_char = str[-2:]
    result=first_char + lastr_char

print("Result: ",result)
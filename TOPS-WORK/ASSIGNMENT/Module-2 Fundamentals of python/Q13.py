"""
Write a Python program to count the number of characters (character
frequency) in a string
"""
string = input("Enter a string: ")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char in frequency:
    freq = frequency[char]
    print(f"'{char}': {freq}")



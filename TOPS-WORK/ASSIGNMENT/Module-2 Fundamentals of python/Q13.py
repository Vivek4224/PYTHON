"""
Write a Python program to count the number of characters (character
frequency) in a string
"""
user_string = input("Enter a string: ")
char_frequency = {}

for char in user_string:
    char_frequency[char] = char_frequency.get(char, 0) + 1

for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")

"""
Write a Python program to test whether a passed letter is a vowel or
not.
"""

letter = input("Enter a letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Invalid input. Please enter a single letter.")
else:
    vowels = 'aeiou'
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")


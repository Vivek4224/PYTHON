"""
Write a Python program to find the second smallest number in a list.
"""

number = [3,4,6,8,3,4,9]

unique_number = list(set(number))

unique_number.sort()

if len(unique_number) >= 2:
    second_small_num = unique_number[1]
    print("Second smallest number is:", second_small_num)
else:
    print("The list has less than 2 unique numbers.")
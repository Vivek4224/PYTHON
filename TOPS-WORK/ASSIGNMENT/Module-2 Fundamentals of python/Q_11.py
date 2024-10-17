"""
Write a python program to sum of the first n positive integers.
"""
num = int(input("Please enter a num:- "))
sum = 0

for i in range(1, num + 1):
    sum += i

print(f"the {num} of sum is {sum}")


"""
Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.
"""

num1 = int(input("Please Enter a num 1:- "))
num2 = int(input("Please Enter a num 2:- "))
num3 = int(input("Please Enter a num 3:- "))

if (num1 == num2) or (num1 == num3) or (num2 == num3):
    total = 0
    print(f"Total = {total}")
else:
    total = num1 + num2 + num3
    print(f"{num1} and {num2} and {num3} Total is {total}")
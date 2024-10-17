"""
• Write a Python program to get the Factorial number of given number.
"""

num = (int(input("Please Enter Number:- ")))

if num <= 0:
    print("Invalid Number")
else:
    factNum = 1
    for i in range(1,num+1):
        factNum *= i
    print(f"The Factorial of {num} is {factNum} ")

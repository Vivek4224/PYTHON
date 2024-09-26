"""
Writte a Python program to check if number is even or odd.
"""

usr_num = int(input("please enter a number:- "))

if (usr_num % 2) != 0:
    print(f"The {usr_num} is even.")
elif (usr_num) <= 0:
    print(f"The {usr_num} number zero.")
else:
    print(f"The {usr_num} is odd.")
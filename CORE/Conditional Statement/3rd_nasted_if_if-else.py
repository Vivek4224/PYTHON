"""
syntax:
if condition1:
    if condition2:
        # block of code

if condition1:
    if condition2:
        # block of code
    else:
        # block of code
else:
    # code of block

"""
"""
age=int(input("Enter your age"))

if age >= 18:
    weight=float(input("Enter Your Weight"))
    if weight >= 50:
        print("You can blood donate")
    else:
        print("you can't blood donate")    
else:
    print("You can't donate blood")
"""

value=int(input("please enter a number"))

if value>=1500 and value<=2700:
    if value%5==0 and value%7==0:
        print("your reminder is 0.") 
    else:
        print("your reminder is not 0.")
else:
    print("you are not enter valid value")
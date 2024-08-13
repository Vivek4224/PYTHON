"""
syntax:
if condition-1:
    # code of block execute if condition-1 is True
elif condition-2:
    # code of block execute if condition-2 is True
elif condition-3:
    # code of block execute if condition-3 is True
    .
    .
    .
else:
    # code of block execute if condition-1, condition-2, condition-3 is False  

"""

score=float(input("please enter a score"))

if score >=0 and score <=100:
    if score>=80:
        print("briliant") 
    elif score >= 50:
        print("good")
    elif score >= 30:
        print("average")
    elif score >=20:
        print("you are fool")
else:
    print("invalid score")
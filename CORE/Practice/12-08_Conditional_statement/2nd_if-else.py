"""
syntax:

if condition:
    # code of block execute if condition is True
else:
    # code of block execute if condition is False
"""

bal=10000
wb=45000

if wb<=bal:
    print("you can withdraw")
    print("withdraw successfully.")
    print("available balance is ",bal-wb)
else : 
    print("you can't withdraw")
"""
syntax:

for var in itrable_var/squence:
    # block of code
"""
"""
# task 2

for num in range(1,11):
    print(num)
"""

"""
# task 2

for num in range(1,11,2):
    print(num)

for num in range (1,11):
    if num%2==0:
        print(num,"Even")
    else:
        print(num,"odd")
"""

"""
# task 3

for num in range(1, 6):
    print("*", end=' ')
    print("*", end=' ')
    print("*", end=' ')
    print("*", end=' ')
    print("*", end=' ')
    print("\n")
"""

"""
num = 5
for row in range(1, num + 1):
    for col in range(1, num + 1):
        print("*", end=' ')
    print()
"""

"""
num = 5
for row in range(1, num + 1):
    for col in range(1, row + 1):
        print("*", end=' ')
    print()
"""

"""
num = 5
for row in range(1, num + 1):
    for col in range(1, row + 1):
        print("*", end=' ')
    print()

for row in range(1, num + 1):
    for col in range(num-row, 0, -1):
        print("*", end=' ')
    print()
"""

"""
num=5
for row in range(1,num+1):
    for col in range(num-row,0,-1):
        print(" ",end=' ')
    for col in range(1,row+1):
        print("*",end=' ')
    print()    
"""

"""
num=5
for row in range(1,num+1):
    for col in range(1,row):
        print(" ",end=' ')
    for col in range(num-row+1,0,-1):
        print("*",end=' ')
    print()       
"""

"""
num=5
for row in range(1,num+1):
    for col in range(num-row,0,-1):
        print(" ",end=' ')
    for col in range(1,row+1):
        print("*",end=' ')
    print()    
for row in range(1, num + 1):
    for col in range(1, row+1):
        print(" ", end=' ')
    for col in range(num-row, 0, -1):
        print("*", end=' ')
    print()
"""

"""
num = 5
for row in range(1, num + 1):
    for col in range(num-row, 0, -1):
        print(" ", end=' ')
    for col in range(1, row + 1):
        print("*", end=' ')
    for col in range(1, row):
        print("*", end=' ')
    print()
for row in range(1, num + 1):
    for col in range(1, row+1):
        print(" ", end=' ')
    for col in range(num-row, 0, -1):
        print("*", end=' ')
    for col in range(num-row-1, 0, -1):
        print("*", end=' ')
    print()
"""    
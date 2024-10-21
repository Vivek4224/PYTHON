"""
Write a Python program to check whether a list contains a sub list
"""

main_list = [1,2,3,[4,5,6],7,9]
sublist = [4,5,6]

check_list = str(sublist) in str(main_list)

if check_list:
    print("Sublist found in main list")
else:
    print("Sublist not found in main list")
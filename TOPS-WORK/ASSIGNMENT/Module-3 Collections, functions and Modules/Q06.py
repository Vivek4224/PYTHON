"""
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings
"""

string_list = ["Vivek","AA","a","bar","cc","anna"]
count = 0

for str in string_list:
    if len(str) >= 2 and str[0] == str[-1]:
        count += 1

print("same characters", count)


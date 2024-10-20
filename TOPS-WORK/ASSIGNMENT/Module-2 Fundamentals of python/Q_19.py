"""
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""

inp=input("Enter a string:")
not_char=inp.find("not")
poor_char=inp.find("poor")

if not_char!=-1 and poor_char != -1 and not_char<poor_char:
    if not_char < poor_char:
        res= inp[:not_char] + 'good' + inp[poor_char + len('poor'):]
else:
    res=inp
print(res)






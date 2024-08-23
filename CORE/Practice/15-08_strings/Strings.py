"""
What is string in python?
=====================================
A string in Python is a sequence of characters, such as a word or a phrase. Strings are immutable, meaning they cannot be changed after they are created.

પાયથોનમાં સ્ટ્રિંગ એ અક્ષરોનો ક્રમ છે, જેમ કે શબ્દ અથવા શબ્દસમૂહ. સ્ટ્રીંગ્સ અપરિવર્તનશીલ હોય છે, એટલે કે તે બનાવ્યા પછી બદલી શકાતી નથી.

including in string: a-z, A-Z, 0-9, special symbols.

syntax:
str_name = ''
str_name = ""
str_name = ''''''
"""

# str_name=''
# print(type(str_name))

# str_name=""
# print(type(str_name))

# str_name=''' '''
# print(type(str_name))

# str_name=""" """
# print(type(str_name))

# name="TOps Technology Pvt. Ltd."

# print(len(name))

# Access a string

# access full string

# print(name)

# Indexing [+/-]

# print(name[0])
# print(name[-4])
# print(name[5])

# Slicing [+/-]

# syntax: obj_name[start:end+1:step+1]
# print(name[0:5])
# print(name[0:8:3])
# print(name[::-1])
# print(name[::-1][20:])
# print(name[-4:-13:-1])

"Your OTP : 2463"

book="Java"
price=2000
pages=2500

# print("the name of book is java.price is 2000 and pages is 2500.")
# print(f"the name of book is {book}.price is {price} and pages is {pages}.")
# print("the name of book is {2}.price is {1} and pages is {0}".format(book,price,pages))
# print("the name of book is {}.price is {} and pages is {}".format(book,price,pages))

# print("my name is "vivek barvaliya"")
# print("my name is 'vivek barvaliya'")
# print('my name is "vivek barvaliya"')
# print("my name is \"vivekbarvaliya\"")
# print('my name is \'vivekbarvaliya\'')

# print("\\\\")
# print("\"")
# print("\'")
# print("\n")
# print("\t")
# print("\b")

# print("vivek \\ barvaliya")
# print("vivek b\\arvaliya")

# company="   tops TChnoLogy  pvT.   LtD. "

# print(dir(company))
# print(company.lower())
# print(company.upper())
# print(company.swapcase())
# print(company.title())
# print(company.capitalize())
# print(company.lstrip())
# print(company.rstrip())
# print(company.strip())
# print(company.title().strip().replace("  ", " ").replace("  ", " "))

# code = "python"
# print(code.center(19,"@"))

# print(code.startswith("p"))
# print(code.startswith("P"))
# print(code.endswith("ON"))
# print(code.endswith("on"))

# password = "Tops@123"
# upr = False
# m_upr = True
# lwr = False
# m_lwr = True
# sc = False
# m_sc = True
# di = False
# m_di = True

# if len(password >= 8):
#     for ch in password:
#         # print(ch)
#         if ch.isupper():
#             upr = True
#         else:
#             if m_upr:
#                 print("Atleast only one char must be upper case.")
#                 m_upr = False
#         if ch.islower():
#             lwr = True
#         else:
#             if m_lwr:
#                 print("Atleast only one char must be lower case.")
#                 m_lwr = False
#         if not ch.isalnum():
#             sc = True
#         else:
#             if m_sc:
#                 print("Atleast one special char must be there.")
#                 m_sc = False
#         if ch.isdigit():
#             di = True
#         else:
#             if m_di:
#                 print("Atleast only one digit must be there.")
#                 m_di = False

# if upr and lwr and sc and di:
#     print("Strong Password")
# else:
#     print("Weak Password")

# password = "ACcVxss@123"
# upr = False
# m_upr = True
# lwr = False
# m_lwr = True
# sc=False
# m_sc=True
# di=False
# m_di=True

# if len(password)>=8:
#     for ch in password:
#         if ch.isupper():
#             upr = True
#             m_upr = False  
#             continue
#         else:
#             if m_upr:
#                 print("At least one char must be upper case.")
#                 m_upr = False  

#         if ch.islower():
#             lwr = True
#             m_lwr = False 
#             continue
#         else:
        
#             if m_lwr:
#                 print("At least one char must be lower case.")
#                 m_lwr = False 

#         if not ch.isalnum():
#             sc=True
#             m_sc=False
#             continue
#         else:
#             if m_sc:
#                 print("At least one special charachter must be in password.")
#                 m_sc=False

#         if ch.isdigit():
#             di=True
#             m_di=False
#             continue
#         else:
#             if m_di:
#                 print("Print atleast one digit must be in password.")
#                 m_di=False

#     if upr and lwr  and sc and di:
#         print("Strong Password")
#     else:
#         print("Weak Password")
# else:
#     print("Password is min. 8 char")

# fname="Vivek"
# lname="Barvaliya"
# print(fname+" "+lname)

# name="Tops"*3
# print(name)

# star = "*"*1
# print(star)
# star = "*"*2
# print(star)
# star = "*"*3
# print(star)
# star = "*"*4
# print(star)
# star = "*"*5
# print(star)

# num = 5
# for row in range(1, num+1):
#     print(" "*(num-row), row*" *")

# num = 5
# for row in range(1, num+1):
#     print(" "*(num-row), row*" *")

name = "tOps technOlogiEs pvt. ltd.".lower()

vowels = "aeiou"
conso_count = 0
special_symbols = 0
for ch in name:
    if ch not in vowels:
        if ch.isalpha():
            conso_count += 1
        
        if not ch.isalnum():
            special_symbols += 1
print(conso_count)
print(special_symbols)
print(len(name) - conso_count - special_symbols)
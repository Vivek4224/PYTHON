name = input("Please Enter a any word:-")
str_char = 0
str_digit = 0
str_sc = 0
str_upr = 0
str_lwr = 0
str_space = 0
str_tab = 0
str_newLine = 0

# count the words of the given string.
strlist=name.split()
print("Word is", len(strlist))

# count the char of the given string
for str in name:
    if not str.isspace():
        str_char += 1
print("Character is",str_char)

# count the digits of the given string
for str in name:
    if str.isnumeric():
        str_digit += 1
print("Number is",str_digit)

# count the special characters of the given string
for str in name:
    if not str.isalnum() and not str.isspace() :
        str_sc += 1
print("Special Character is",str_sc)

# count the upper case letters of the given string
for str in name:
    if str.isupper():
        str_upr += 1
print("Upper Case is",str_upr)

# count the lower case letters of the given string
for str in name:
    if str.islower():
        str_lwr += 1
print("Lower Case is",str_lwr)

# count the spaces of the given string
for str in name:
    if str.isspace():
        str_space += 1
print("Space is",str_space)

# count the tabs of the given string
for str in name:
    if str == '\t':
        str_tab += 1
print("Tab is",str_tab)

# count the new line of the given string
for str in name:
    if str == '\n':
        str_newLine += 1
print("New Line is",str_newLine)

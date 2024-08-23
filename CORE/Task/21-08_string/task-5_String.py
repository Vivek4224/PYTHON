input_string = "VIVEK Barvaliya"
lwr_case = ""
upr_case=""
swap_case=""

# convert given string to lower case 
for char in input_string:
    ascii_value = ord(char)
    if 'A' <= char <= 'Z':
        lwr_char = chr(ascii_value + 32)
        lwr_case += lwr_char
    else:
        lwr_case += char
print("lower case is :-",lwr_case)

# convert given string to upper case
for char in input_string:
    ascii_value = ord(char)
    if 'a' <= char <= 'z':
        upr_char = chr(ascii_value - 32)
        upr_case += upr_char
    else:
        upr_case += char
print("Upper case is :-",upr_case)

# convert given string to swap case
for char in input_string:
    ascii_value = ord(char)
    if 'a' <= char <= 'z':
        swap_char = chr(ascii_value - 32)
        swap_case += swap_char
    elif 'A' <= char <= 'Z':
        swap_char = chr(ascii_value + 32)
        swap_case += swap_char
    else:
        swap_case += char    
print("Swap case is :-",swap_case)

# convert given string to title case


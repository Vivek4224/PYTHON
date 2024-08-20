password = ("Vi@1ekek")

# input("please enter password:")

is_first=True
upr=False
m_upr=True
is_second=True
lwr=False
m_lwr=True
is_third=True
sc=False
m_sc=True
is_four=True
digit=False
m_digit=True

if len(password) >= 8 and len(password) <= 10:
    for ch in password:
        if is_first:
            if ch.isupper():
                upr=True
                is_first=False
                continue
            else:
                if m_upr:
                    print("Atleset one upper case use in passsword ")
                    m_upr=False
        if is_second:
            if ch.islower():
                lwr=True
                is_second=False
                continue
            else:
                if m_lwr:
                    print("Atleset one lower case use in passsword ")
                    m_lwr=False
        if is_third:
            if not ch.isalnum():
                sc=True
                is_third=False
                continue
            else:
                if m_sc:
                    print("Atleast add one special charactert")
                    m_sc=False
        if is_four:
            if ch.isdigit():
                digit=True
                is_four=False
                continue
            else:
                if m_digit:
                    print("Atleast add one number")
                    m_digit=False
    if upr and lwr and sc and digit:
        print("password is strong")
    else:
        print("weak password")
else:
    print("8 to 10 ch must")
                

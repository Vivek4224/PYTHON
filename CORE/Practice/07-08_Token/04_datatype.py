"""
1. What is datatype ?
ans: A datatype is a classification that specifies which type of value a variable can hold and what operations can be performed on it. Python supports various built-in datatypes, including: 

ડેટાટાઈપ એ એક classification છે જે સ્પષ્ટ કરે છે કે વેરીએબલ કયા પ્રકારનું મૂલ્ય ધરાવે છે અને તેના પર કઈ કામગીરી કરી શકાય છે. પાયથોન વિવિધ બિલ્ટ-ઇન ડેટાટાઇપ્સને સપોર્ટ કરે છે, જેમાં નીચેનાનો સમાવેશ થાય છે:

                            Datatype
                                |
              ------------------------------------                           
              |                                  |
           prmitive                       non-primitive
       -----------------           ----------------------------
       |               |           |             |            |
Numeric-types    Boolean-type Sequence-types Mapping-type Set-types
 -------------         -       ----------        -            -
 |    |      |         |       |   |    |        |            |
int float complex     bool    str list tuple    dict         set

# Binary Types:

# bytes: Immutable sequences of bytes.
# bytearray: Mutable sequences of bytes.
# memoryview: A view object that exposes the buffer interface.

"""

age=21
print(type(age)) # <class 'int'>

price=21.21
print(type(price)) # <class 'float'>

real_img=32+32j
print(type(real_img)) # <class 'complex'>

is_active=True
print(type(is_active)) # <class 'bool'>

name="vivek"
print(type(name)) # <class 'str'>

names=['vivek','jatin','uttam','shrey','seenu']
print(type(names)) # <class 'list'>

nums=(1,2,3,4)
print(type(nums)) # <class 'tuple'>

car = {
    "brand":"BMW",
    "price":"1cr"
}
print(type(car)) # <class 'dic'>


ch={'a','b','c'}
print(type(ch)) # <class 'set'>

# khali brackets ma default tarike 'dic' type re chhe
Ch = {}
print(type(Ch)) # <class 'dic'>

"""
TYPE CONVERSION
int() - converts to integer
float() - converts to float
complex() - converts to complex number
...
"""

# Implicit coversion
# num1=10
# num2=10.5
# num3=num1+num2
# print(num3)

# Explicit coversion
num1=10
num2=10.5
num3=int(num2)
print(type(num3))

# name="vivek"
# i=int(name) # ValueError: invalid literal for int() with base 10: 'vivek'
# print(type(i))

nums1="220803"
print(type(int(nums1))) # 220803 <class 'int'>




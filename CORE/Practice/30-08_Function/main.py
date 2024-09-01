"""
syntax:

def function_name(para1, para2, ...paraN):
    block of code

function call
function_name(value1, value2, ...valueN)

"""

# a = 10
# b = 20
# c = a + b
# print(c)

# def addition(a,b):
#     print(a+b)

# addition(10,20)
# addition(500,10000)

# def add(a,b):
#     return a+b

# print(add(200,400))

"""
Type Of paras

1] Positional para
2] Default/keyword Para
3] Variable length para
    - *args
    - **kwargs
"""

# # 1] Positional para
# def add(a, b, c):
#     print(a+b+c)

# add(10,20,50)

# # 2] Defaul / keyword para
# def bill(tomato,potato=50):
#     print("Tomato Price is",tomato)
#     print("potato price is",potato)
#     print("total amount:",tomato+potato)

# bill(30)

# 3] Variable length para

## sir ne puchhvanu

    # - *args
    # - **kwargs
# def add(*nums):
#     print(sum(nums))
#     # print(type(nums))

# add(1,2,3,4, 100, 1000)

# def bill(**products):
#     # print(type(products))
#     total = 0
#     for key, value in products.items():
#         print(f"{key} price is: {value}")
#         total += value

#     print("Total amount is: ", total)

# bill(pen=10, book= 200, tomato=30, iceCream=20)

# a = 10

# def test():
#     global a
#     a = 20 
#     print(a)

# test()
# print(a)

# def upper_case(func):
#     def wrapper():
#         res = func().upper()
#         print(res)
#         return res
#     return wrapper

# def capitalize_case(func):
#     def wrapper():
#         res = func().capitalize()
#         print(res)
#         return res
#     return wrapper

## sir ne puchhvanu

# @capitalize_case
# @upper_case
# def text():
#     return input("Enter something: ")

# text()

## sir ne puchhvanu

# test = lambda num1, num2:num1*num2
# print(test(10, 20))

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x*x, nums)))
# print(list(filter(lambda x:x%2==0, nums)))
# print(list(filter(lambda x:x%2!=0, nums)))
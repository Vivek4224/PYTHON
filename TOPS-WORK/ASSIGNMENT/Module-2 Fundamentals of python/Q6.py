"""
Write python program that swap two number with temp variable and
without temp variable.
"""

# Program to swap two numbers using a temp variable

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("First number:", a)
print("Second number:", b)


# Program to swap two numbers without using a temp variable

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("First number:", a)
print("Second number:", b)

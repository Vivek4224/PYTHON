"""
Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
"""

squares = []

for i in range(1,31):
    squares.append(i**2)

print("first 5 elements",squares[:5])
print("last 5 elements",squares[-5:])
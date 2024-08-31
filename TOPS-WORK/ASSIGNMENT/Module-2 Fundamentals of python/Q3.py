"""
Write a Python program to get the Fibonacci series of given range.
"""


num = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1

for i in range(num):
    print(a, end=" ")
    a, b = b, a + b



"""
Write a Python function to reverses a string if its length is a multiple of
4.
"""

def reverse_if_multiple_of_four(str):
    if len(str) % 4 == 0:
        return str[::-1]
    else:
        return str

input_string = input("Enter a string: ")

result = reverse_if_multiple_of_four(input_string)

print("Result:", result)

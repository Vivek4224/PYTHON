"""
Write a Python function to get the largest number, smallest num and sum
of all from a list.
"""

def num(numbers):
    if not numbers:
        return None, None, 0
    else:
        largest = numbers[0]
        small = numbers[0]
        total = numbers[0]
        
        for i in numbers:
            if i > largest:
                largest = i
            if i < small:
                small = i
            total += i

    return largest, small, total

list = [1,23,36,4,5895,546,50000]
largest, small,total = num(list) 
print("largets number", largest)
print("small number", small)
print("total number", total)

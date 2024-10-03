"""
Write a Python function that takes a list of words and returns the length
of the longest one.
"""

def longest_word_len(words):
    longest_len = 0  
    for word in words:
        if len(word) > longest_len:  
            longest_len = len(word) 
    return longest_len  

list = ["apple", "banana", "cherry", "date"]
length = longest_word_len(list)
print(f"The length of the longest word is: {length}")


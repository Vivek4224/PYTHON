"""
Write a Python function that takes a list of words and returns the length
of the longest one.
"""

def length_of_longest_word(words):
    if not words:
        return 0
    
    lengths = [len(word) for word in words]
    
    return max(lengths)

if __name__ == "__main__":
    words_list = ["apple", "banan", "cherr", "date"]
    print("The length of the longest word is:", length_of_longest_word(words_list))

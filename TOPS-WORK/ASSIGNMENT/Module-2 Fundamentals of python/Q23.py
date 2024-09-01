"""
Write a Python function to insert a string in the middle of a string.
"""
def insert_in_middle(original, to_insert):
    middle_index = len(original) 
    
    new_string = original[:middle_index] + to_insert + original[middle_index:]
    
    return new_string

original_string = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

result = insert_in_middle(original_string, string_to_insert)
print("Resulting string:", result)


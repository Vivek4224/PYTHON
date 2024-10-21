"""
Write a Python script to sort (ascending and descending) a dictionary by
value.
"""
numbers={'n1':3,
         'n2':1,
         'n3':2,
         'n4':5,
         'n5':4
        }
ascending=dict(sorted(numbers.items(),key = lambda x : x[1]))
print(f"Ascending order: {ascending}")
descending=dict(sorted(numbers.items(),key = lambda x : x[1], reverse=True))
print(f"Descending order:{descending}")
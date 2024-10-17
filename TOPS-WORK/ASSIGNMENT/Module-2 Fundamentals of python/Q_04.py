"""
How memory is managed in Python?

Ans:-

1. Automatic Memory Management
- Garbage Collection: Python automatically manages memory using garbage collection to clean up unused objects. 

  - Reference Counting: Tracks the number of references to an object. When no references remain, the memory is freed.

  - Cycle Detection: Handles circular references (objects that reference each other) that reference counting alone can't manage.

2. Memory Pooling
- Private Heap: Python uses a private area of memory for storing objects. 

- Specialized Allocators: For small objects, Python uses efficient memory pools to minimize overhead.

3. Key Components
- Memory Manager: Manages allocation and deallocation of memory for Python objects.

- Garbage Collector: Handles garbage collection in different stages (generations) to manage memory efficiently.

## Summary
Python handles memory automatically by cleaning up unused objects and using efficient memory pools. This process helps keep the program running smoothly without manual memory management by the developer.
"""


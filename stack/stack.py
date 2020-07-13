"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def is_empty(self):
        return len(self.storage) == 0

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        return value

    def pop(self):
        if not self.is_empty():
            #push 100
            #push 101
            #push 105
            count = len(self.storage)
            value = self.storage[count - 1]
            self.storage.pop()
            return value


import sys
sys.path.append('stack')

from stack import Node, LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def is_empty(self):
        return len(self.storage) == 0
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):        
        self.storage.insert(0, Node(value))
    
    def contains(self, value):
        return next(node for node in self.storage if node.value == value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop().value

queue = Queue()
queue.enqueue(2)
queue.enqueue(4)

queue.dequeue()

for n in queue.storage:
    print(n.value)
import sys
sys.path.append('stack')

from stack import Node, LinkedList

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

        return node.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.tail == None:
            self.head = new_node            
            self.tail = self.head

            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            new_node.previous = self.tail
            self.tail = new_node
            self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        self.length -= 1
        return node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node)        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        prev_node = node.previous
        next_node = node.next

        if prev_node is not None:
            prev_node.next_node = next_node
        else:
            self.head = next_node

        next_node.previous = prev_node

        if next == None:
            self.tail = prev_node        
        
        self.length -= 1
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

dll = DoublyLinkedList()

node = ListNode(2)

dll.add_to_tail(node)

node_2 = ListNode(3)

dll.add_to_tail(node_2)

print(dll.tail.value.value)
print(dll.tail.prev.value.value)
print(dll.head.next.value.value)

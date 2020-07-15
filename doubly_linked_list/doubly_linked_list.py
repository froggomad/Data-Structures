"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_value(self):
        return self.value
            
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
    
    def is_empty(self):
        return self.length == 0

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
        if self.is_empty():
            return
        node = self.head
        self.head = self.head.next
        #note, I don't see why this check is necessary, but test is failing on line 29
        if self.head:            
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
        
        if self.is_empty():
            print(f"empty list. adding {new_node.value}")
            self.head = new_node
            self.tail = self.head
        else:
            print(f"add node: {new_node.value}")
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            print(self.tail.prev.value)
            
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.is_empty():            
            return                
        node = self.tail
        if node.prev:
            self.tail = node.prev        
            self.tail.next = None
        #there is nothing before the tail, which means the head and tail are equal and we just deleted the last node from the list
        else:
            self.tail = None
            self.head = None

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
        if node is self.tail:
            return

        elif node is self.head:
            if node.next is not None:                
                self.add_to_tail(node)
                self.move_to_front(node.next)
            return

        self.delete(node)
        self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.is_empty():
            return
        #get the next and prev nodes so we can re-link the list
        prev_node = node.prev
        next_node = node.next

        # if the previous node exists, assign next_node to its next
        if prev_node is not None:
            prev_node.next_node = next_node
        # otherwise, we must be dealing with the head, so replace the head with the next node 
        else:
            if next_node is not None:
                self.head = next_node
            # if next_node is none and prev node is not none, we must have just deleted the head, and there are no other nodes
            else:
                self.head = None
                self.tail = None
        
        self.length -= 1
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.is_empty():
            return 0
        max_value = self.head.get_value()
        print(f"beginning max: {max_value}")
        current = self.head

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()                
            current = current.get_next()

        print(f"new max: {max_value}")

        if self.tail.get_value() > max_value:
            print(self.tail.get_value())
            return self.tail.value
        return max_value

dll = DoublyLinkedList()
dll.add_to_head(1)
dll.add_to_head(2)
dll.delete(dll.tail)
print(dll.head.value)
dll.get_max()
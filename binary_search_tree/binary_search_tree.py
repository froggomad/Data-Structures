"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
            # we need to go left

            # if we see there is no left, wrap value in BSTNode
            # and park it
            # if there's no node to compare the input to,
                # we can wrap the value in a BSTNode and park it
                # otherwise there is a child
                # call the left child's `insert` method
        #otherwise, value >= Node's value...
            # we need to go right
            # if we see there is no right, wrap value in BSTNode
            # and park it
            # otherwise there is a child
            # call the right child's insert method
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):        
        if target == self.value:
            return True

        if target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        else:
            return False
               

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        temp = self
        current = self
        while current.left:
            if current.left.value > max_value:
                max_value = current.left.value
            current = current.left
        
        current = temp

        while current.right:
            if current.right.value > max_value:
                max_value = current.right.value
            current = current.right
        
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


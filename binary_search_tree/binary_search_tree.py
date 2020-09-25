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
        # if there's no root
        if self.value is None:
            # insert value as root
            self.value = value

        # if value is >= root
        elif value >= self.value:
            # if there's no right child, insert value at the right
            if self.right is None:
                self.right = BSTNode(value)
            # otherwise recursively apply the comparison
            else:
                self.right.insert(value)

        else:
            if self.left is None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if there's no root, return False
        if self.value is None:
            return False

        # if root is the target, return True
        elif self.value == target:
            return True

        # if target is >= root, go right, otherwise go left
        elif target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

        else:
            if not self.left:
                return False
            else:
                return self.right.contains(target)

        # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value

        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self.value:
            return
        else:
            fn(self.value)

            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        if not self.value:
            return
        queue = []
        queue.append(self)

        while queue:
            for _ in range(len(queue)):
                current = queue.pop(0)
                print(current.value)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        if not self.value:
            return

        stack = []
        stack.append(self)

        while stack:
            for _ in range(len(stack)):
                current = stack.pop()
                print(current.value)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()

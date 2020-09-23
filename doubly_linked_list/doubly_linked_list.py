"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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
        new_head = ListNode(value)

        if self.length == 0:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        removed_head = self.head.value
        # empty DLL
        if self.head is None:
            return None

        # 1 element DLL
        elif self.length == 1:
            self.head = None
            self.tail = None

        # +2 elements DLL
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return removed_head

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        # 1 Empty list
        if self.length == 0:
            self.head = new_tail
            self.tail = new_tail

        # 2 Nonempty list
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail

        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        removed_tail = self.tail.value
        # Empty DLL
        if self.length == 0:
            return None

        # 1 element DLL
        elif self.length == 1:
            self.head = None
            self.tail = None

        # +2 elements DLL
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return removed_tail

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return

        elif self.length == 1:
            return

        else:
            self.delete(node)
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return

        elif self.length == 1:
            return

        else:
            self.delete(node)
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # DLL is empty
        if self.length == 0:
            return None

        # DLL has 1 node
        elif self.length == 1:
            self.head = None
            self.tail = None

        # DLL has +2 nodes
        else:
            # node is the head
            if self.head is node:
                self.head = self.head.next
                node.delete()

            # node is the tail
            elif self.tail is node:
                self.tail = self.tail.prev
                node.delete()

            # node is not the head or the tail
            else:
                node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None

        else:
            current_node = self.head
            max_value = self.head.value
            while current_node:
                if current_node.value > max_value:
                    max_value = current_node.value
                current_node = current_node.next

            return max_value

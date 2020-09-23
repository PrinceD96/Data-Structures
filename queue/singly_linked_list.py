class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_tail = Node(value)

        if self.head is None:
            self.head = new_tail

        else:
            self.tail.set_next_node(new_tail)
        self.tail = new_tail

    def remove_head(self):
        if self.head is None:
            return None

        else:
            current_head = self.head.get_value()

            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.get_next_node()

            return current_head

    def remove_tail(self):
        # Empty LL
        if self.head is None:
            return None
        # Nonempty LL
        else:
            # Only 1 Node LL
            if self.head == self.tail:
                value = self.head.get_value()
                self.head = None
                self.tail = None
                return value

            # +2 Nodes LL
            else:
                current = self.head
                while current.get_next_node() is not self.tail:
                    current = current.get_next_node()

                value = self.tail.get_value()
                self.tail = current
                self.tail.set_next_node(None)
                return value

    def contains(self, value):
        if self.head is None:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next_node()
        return False

    def get_max(self):
        if self.head is None:
            return None

        max_value = self.head.get_value()
        current = self.head.get_next_node()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next_node()
        return max_value

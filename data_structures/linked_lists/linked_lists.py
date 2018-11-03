
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # indicates node is a leaf by default

class LinkedList:
    def __init__(self):
        self.head = None

    def append(data):
        if self.head is None:
            self.head = Node(data)
            return

        # find leaf node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = Node(data)

    def prepend(data):
        # Point new node to previous head, which could be null (if list is empty)
        node = Node(data)
        node.next = self.head

        # Update the head so future operations can be performed
        self.head = node

    def delete_with_value(data):
        if self.head is None:
            return

        # delete head
        if self.head.data == data:
            # delete self.head from memory?
            self._head = self.head.next
            return
        
        current = self.head
        while current is not None:
            # delete the next node
            if current.next.data == data:
                # delete current.next
                current.next = current.next.next
                return

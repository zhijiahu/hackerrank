
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):

    slow = head

    if head.next is None:
        return False

    fast = head.next.next

    if fast is None:
        return False

    while slow is not None:
        slow = slow.next

        if fast.next is None:
            return False

        fast = fast.next.next

        if slow is fast:
            return True

    return False

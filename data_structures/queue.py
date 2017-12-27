"""
1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
"""
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if not self.stack2:
            self.move_to_other_stack()

        return self.stack2[-1]

    def pop(self):
        if not self.stack2:
            self.move_to_other_stack()

        return self.stack2.pop()

    def put(self, value):
        self.stack1.append(value)

    def move_to_other_stack(self):
        # move all elements in stack1 to stack2 in reverse order
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def size(self):
        return len(self.stack1) + len(self.stack2)

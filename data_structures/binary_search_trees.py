
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        """
        Naive way
        """
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value < self.value:
            if self.left is not None:
                return self.left.contains(value)
            else:
                return False
                
        elif value > self.value:
            if self.right is not None:
                return self.right.contains(value)
            else:
                return False
        else:
            return True

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print('[{value}]'.format(value=self.value))

        if self.right is not None:
            self.right.print_in_order()


if __name__ == "__main__":
    n = Node(5)
    n.insert(3)
    n.insert(7)
    n.insert(1)
    n.insert(15)
    n.insert(6)

    n.print_in_order()

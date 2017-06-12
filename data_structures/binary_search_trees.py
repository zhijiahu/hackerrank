from trees_binary_search import checkBST


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        """
        Naive way
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, data):
        if data < self.data:
            if self.left is not None:
                return self.left.contains(data)
            else:
                return False
                
        elif data > self.data:
            if self.right is not None:
                return self.right.contains(data)
            else:
                return False
        else:
            return True

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print('[{data}]'.format(data=self.data))

        if self.right is not None:
            self.right.print_in_order()


if __name__ == "__main__":
    n = Node(1)
    n.insert(2)
    n.insert(4)
    n.insert(3)
    n.insert(5)
    n.insert(6)
    n.insert(7)

    n.print_in_order()

    print(checkBST(n))

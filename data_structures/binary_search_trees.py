from queue import MyQueue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return (self.data < other.data)

    def __gt__(self, other):
        return(self.data > other.data)
    
    def insert(self, data):
        """
        Naive way
        """
        print('Inserting [{}]... now at [{}]'.format(data, self.data))

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

        print('    [{}]'.format(self.data))
        print('    /  \\')
        print('  [{}]  [{}]'.format(self.left.data if self.left is not None else '', self.right.data if self.right is not None else ''))
        print('')

    def contains(self, data):
        print('Finding {}'.format(data))

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

    def get_ordered_list(self, sorted_list):
        if self.left is not None:
            self.left.get_ordered_list(sorted_list)

        sorted_list.append(self.data)

        if self.right is not None:
            self.right.get_ordered_list(sorted_list)

    def print_tree(self):
        q = MyQueue()
        q.put(self)

        while q.size() > 0:
            n = q.pop()

            print('[{}]'.format(n.data))
            if n.left is not None:
                q.put(n.left)

            if n.right is not None:
                q.put(n.right)


if __name__ == "__main__":

    # Insert
    print('\nInserting...')
    top = 8
    n = Node(top)
    insert_list = [3,7,2,4,6,5]
    for d in insert_list:
        n.insert(d)
    print('Insert order: {},{}'.format(top, ','.join(str(d) for d in insert_list)))

    # Order
    sorted_list = []
    n.get_ordered_list(sorted_list)
    print('\nReturn ordered list: {}'.format(sorted_list))

    # BFS
    print('\nReturn list after BFS:')
    n.print_tree()

    # Search
    e = insert_list[2]
    print('\nFinding element {} .. {}'.format(e, n.contains(e)))


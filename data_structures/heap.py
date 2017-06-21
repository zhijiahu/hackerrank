
class Heap:
    """
     5
   /   \
  8     11
 / \   /  \
14 15 26  47

    """
    def __init__(self):
        self.data = []

    def __get_parent_index(index):
        return (index - 1) // 2

    def __get_left_index(parent_index):
        return (parent_index * 2) + 1

    def __get_right_index(parent_index):
        return (parent_index * 2) + 2

    def peek(self):
        if self.data:
            return self.data[0]

    def push(self, value):
        self.data.append(value)
        self.sift_up()

    def poll(self):
        first = self.data[0]
        last = self.data.pop()
        self.data[0] = last

        self.sift_down()

        return first

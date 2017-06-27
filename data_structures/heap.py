
class Heap:
    """
     5
   /   \
  8     11
 / \   /  \
14 15 26  47

    """
    def __init__(self):
        self.__items = []

    def __get_parent_index(index):
        return (index - 1) // 2

    def __get_left_index(parent_index):
        return (parent_index * 2) + 1

    def __get_right_index(parent_index):
        return (parent_index * 2) + 2

    def __has_left_child(index):
        return __get_left_index(index) < len(self.__items)

    def __has_right_child(index):
        return __get_right_index(index) < len(self.__items)

    def __has_parent(index):
        return __get_parent_index(index) >= 0

    def __left_child(index):
        return self.__items[self.__get_left_index(index)]

    def __right_child(index):
        return self.__items[self.__get_right_index(index)]

    def __parent(index):
        return self.__items[self.__get_parent_index(index)]

    def __swap(index_one, index_two):
        temp = self.__items[index_one]
        self.__items[index_one] = self.__items[index_two]
        self.__items[index_two] = temp

    def peek(self):
        return self.__items[0]

    def poll(self):
        first = self.__items[0]
        last = self.__items.pop()
        self.__items[0] = last

        self.__sift_down()

        return first

    def add(self, value):
        self.__items.append(value)
        self.__sift_up()

    def __sift_up():
        # start with last index
        index = len(self.__items) - 1

        while self.__has_parent(index) and (self.__parent(index) > self._items[index]):
            parent_index = self.__get_parent_index(index)
            self.__swap(index, parent_index)
            index = parent_index

    def __sift_down():
        pass

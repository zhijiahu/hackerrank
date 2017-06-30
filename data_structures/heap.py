
class Heap:
    """
     5
   /   \
  8     11
 / \   /  \
14 15 26  47

    """
    def __init__(self, is_max):
        self.__items = []

        if is_max:
            self.__comparator = self.__more_than
        else:
            self.__comparator = self.__less_than

    def __more_than(self, item_one, item_two):
        return item_one > item_two

    def __less_than(self, item_one, item_two):
        return item_one < item_two

    def __get_parent_index(self, index):
        return (index - 1) // 2

    def __get_left_index(self, parent_index):
        return (parent_index * 2) + 1

    def __get_right_index(self,parent_index):
        return (parent_index * 2) + 2

    def __has_left_child(self, index):
        return self.__get_left_index(index) < len(self.__items)

    def __has_right_child(self, index):
        return self.__get_right_index(index) < len(self.__items)

    def __has_parent(self, index):
        return self.__get_parent_index(index) >= 0

    def __left_child(self, index):
        return self.__items[self.__get_left_index(index)]

    def __right_child(self, index):
        return self.__items[self.__get_right_index(index)]

    def __parent(self, index):
        return self.__items[self.__get_parent_index(index)]

    def __swap(self, index_one, index_two):
        temp = self.__items[index_one]
        self.__items[index_one] = self.__items[index_two]
        self.__items[index_two] = temp

    def size(self):
        return len(self.__items)

    def peek(self):
        if not self.__items:
            return None

        return self.__items[0]

    def poll(self):
        first = self.__items[0]
        last = self.__items.pop()

        if self.size() > 0:
            self.__items[0] = last
            self.__sift_down()

        return first

    def add(self, value):
        self.__items.append(value)
        self.__sift_up()

    def __sift_up(self):
        # start with last index
        index = len(self.__items) - 1

        while self.__has_parent(index) and self.__comparator(self.__items[index], self.__parent(index)):
            parent_index = self.__get_parent_index(index)
            self.__swap(index, parent_index)
            index = parent_index

    def __sift_down(self):
        # start with first index
        index = 0

        while self.__has_left_child(index):
            # find which child has the priority, in order to compare with current item
            # check left first
            higher_priority_child_index = self.__get_left_index(index)
            if self.__has_right_child(index) and self.__comparator(self.__right_child(index), self.__left_child(index)):
                higher_priority_child_index = self.__get_right_index(index)

            # if child has higher priority, swap!
            if self.__comparator(self.__items[higher_priority_child_index], self.__items[index]):
                self.__swap(index, higher_priority_child_index)
                index = higher_priority_child_index
            else:
                break

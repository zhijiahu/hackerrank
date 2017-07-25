
class Tries:
    """
        c
       / \
      a   i
     / \   \
    t   r   d

    """

    def __init__(self):
        self.tries = Node()

    def add(self, word):
        self.tries.add_child(word)

    def start_with_prefix(self, prefix):
        pass

    def has_word(self, word):
        pass

    def __str__(self):
        print(self.tries)


class Node:
    def __init__(self):
        self._is_complete = False
        self.__children = {}

    def __str__(self):
        print(self._children)

    def add_child(self, word):
        first_letter = word[0]

        if len(word) > 1:
            if first_letter not in self.__children:
                node = Node()
                node.add_child(word[1:])
                self.__children[first_letter] = node
            else:
                self.__children[first_letter].add_child(word[1:])

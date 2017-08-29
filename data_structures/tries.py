
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
        self.tries.add(word)

    def get_words_starting_with_prefix(self, prefix):
        words = []
        self.tries.get_words_starting_with_prefix(prefix, words)

        return words

    def has_word(self, word):
        pass

    def __str__(self):
        return str(self.tries)


class Node:
    def __init__(self):
        self._is_complete = False
        self.__children = {}

    def __repr__(self):
        return str(self.__children)

    def __str__(self):
        return str(self.__children)

    def get_words_starting_with_prefix(self, prefix, words):
        first_letter = prefix[0]

        #if first_letter in self._children:
            
        
    def add(self, word):
        first_letter = word[0]

        if first_letter not in self.__children:
            node = Node()
            if len(word) > 1:
                node.add(word[1:])
            self.__children[first_letter] = node
        else:
            self.__children[first_letter].add(word[1:])

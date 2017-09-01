
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Tries:
    """
    cat
    car
    cid

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
        self.tries.get_words_starting_with_prefix('', prefix, words)

        return words

    def has_word(self, word):
        pass

    def __str__(self):
        return str(self.tries)


class Node:
    def __init__(self):
        self._is_complete = False
        self.__children = {}
        self.__is_last_letter = False
        self.__visited = False

    def __repr__(self):
        return pp.pformat(self.__children)

    def set_visited(self):
        self.__visited = True

    def set_last_letter(self):
        assert(not self.__is_last_letter)
        self.__is_last_letter = True

    def get_words_starting_with_prefix(self, curr_word, prefix, words):
        """
        find c
        """
        first_letter = prefix[0]
        curr_word += first_letter

        if first_letter in self.__children:

            if len(prefix) > 1:
                self.__children[first_letter].get_words_starting_with_prefix(curr_word, prefix[1:], words)
            else:
                self.__children[first_letter].__get_all_words_from_node(curr_word, words)

    def __get_all_words_from_node(self, curr_word, words):
        if self.__is_last_letter:
            words.append(curr_word)

        if self.__children:
            for letter, node in self.__children.items():
                curr_word += letter
                if not node.__get_all_words_from_node(curr_word, words):
                    curr_word = curr_word[:-1]
        else:
            return False

    def add(self, word):
        first_letter = word[0]

        if first_letter not in self.__children:
            node = Node()
            if len(word) > 1:
                node.add(word[1:])
            else:
                node.set_last_letter()
            self.__children[first_letter] = node
        else:
            self.__children[first_letter].add(word[1:])


from functools import cmp_to_key
from itertools import zip_longest


class QuickSort():

    @staticmethod
    def sort(array):
        """
        1. Choose a pivot from the current segment with right and left pointers
           at last and first element
        2. Move left pointer until it is pointing at an element > pivot
        3. Move right pointer until it is pointing at an element < pivot
        4. Swap the 2 elements
        5. Partition from first to 1 element before RIGHT and from RIGHT to last
        6. Perform the same logic on each partitions
        """
        pivot = len(array) // 2
        left = 0
        right = len(array)-1

        left_element = None
        while left <= pivot:
            if array[left] > array[pivot]:
                left_element = array[left]
                break
            left += 1

        right_element = None
        while right >= pivot:
            if array[right] < array[pivot]:
                right_element = array[right]
                break
            right -= 1

        # swap
        left_element, right_element = right_element, left_element

    def partition_sort(left, right, pivot):
        pass


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.name

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif b.score > a.score:
            return 1

        char_pairs = zip_longest(a.name, b.name)
        for pair in char_pairs:
            if pair[0] is None:
                return -1
            if pair[1] is None:
                return 1

            if pair[0] > pair[1]:
                return 1
            elif pair[1] > pair[0]:
                return -1

        return 0 # same

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

# Using built-in sort
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


# Using my own sort
data = [d.score for d in data]
QuickSort.sort(data)
for i in data:
    print(i)

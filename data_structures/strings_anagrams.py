"""
Sample Input
cde
abc

Sample Output
4

"""

from collections import defaultdict


def number_needed(a, b):
    """
    number of deletions needed to make them anagrams
    """
    count = 0
    freq = defaultdict(int)

    for char in a:
        freq[char] += 1
    for char in b:
        freq[char] -= 1

    print(freq)
    for c in freq.values():
        count += abs(c)

    return count


def is_twin(a, b):
    letters = [0] * 26

    for c in a:
        letters[ord(c.lower()) - ord('a')] += 1

    for c in b:
        letters[ord(c.lower()) - ord('a')] -= 1

    print(letters)
    for c in letters:
        if c != 0:
            return False

    return True


a = input().strip()
b = input().strip()

print('Requires {} deletions to make them anagram'.format(number_needed(a, b)))
print('Is anagram? {}'.format(is_twin(a, b)))

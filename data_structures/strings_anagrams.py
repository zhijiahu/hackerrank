"""
Sample Input
cde
abc

cdde
adc


Sample Output
4

"""

from collections import defaultdict


def number_needed(a, b):
    count = 0
    freq = defaultdict(int)

    for char in a:
        freq[char] += 1
    for char in b:
        freq[char] -= 1
    
    for c in freq.values():
        count += abs(c)

    return count


a = input().strip()
b = input().strip()

print(number_needed(a, b))

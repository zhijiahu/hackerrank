"""
Sample Input
cde
abc

Sample Output
4

"""

def number_needed(a, b):
    # increment if a contains a char not in b
    count = 0

    # build a dict of char -> count for a and b
    a_char_count = {}
    for char in a:
        if char in a_char_count:
            a_char_count[char] += 1
        else:
            a_char_count[char] = 1


    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))

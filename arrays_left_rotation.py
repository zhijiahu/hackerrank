import copy

"""
sample input:
5 4
1 2 3 4 5
"""

def array_left_rotation(a, n, k):
    output = copy.copy(a)
    for i, item in enumerate(a):
        new_location = (i-k+n)%n
        output[new_location] = item

    return output

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

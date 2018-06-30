import random

loops = 0

def merge_sort(array):
    global loops
    loops += 1

    if len(array) > 1:
        middle = len(array) // 2
        left = merge_sort(array[0:middle])
        right = merge_sort(array[middle:len(array)])

        partial = []
        while left:
            loops += 1

            if not right or left[0] < right[0]:
                partial.append(left[0])
                left = left[1:]
            else:
                partial.append(right[0])
                right = right[1:]

        while right:
            loops += 1

            partial.append(right[0])
            right = right[1:]

        return partial

    else:
        return array


l = random.sample(range(10000), 100)
print(l)
l = merge_sort(l)
print('{} loops'.format(loops))
print(l)



def has_sequence_of_sums(array, sums):
    start = 0
    total = 0

    for i, x in enumerate(array):
        total += x

        while (total > sums and start < len(array)):

            total -= array[start]
            start += 1

        if total == sums:
            return True, (start, i)

    return False


a = [6, 2, 9, 4, 3, 1]
print(a)
result, ranges = has_sequence_of_sums(a, 16)
print(result, ranges)

if result:
    print(a[ranges[0]: ranges[1]+1])

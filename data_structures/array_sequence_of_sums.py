import timeit


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

def slow_algo(array, sums):
    start = 0
    end = 1
    total = array[start]

    while start < len(array):
        total += array[end]

        if total > sums:

            start += 1
            end = start + 1
            total = array[start]
            continue

        if total == sums:
            return True, (start, end)

        end += 1


a = [0] * 1000 + [6, 2, 9, 4, 3, 1]
sums = 16

print(a)
print('Finding sum = {}'.format(sums))
result, ranges = has_sequence_of_sums(a, 16)
print(result, ranges)

result, ranges = slow_algo(a, 16)
print(result, ranges)

if result:
    print(a[ranges[0]: ranges[1]+1])


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(has_sequence_of_sums, a, sums)
print(timeit.timeit(wrapped, number=1))

wrapped = wrapper(slow_algo, a, sums)
print(timeit.timeit(wrapped, number=1))

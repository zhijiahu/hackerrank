
import random


def bubble_sort(array):

    total_swaps = 0
    for (i, item) in enumerate(array):
        num_swaps = 0;

        for (j, item) in enumerate(array[:-1]):
            # Swap adjacent elements if they are in decreasing order
            if (array[j] > array[j + 1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                num_swaps += 1

        total_swaps += num_swaps

        #If no elements were swapped during a traversal, array is sorted
        if num_swaps == 0:
            break

    print('Array is sorted in {} swaps.'.format(total_swaps))
    print('First Element: {}'.format(array[0]))
    print('Last Element: {}'.format(array[-1]))


l = [random.randint(0,1000) for _ in range(1000)]
print(l)
bubble_sort(l)
print(l)



import random

class QuickSort():

    @staticmethod
    def _sort(left, right, array):
        """
        1. Choose a pivot from the current segment with right and left pointers
           at last and first element
        2. Move left pointer until it is pointing at an element > pivot
        3. Move right pointer until it is pointing at an element < pivot
        4. Swap the 2 elements
        5. Partition from first to 1 element before RIGHT and from RIGHT to last
        6. Perform the same logic on each partitions
        """
        pivot = right
        right = pivot-1
        initial_left = left
        initial_right = right

        print('pivot [{}]'.format(pivot))

        while True:
            while True:
                if left == right:
                    break

                if array[left] >= array[pivot]:
                    break

                if left == pivot-1:
                    break

                left += 1
                print('left [{}]'.format(left))

            while True:
                if left == right:
                    break

                if array[right] <= array[pivot]:
                    break

                if right == 0:
                    break

                right -= 1
                print('right [{}]'.format(right))

            if left == right:
                break

            # swap left and right
            print("swapping [{}] [{}]".format(left, right))
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            print(array)


        assert left == right

        # right/left onswap with pivot
        print("swapping pivot [{}] [{}]".format(pivot, right))
        temp = array[pivot]
        array[pivot] = array[left]
        array[left] = temp
        print(array)

        if pivot == left and pivot == right:
            return # already sorted

        pivot = left # or right, no diff

        import ipdb; ipdb.set_trace()

        print(array)
        print('Split at [{}]'.format(pivot))
        QuickSort._sort(initial_left, pivot-1, array)
        QuickSort._sort(pivot+1, initial_right+1, array)

    @staticmethod
    def sort(array):
        QuickSort._sort(left=0, right=len(array)-1, array=array)

l = [random.randint(0,10) for _ in range(10)]
print(l)
QuickSort.sort(l)
print(l)


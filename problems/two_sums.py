
def two_sum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Time complexity : O(n)
    We traverse the list containing n elements only once. Each look up in the table costs only O(1)time.

    Space complexity : O(n)
    The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
    """
    visited = {}
    for i, a in enumerate(nums):
        b = target - a
        if b not in visited:
            visited[a] = i
        else:
            j = visited[b]
            return [i, j]

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    result = two_sum(nums, target)
    assert 1 in result and 2 in result

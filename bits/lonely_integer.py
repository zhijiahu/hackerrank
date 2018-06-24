


def find_lonely_int(array):
    """
    Assume there is only 1 lonely int
    """
    bits = 0

    for d in array:
        bits ^= d

    return bits

array = [12, 3, 3, 7, 12]
print('Found lonely {} in {}'.format(find_lonely_int(array), array))

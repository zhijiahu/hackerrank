


def find_lonely_int(array):
    """
    Assume there is only 1 lonely int
    """
    bits = 0

    for d in array:
        bits ^= d

    return bits

KEY = 'secret'
def xor_cipher(a, b):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(a, b))

array = [12, 3, 3, 7, 12]
print('Found lonely {} in {}'.format(find_lonely_int(array), array))

string = 'abcd'
print(xor_cipher(string, KEY))
print(xor_cipher(xor_cipher(string, KEY), KEY));

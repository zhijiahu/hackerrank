

def reverse_loop(word):
    results = ''

    i = len(word) - 1
    while i >= 0:
        results += word[i]
        i -= 1

    return results

def reverse_recursive(word):
    print('[{}]'.format(word))

    if len(word) == 1:
        print('STOPPED')
        return word

    bottom = reverse_recursive(word[1:])
    result = bottom + word[0]

    print('{} , [{}] : {}'.format(bottom, word, result))

    return result

word = 'hello'
print('{} {}'.format(word, reverse_loop(word)))
print('{} {}'.format(word, reverse_recursive(word)))

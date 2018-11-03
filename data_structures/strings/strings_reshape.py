
def reshape(n, letters):
    output = ''
    count = 0

    for c in letters:
        if c != ' ':
            count += 1
            output += c

        if count == n:
            output += '\n'
            count = 0

    return output


inputs = [(3, 'abc de fghij'), (6, '1 23 456')]

for n, letters in inputs:
    print(letters)
    print(reshape(n, letters))


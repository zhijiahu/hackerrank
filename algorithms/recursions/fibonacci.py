

def fibonacci(n):
    if n == 0:
        print('[{}] Returning {}'.format(n, 0))
        return 0

    if n == 1:
        print('[{}] Returning {}'.format(n, 1))
        return 1

    print('[{}] Calling f({}) + f({})'.format(n, n-2, n-1))
    return fibonacci(n-2) + fibonacci(n-1)


# 0,1,2,3,4,5
print(fibonacci(5))

from tries import Tries

tries = Tries()

def add_name(name):
    tries.add(name)

def find_partial(partial):
    words = tries.get_words_starting_with_prefix(partial)
    print(len(words))

def run_with_user_input():
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op == 'add':
            add_name(contact)
        elif op == 'find':
            find_partial(contact)

        # debug
        print(tries)

if __name__ == '__main__':
    run_with_user_input()

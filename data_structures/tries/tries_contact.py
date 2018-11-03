from tries import Tries

g_debug = False

tries = Tries()

def print_verbose(msg):
    if g_debug:
        print(msg)

def add_name(name):
    tries.add(name)
    print_verbose(tries)

def find_partial(partial):
    words = tries.get_words_starting_with_prefix(partial)
    print_verbose(words)
    result = len(words)
    print_verbose(result)
    return result

def run_with_user_input():
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op == 'add':
            add_name(contact)
        elif op == 'find':
            find_partial(contact)

def run_test_case():
    expected_results = []
    with open('tries_output.txt') as f:
        for item in f:
            expected_results.append(item)

    output_index = 0
    with open('tries_input.txt') as f:
        for index, item in enumerate(f):
            if index == 0: # skip the count
                continue

            op, contact = item.split(' ')
            contact = contact.rstrip()
            if op == 'add':
                add_name(contact)
            elif op == 'find':
                result = find_partial(contact)
                if result != int(expected_results[output_index]):
                    print('input {}, output {}'.format(index, output_index))
                    print('contact: {}'.format(contact))
                    print('result:{} != expected:{}'.format(result, expected_results[output_index]))
                    break
                output_index += 1

if __name__ == '__main__':
    #run_with_user_input()
    run_test_case()

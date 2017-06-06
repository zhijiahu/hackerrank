

def is_matched(expression):

    stack = []
    for bracket in expression:
        # Found a close bracket
        if bracket == '}' or bracket == ']' or bracket == ')':
            if not stack:
                return False

            last_open_bracket = stack.pop()

            if (ord(last_open_bracket) + 1 != ord(bracket)) and \
               (ord(last_open_bracket) + 2 != ord(bracket)):
                return False
        else:
            # Assume opened brackets, push into stack
            stack.append(bracket)

    return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

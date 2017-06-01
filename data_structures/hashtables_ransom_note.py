
"""
6 4
give me one grand today night
give one grand today

"""

def ransom_note(magazine, ransom):
    print(magazine)

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

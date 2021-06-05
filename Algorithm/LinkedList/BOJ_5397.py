import sys
case = int(sys.stdin.readline().rstrip())

for i in range(0, case):
    left = []
    right = []
    strings = sys.stdin.readline().strip()
    for j in range(len(strings)):
        if strings[j] == '<':
            if left:
                right.append(left.pop())
        elif strings[j] == '>':
            if right:
                left.append(right.pop())
        elif strings[j] == '-':
            if left:
                left.pop()
        else:
            left.append(strings[j])
    right.reverse()
    print("".join(left + right))













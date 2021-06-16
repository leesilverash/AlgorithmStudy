from collections import deque
import sys

strings = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())

left=[]
right=[]
cursor = len(strings)

for i in range(len(strings)):
    left.append(strings[i])

for i in range(n):
    command = sys.stdin.readline().strip()
    if command[0] == 'L':
        if len(left) != 0:
            tmp = left.pop()
            right.append(tmp)
    elif command[0] == 'D':
        if len(right) != 0:
            tmp = right.pop()
            left.append(tmp)
    elif command[0] == 'B':
        if len(left) != 0:
            left.pop()
    else:
        left.append(command[2])
right.reverse()
print("".join(left+right))



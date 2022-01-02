import sys
from collections import deque
import re

t = int(sys.stdin.readline().strip())

while t != 0:
    deq = deque()
    cmd = list(sys.stdin.readline().strip())
    size = int(sys.stdin.readline().strip())
    str = sys.stdin.readline().strip()
    num = re.findall("[0-9]+", str)
    isReversed = -1
    error = False
    for i in num:
        deq.append(i)
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            isReversed *= -1
        else:
            if deq:
                if isReversed == -1:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                error = True
                break
    if error == False:
        size = len(deq)
        if isReversed == -1:
            str = '['
            for i in range(size):
                str += deq.popleft()
                if i < size-1:
                    str += ','
            str += ']'
            print(str)
        else:
            str = '['
            for i in range(size):
                str += deq.pop()
                if i < size-1:
                    str += ','
            str += ']'
            print(str)
    else:
        print('error')
    t -= 1

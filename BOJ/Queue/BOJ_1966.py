import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    deq = deque(map(int, sys.stdin.readline().rstrip().split()))
    idx = [0 for _ in range(n)]
    idx[m] = 1
    count = 0
    while deq:
        if deq[0] == max(deq):
            if idx[0] == 1:
                break
            else:
                deq.popleft()
                idx.pop(0)
                count+=1
        else:
            deq.append(deq.popleft())
            idx.append(idx.pop(0))
    print(count+1)

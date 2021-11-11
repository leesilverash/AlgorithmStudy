import sys
from collections import deque
deq = deque()
n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    deq.append(i)

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())
print(deq[0])
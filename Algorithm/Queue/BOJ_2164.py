from collections import deque
import sys

deq = deque()
n = int(sys.stdin.readline().strip())

for i in range(1, n+1):
    deq.append(i)

count = 1
while len(deq) != 1:
    if count % 2 != 0:
        deq.popleft()
        count+=1
    else:
        deq.rotate(-1)
        count+=1

print(deq.pop())
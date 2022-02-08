from collections import deque

n, k = map(int, input().split())
deq = deque([i for i in range(1, n+1)])

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    deq.popleft()
    if len(deq) == 1:
        print(deq[0])
        deq.popleft()
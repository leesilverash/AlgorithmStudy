import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())

lst = []
lst.extend(list(map(int, sys.stdin.readline().rstrip().split())))
heapq.heapify(lst)

for _ in range(M):
    x = heapq.heappop(lst)
    y = heapq.heappop(lst)
    heapq.heappush(lst, x + y)
    heapq.heappush(lst, x + y)

print(sum(lst))

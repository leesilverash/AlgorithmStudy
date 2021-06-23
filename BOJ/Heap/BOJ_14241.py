import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0

while len(heap) != 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap,x+y)
    answer += x*y
print(answer)
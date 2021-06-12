import sys
import heapq
N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x >= 1:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))


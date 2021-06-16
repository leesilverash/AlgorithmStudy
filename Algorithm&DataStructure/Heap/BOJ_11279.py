import sys
import heapq
N= int(sys.stdin.readline().rstrip())

heap = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x >= 1:
        heapq.heappush(heap, (-x,x))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
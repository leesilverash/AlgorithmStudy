import heapq
heap = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)
# 5
# 3
# 6
# 0
# 5
# 0
# 2
# 4
# 0
# -1
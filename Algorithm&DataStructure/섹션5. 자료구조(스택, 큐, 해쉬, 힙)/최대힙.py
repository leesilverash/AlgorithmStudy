import heapq
heap =[]
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n, n))

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

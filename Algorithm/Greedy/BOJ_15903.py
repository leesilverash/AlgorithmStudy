import heapq

n, m = map(int,input().split())
list = list(map(int, input().split(' ')))
heap = []

for i in list:
    heapq.heappush(heap,i)

for _ in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    heapq.heappush(heap, x+y)

print(sum(heap))

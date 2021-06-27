import sys
import heapq
n = int(sys.stdin.readline().rstrip())
minHeap = [] # 오른쪽
maxHeap = [] # 왼쪽

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if len(minHeap) == len(maxHeap):
        heapq.heappush(maxHeap, (-num, num))
    else:
        heapq.heappush(minHeap, (num, num))

    if minHeap and maxHeap[0][1] > minHeap[0][1]:
        max_val = heapq.heappop(maxHeap)[1]
        min_val = heapq.heappop(minHeap)[1]
        heapq.heappush(maxHeap, (-min_val, min_val))
        heapq.heappush(minHeap, (max_val, max_val))
    print(maxHeap[0][1])



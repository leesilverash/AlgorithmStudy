import sys
import heapq

N = int(sys.stdin.readline().rstrip())

heap = []
def absNum(num):
    if num < 0:
        num = num*-1
        return num
    else:
        return num

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(heap, (absNum(x), x))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])


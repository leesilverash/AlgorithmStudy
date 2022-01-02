import sys
import heapq
lst = []
n = int(sys.stdin.readline())
for _ in range(n):
    ins = int(sys.stdin.readline())
    def infiniteNumber(num):
        return num * -1 if num < 0 else num
    if ins != 0:
        heapq.heappush(lst, [infiniteNumber(ins),ins])
    else:
        if not lst:
            print(0)
        else:
            x = heapq.heappop(lst)
            print(x[1])




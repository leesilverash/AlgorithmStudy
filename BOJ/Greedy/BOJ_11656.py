import sys
import heapq
s = sys.stdin.readline().rstrip()
lst = []
for i in range(len(s)):
    heapq.heappush(lst, s[i:])

while lst:
    print(heapq.heappop(lst))

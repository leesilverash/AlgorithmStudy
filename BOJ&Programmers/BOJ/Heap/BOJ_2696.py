import heapq
import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    m = int(sys.stdin.readline().rstrip())
    lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    mid = m // 2 if m % 2 == 0 else m // 2 + 1
    print(mid)

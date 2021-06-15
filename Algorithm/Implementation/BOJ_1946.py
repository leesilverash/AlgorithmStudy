import sys
import heapq
T = int(sys.stdin.readline().rstrip())

while T > 0:
    N = int(sys.stdin.readline().rstrip())
    lst = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
    lst.sort()
    answer = 1
    rank = lst[0][1]
    for i in range(1, N):
        if lst[i][1] < rank:
            rank = lst[i][1]
            answer += 1
    print(answer)
    T -= 1







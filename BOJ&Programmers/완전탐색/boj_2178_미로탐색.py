import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0] * m for _ in range(n)]
for _ in range(m):
    line = list(map(int, input().split()))
    print(line[0], line[1])
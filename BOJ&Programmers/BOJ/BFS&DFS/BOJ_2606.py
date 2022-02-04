import sys

n = int(sys.stdin.readline().rstrip())
pair = int(sys.stdin.readline().rstrip())
matrix = [[0] * n for _ in range(n)]
visited = [0 for i in range(n)]
for i in range(pair):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if matrix[v][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(0)
cnt = 0
for i in range(1, n):
    if visited[i] == 1:
        cnt += 1
print(cnt)

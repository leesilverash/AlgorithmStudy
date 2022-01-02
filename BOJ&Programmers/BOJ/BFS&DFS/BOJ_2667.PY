import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    n = len(graph)
    que = deque()
    que.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1
    return cnt

n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])

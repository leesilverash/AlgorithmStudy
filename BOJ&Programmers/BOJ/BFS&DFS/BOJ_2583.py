from collections import deque

m, n, k = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
g = []
for i in range(m):
    g.append([0] * n)
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            g[k][j] = 1
answer = []
for i in range(m):
    for j in range(n):
        if g[i][j] == 0:
            cnt = 1
            g[i][j] = 1
            q = deque()
            q.append((i, j))
            while q:
                tmp = q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < m and 0 <= y < n and g[x][y] == 0:
                        g[x][y] = 1
                        cnt += 1
                        q.append((x, y))
            answer.append(cnt)
print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i], end=' ')
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
# t
# (x1, m - y1)
# print(x2, m - y2)


# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

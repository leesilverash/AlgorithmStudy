from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0, 0))
    dis = [[0] * m for _ in range(n)]
    dis[0][0] = 1
    while q:
        tmp = q.popleft()
        for i in range(4):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1:
                maps[xx][yy] = 0
                dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
                q.append((xx, yy))
    if dis[-1][-1] == 0:
        return -1
    else:
        return dis[-1][-1]

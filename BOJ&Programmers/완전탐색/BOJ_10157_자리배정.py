from collections import deque

x, y = map(int, input().split())
n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [[0] * x for _ in range(y)]
idx = 0
cnt = 1
q = deque()
q.append((y - 1, 0))
answer = [0, 0]
board[y-1][0] = 1
if n > x*y:
    print(0)
else:
    while cnt < n:
        cnt += 1
        tmp = q.popleft()
        xx = tmp[0] + dx[idx]
        yy = tmp[1] + dy[idx]
        if 0 <= xx < y and 0 <= yy < x and board[xx][yy] == 0:
            board[xx][yy] = cnt
            q.append((xx, yy))
        else:
            if idx == 3:
                idx = 0
            else:
                idx += 1
            xx = tmp[0] + dx[idx]
            yy = tmp[1] + dy[idx]
            board[xx][yy] = cnt
            q.append((xx, yy))

    location = q.popleft()
    answer[0] = x - (x - location[1]) + 1
    answer[1] = y - location[0]
    for i in answer:
        print(i, end= ' ')

# 7 6
# 11

# 100 100
# 3000
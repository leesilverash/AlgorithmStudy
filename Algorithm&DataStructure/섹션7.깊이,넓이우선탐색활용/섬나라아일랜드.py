
## DFS 풀이

# dx=[-1, -1, 0, 1, 1, 1, 0, -1]
# dy=[0, 1, 1, 1, 0, -1, -1, -1]
# def dfs(x, y):
#     board[x][y] = 0
#     for i in range(8):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
#             board[xx][yy] = 0
#             dfs(xx, yy)
#
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# res = 0
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 1:
#             print(i,j)
#             dfs(i, j)
#             res+=1
# print(res)

##  BFS  풀이
from collections import deque
q = deque()
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            answer += 1
            q.append((i,j))
            while q:
                tmp = q.pop()
                for k in range(8):
                    xx = tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
                        board[xx][yy] = 0
                        q.append((xx,yy))

print(answer)
# 7
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0
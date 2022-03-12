import sys
dx = [0, 0, -1]
dy = [1, -1, 0]

def dfs(x,y):
    if x == 0:
        print(y)
        sys.exit(0)
    else:
        for i in range(3):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 9 and 0 <= yy <= 9 and board[xx][yy] == 1 and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                dfs(xx,yy)

board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]
# right, left, up 순서
x = 9
y = 0
ans = 0
for i in range(10):
    if board[9][i] == 2:
        y = i
ch[x][y] = 1
dfs(x,y)
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 0 1 0 0 1 0 1 0 1
# 1 0 1 1 1 1 0 1 0 1
# 1 0 1 0 0 1 0 1 1 1
# 1 1 1 0 0 1 0 1 0 1
# 1 0 1 0 0 1 1 1 0 1
# 1 0 1 0 0 2 0 1 0 1
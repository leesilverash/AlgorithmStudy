dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global ans
    if x == 6 and y == 6:
        ans += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < 7 and 0 <= yy < 7 and board[xx][yy] == 0:
                board[xx][yy] = 1
                dfs(xx, yy)
                board[xx][yy] = 0

board = [list(map(int, input().split())) for _ in range(7)]
ans = 0
board[0][0] = 1
dfs(0,0)
print(ans)
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 0
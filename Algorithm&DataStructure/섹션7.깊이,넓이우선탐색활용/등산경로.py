def dfs(x, y):
    global ans
    if x == end[0] and y == end[1]:
        ans += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and g[x][y] < g[xx][yy]:
                board[xx][yy] = 1
                dfs(xx, yy)
                board[xx][yy] = 0



n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
start = [0, 0]
end = [0, 0]
board = [[0] * n for _ in range(n)]
board[start[0]][start[1]] = 1
ans = 0
for i in range(n):
    for j in range(n):
        if g[i][j] < g[start[0]][start[1]]:
            start[0] = i
            start[1] = j
        if g[i][j] > g[end[0]][end[1]]:
            end[0] = i
            end[1] = j
dfs(start[0], start[1])
print(ans)

# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100

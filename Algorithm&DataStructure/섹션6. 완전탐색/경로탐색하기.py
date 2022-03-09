def dfs(v):
    global cnt
    global ans
    if v == n:
        cnt += 1
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                dfs(i)
                ch[i] = 0

n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0] * (n + 1)
cnt = 0
ans = 214700000
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
ch[1] = 1
dfs(1)
print(cnt)
# 5 9
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 5
# 3 4
# 4 2
# 4 5
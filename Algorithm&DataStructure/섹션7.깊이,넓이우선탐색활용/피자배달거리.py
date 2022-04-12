def dfs(l, k):
    global ans
    if l == m:
        sum = 0
        for i in range(len(h)):
            x = h[i][0]
            y = h[i][1]
            tmp = 21470000
            for j in res:
                xx = p[j][0]
                yy = p[j][1]
                dist = abs(x - xx) + abs(y - yy)
                if dist < tmp:
                    tmp = dist
            sum += tmp
        if sum < ans:
            ans = sum
    else:
        for i in range(k, len(p)):  # [0, 0, 0, 0]
            res[l] = i  # res [1, 0]
            dfs(l + 1, i + 1)


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
h = []
p = []
ans = 2147000000

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            h.append((i, j))
        elif g[i][j] == 2:
            p.append((i, j))
res = [0] * m
dfs(0, 0)
print(ans)

# 4 4
# 0 1 2 0
# 1 0 2 1
# 0 2 1 2
# 2 0 1 2

def dfs(l, k):
    global ans
    if l == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        ans += 1
    else:
        for i in range(k, n+1): # [0, 0, 0, 0]
            res[l] = i  # res [1, 0]
            dfs(l+1, i+1)

n, m = map(int, input().split())
res = [0] * m
ans = 0
dfs(0, 1)
print(ans)

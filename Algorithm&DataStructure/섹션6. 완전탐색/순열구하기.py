def dfs(l):
    if l == m:
        global ans
        for i in range(m):
            print(res[i], end = ' ')
        print()
        ans += 1
    else:
        for i in range(1, n+1): # [0, 0, 0, 0]
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i  # res [1, 0]
                dfs(l+1)
                ch[i] = 0

n, m = map(int, input().split())
res = [0] * m
ch = [0] * (n+1)
ans = 0
dfs(0)
print(ans)
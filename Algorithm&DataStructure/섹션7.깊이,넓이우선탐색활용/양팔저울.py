def dfs(l, sum):
    global res
    if l == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        for i in range(1, n+1):
            dfs(l+1, sum+g[l])
            dfs(l+1, sum-g[l])
            dfs(l+1, sum)

n = int(input())
g = list(map(int, input().split()))
s = sum(g)
res = set()
dfs(0,0)
print(s-len(res))


def dfs(l, sums):
    global ans
    if l == n:
        val = max(sums) - min(sums)
        if val < ans:
            ans = val
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                dfs(l+1, sums[])

n = int(input())
lst = [0] * n
ch = [0] * n
ans = 214700000
for i in range(n):
    lst[i] = int(input())
sums = [0] * 3
dfs(0, sums)
def dfs(l, score, time):
    global ans
    if time > m:
        return
    if l == n:
        if score > ans:
            ans = score
    else:
        dfs(l+1, score+lst[l][0], time+lst[l][1])
        dfs(l+1, score, time)

n, m = map(int, input().split())
ch = [0] * (n+1)
ans = -21470000
lst = [[0]*(2) for _ in range(n+1)]
for i in range(1, len(lst)):
    lst[i] = list(map(int, input().split()))
dfs(0,0,0)
print(ans)
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4
def dfs(l, price):
    global ans
    if l > n+1:
        return
    if l == n+1:
        if price > ans:
            ans = price
    else:
        if l + t[l] <= n+1:
            dfs(l+t[l], price + p[l])
        dfs(l+1, price)

n = int(input())
schedule = [0] * (n+1)
ans = 0
t = [0] * (n+1)
p = [0] * (n+1)
for i in range(1, n+1):
    a, b = (map(int,input().split()))
    t[i] = a
    p[i] = b

dfs(1, 0)
print(ans)
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 2
# 1 10
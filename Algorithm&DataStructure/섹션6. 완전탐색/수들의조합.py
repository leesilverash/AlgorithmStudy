n, k = map(int, input().split())
lst = sorted(list(map(int, input().split())))
m = int(input())
res= [0] * k
ans = 0

def dfs(l, s, sum):
    global ans
    if l == k:
        if sum % m == 0:
            ans += 1
    else:
        for i in range(s, n):
            dfs(l+1, i+1, sum+lst[i])

dfs(0,0,0)
print(ans)
# 5 3
# 2 4 5 8 12
# 6
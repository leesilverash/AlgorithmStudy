c, n = map(int, input().split())
w = []
for i in range(n):
    w.append(int(input()))
ans = 0
total = sum(w)

def DFS(l, sum, tsum):
    global ans
    if sum + (total-tsum) < ans:
        return
    if sum > c:
        return
    if l == n:
        if sum > ans:
            ans = sum
    else:
        DFS(l+1, sum + w[l], tsum+w[l])
        DFS(l+1, sum, tsum+w[l])

DFS(0,0,0)
print(ans)


# 259 5
# 81
# 58
# 42
# 33
# 61
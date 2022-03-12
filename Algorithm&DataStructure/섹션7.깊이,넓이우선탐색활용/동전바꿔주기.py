def dfs(l, sum):
    global cnt
    if sum > m:
        return
    if l == n:
        if sum == m:
            cnt += 1
    else:
        for i in range(cn[l] + 1):
            dfs(l+1, sum+cv[l] * i)

m = int(input())
n = int(input())
res = set()
cv = []
cn = []
for i in range(n):
   a,b = map(int ,input().split())
   cv.append(a)
   cn.append(b)
cnt = 0
dfs(0,0)
print(cnt)
# 20
# 3
# 5 3
# 10 2
# 1 5


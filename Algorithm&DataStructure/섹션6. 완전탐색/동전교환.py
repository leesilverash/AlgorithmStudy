n = int(input())
coin = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
ans = 214700000

def DFS(l, sum):
    global ans
    if l >= ans:
        return
    if sum > m:
        return
    if sum == m:
        if l < ans:
            ans = l
    else:
        for i in range(n):
            DFS(l+1, sum + coin[i])

DFS(0,0)
print(ans)
# 3
# 1 2 5
# 15
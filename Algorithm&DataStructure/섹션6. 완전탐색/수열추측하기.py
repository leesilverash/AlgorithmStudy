n = int(input())
lst = sorted(list(map(int, input().split())), reverse= True)
m = int(input())
ans = 214700000

def dfs(l, sum):
    global ans
    if l >= ans:
        return
    if sum > ans:
        return
    if sum == m:
        if l < ans:
            ans = l
    else:
        for i in range(n):
            dfs(l+1, sum+lst[i])



dfs(0, 0)
print(ans)
# 3
# 1 2 5
# 15
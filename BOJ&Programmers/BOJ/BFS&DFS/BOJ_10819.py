def dfs(l):
    global ans
    if l == n:
        tmp = 0
        for i in range(len(ch)-1):
            tmp += abs(ch[i] - ch[i+1])
        if tmp > ans:
            ans = tmp
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = lst[l]
                dfs(l+1)
                ch[i] = 0

n = int(input())
lst = list(map(int, input().split()))
ans = -214700000
ch = [0] * n
dfs(0)
print(ans)
# 6
# 20 1 15 8 4 10
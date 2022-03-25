def dfs(l):
    if l == n:
        for i in range(n):
            print(res[i], end = ' ')
        print()
    else:
        for i in range(1, n+1): # [0, 0, 0, 0]
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i  # res [1, 0]
                dfs(l+1)
                ch[i] = 0

n = int(input())
res = [0] * n
ch = [0] * (n+1)
dfs(0)
def dfs(l, k):
    if l == 6:
        for i in range(6):
            print(res[i], end = ' ')
        print()
    else:
        for i in range(k, n+1):
            res[l] = lst[i]
            dfs(l+1, i+1)

while True:
    lst = list(map(int,input().split()))
    n = lst[0]
    res = [0] * 6
    if n == 0:
        break
    else:
        dfs(0,1)
    print()




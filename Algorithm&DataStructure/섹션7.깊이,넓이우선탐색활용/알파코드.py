def dfs(l,p):
    global cnt
    if l == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j]+64),end='')
        print()
    else:
        for i in range(1, 27):
            if code[l] == i:
                res[p] = i
                dfs(l + 1, p + 1)
            elif i >= 10 and code[l] == i // 10 and code[l + 1] == i % 10:
                res[p] = i
                dfs(l + 2, p + 1)

code = list(map(int, input()))
n = len(code)
code.insert(n, -1)
res = [0] * (n + 3)
cnt = 0
dfs(0, 0)
print(cnt)

# 25114


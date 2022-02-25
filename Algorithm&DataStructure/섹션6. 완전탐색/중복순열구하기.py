import sys
input = sys.stdin.readline

def DFS(l):
    if l == m:
        global cnt
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[l] = i
            DFS(l+1)
n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)
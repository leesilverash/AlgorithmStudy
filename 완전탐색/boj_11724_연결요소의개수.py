import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n , m = map(int, input().split())
adj = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: x-1 , map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * n

def dfs(now):
    for nxt in range(n):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(n):
    if not chk[i]:
        ans+=1
        chk[i] = True
        dfs(i)
print(ans)
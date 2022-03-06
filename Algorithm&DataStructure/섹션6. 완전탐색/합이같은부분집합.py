import sys
n = int(input())
lst = list(map(int, input().split()))
total = sum(lst)
def dfs(l, sum):
    if sum > total // 2:
        return
    if l == n:
        if sum == total - sum:
            print('YES')
            sys.exit(0)
    else:
        dfs(l+1, sum+lst[l])
        dfs(l+1, sum)

dfs(0,0)
print('NO')
# 6
# 1 3 5 6 7 10
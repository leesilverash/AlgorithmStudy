import sys
n = int(input())
lst = list(map(int, input().split()))
total = sum(lst)
answer = False
def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+lst[L])
        DFS(L+1, sum)

DFS(0, 0)
print("NO")

# 6
# 1 3 5 6 7 10
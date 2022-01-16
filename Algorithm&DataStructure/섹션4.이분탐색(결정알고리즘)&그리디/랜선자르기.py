n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lt = 0
rt = max(lst)
ans = 0
while lt <= rt:
    tmp = 0
    mid = (lt + rt) // 2
    for i in range(n):
        tmp += lst[i]//mid
    if tmp < m:
        rt = mid -1
    else:
        ans = mid
        lt = mid + 1

print(ans)
# 4 11
# 802
# 743
# 457
# 539


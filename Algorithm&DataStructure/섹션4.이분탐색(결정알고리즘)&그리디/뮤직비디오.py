n, m = map(int, input().split())
lst = list(map(int,input().split()))
lt = 1
rt = sum(lst)
ans = 0

def check(mid):
    cnt = 1
    sum = 0
    for i in lst:
        if sum + i < mid:
            sum += i
        else:
            cnt += 1
            sum = i
    return cnt

while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) <= m:
        ans = mid-1
        rt = mid-1
    else:
        lt = mid+1

print(ans)

def Count(len):
    cnt = 1
    ep = lst[0]
    for i in range(1, n):
        if lst[i]-ep >= len:
            cnt +=1
            ep = lst[i]
    return cnt

n,m = map(int, input().split())

lst = [int(input()) for _ in range(n)]
lst.sort()

lt = 1
rt = lst[n-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)


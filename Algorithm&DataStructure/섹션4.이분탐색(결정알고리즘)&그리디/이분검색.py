n, m = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt+rt)//2
    if lst[mid] == m:
        print(mid+1)
        break
    elif lst[mid] < m:
        lt = mid+1
    else:
        rt = mid-1
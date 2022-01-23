n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lt = 0
rt = n-1
answer = 0
while lt <= rt:
    if lst[lt] + lst[rt] <= m:
        answer += 1
        lt += 1
        rt -= 1
    else:
        rt -= 1
        answer += 1
print(answer)
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# answer = 0
# for i in range(n):
#     sum = lst[i]
#     for j in range(i+1, n):
#         if sum < m:
#             sum += lst[j]
#             if sum == m:
#                 answer += 1
#                 break
#         else:
#             if sum == m:
#                 answer += 1
#                 break
#             break
# print(answer)

n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)



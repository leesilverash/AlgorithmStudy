n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
dict = {}
answer = 0

for i in range(m):
    lt = 0
    rt = 1
    while lt < n-1:
        if i == 0:
            dict[(lst[i][lt], lst[i][rt])] = 1
        else:
            if (lst[i][lt],lst[i][rt]) in dict:
                dict[(lst[i][lt], lst[i][rt])] += 1
        if rt == n-1:
            lt += 1
            rt = lt+1
        else:
            rt += 1

for key,value in dict.items():
    if value == m:
        answer+=1

print(answer)
# 4 3
# 3 4 1 2
# 4 3 2 1
# 3 1 4 2

n,m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    for j in range(1, m+1):
        num = i + j
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
lst = sorted(dic.items(),key = lambda x: x[1], reverse=True)

val = lst[0][1]
answer = []
for i in range(len(lst)):
    if lst[i][1] != val:
        break
    else:
        print(lst[i][0], end=' ')







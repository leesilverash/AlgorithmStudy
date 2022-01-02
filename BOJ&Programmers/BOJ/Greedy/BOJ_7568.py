import sys

n = int(sys.stdin.readline().rstrip())

lst = []
for i in range(n):
    lst.append(sys.stdin.readline().rstrip().split())

lst_len = len(lst)
ans = []

for i in range(lst_len):
    cnt = 1
    for j in range(lst_len):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    ans.append(cnt)

for i in ans:
    print(i, end=' ')

import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
lst.sort()

x, y = lst[0][0], lst[0][1]
answer = y-x
for i in range(1, n):
    if lst[i][0] <= y and lst[i][1] <= y:
        continue
    answer += lst[i][1] - lst[i][0]

    if lst[i][0] < y:
        answer-=(y-lst[i][0])

    x = lst[i][0]
    y = lst[i][1]

print(answer)
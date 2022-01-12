# 현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
# 그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
# 만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다
from collections import deque
n = int(input())
lst = []

for i in range(n):
    lst.append(deque(map(int,input().split())))

m = int(input())
for i in range(m):
    x, y, z = map(int, input().split())
    if y == 1:
        lst[x-1].rotate(z)
    else:
        lst[x-1].rotate(-z)
answer = 0
begin, end = 0, n//2+1
for i in range(n//2+1):
    if i < n//2:
        if i == 0:
            answer += sum(lst[i])
            answer += sum(lst[n - i - 1])
        else:
            for j in range(i):
                lst[i].pop()
                lst[i].popleft()
                lst[n - i - 1].pop()
                lst[n - i - 1].popleft()
            answer += sum(lst[i])
            answer += sum(lst[n - i - 1])
    else:
        print(lst[i][i])
        answer += lst[i][i]

print(answer)
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4


# 9
# 64 8 59 87 94 71 66 4 9
# 38 21 30 24 33 65 7 79 27
# 99 10 78 74 84 32 33 74 30
# 4 6 69 53 100 15 23 15 88
# 22 88 8 3 62 75 46 4 41
# 39 64 7 75 91 26 83 32 41
# 100 98 20 100 18 39 90 60 56
# 56 30 94 29 81 76 96 50 11
# 66 88 88 95 13 56 29 13 31
# 5
# 1 0 5
# 3 0 6
# 2 1 5
# 6 0 7
# 5 0 8
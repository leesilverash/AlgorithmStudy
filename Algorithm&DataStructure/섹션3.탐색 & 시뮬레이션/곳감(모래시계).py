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

for i in range(n//2+1):
    if i < n//2:
        if i == 0:
            answer += sum(lst[i])
            answer += sum(lst[n - i - 1])
        else:
            lst[i].pop()
            lst[i].popleft()
            lst[n - i - 1].pop()
            lst[n - i - 1].popleft()
            answer += sum(lst[i])
            answer += sum(lst[n - i - 1])
    else:
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
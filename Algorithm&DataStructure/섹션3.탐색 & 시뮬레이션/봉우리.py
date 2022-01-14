# 지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.

n = int(input())
lst= [[0]*n]
cnt = 0
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.append([0]*n)
for i in lst:
    i.insert(0,0)
    i.append(0)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
            if all(lst[i][j] > lst[i+dx[k]][j+dy[k]] for k in range(4)):
                cnt+=1
print(cnt)

# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input().split())))
#
# mid = n//2
# idx = 0
# ans = sum(lst[mid])
# for i in range(n//2):
#     if i == 0:
#         ans += lst[0][mid]
#         ans += lst[-1][mid]
#     else:
#         for j in range(mid-idx, mid+idx+1):
#             ans += lst[i][j]
#             ans += lst[n-i-1][j]
#     idx += 1
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# print(ans)


from collections import deque

n = int(input())
dx= [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
g = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum = 0
q = deque()
ch[n//2][n//2] = 1
sum += g[n//2][n//2]
q.append((n//2, n//2))
l = 0
while True:
    if l == n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += g[x][y]
                ch[x][y] = 1
                q.append((x, y))
    l+=1
print(sum)

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

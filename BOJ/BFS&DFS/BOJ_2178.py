import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = []
q = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    lst.append(list(sys.stdin.readline().rstrip()))

q = [[0, 0]]
lst[0][0] = 1
while q:
    a, b = q[0][0], q[0][1]
    del q[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and lst[x][y] == "1":
            q.append([x, y])
            lst[x][y] = lst[a][b] + 1
print(lst[n - 1][m - 1])

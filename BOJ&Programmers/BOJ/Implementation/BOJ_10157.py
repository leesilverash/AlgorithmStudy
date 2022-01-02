import sys

x, y = map(int, sys.stdin.readline().rstrip().split(' '))
n = int(sys.stdin.readline().rstrip())
y_idx = y
idx = 1
board = [[0] * x for _ in range(y)]
for i in range(1, x*y+1):
    if y_idx > 0:
        board[-i][0] = i

print(board)
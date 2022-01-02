import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lst.append([x, y])
lst.sort(key=lambda x: (x[0], x[1]))
for i in lst:
    print(i[0], i[1])

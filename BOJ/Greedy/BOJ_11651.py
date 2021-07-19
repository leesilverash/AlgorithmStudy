import sys

n = int(sys.stdin.readline().rstrip())

lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

lst.sort()
lst.sort(key = lambda x: x[1])
for i in lst:
    print(i[0], i[1])
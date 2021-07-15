import sys
n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    n,m = map(str, sys.stdin.readline().rstrip().split())
    lst.append((int(n), m))

lst.sort(key = lambda x : x[0])
for i in lst:
    print(i[0], i[1])


import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
neverSeen = []
neverHeard = []
for i in range(n):
    neverSeen.append(sys.stdin.readline().rstrip())
for i in range(m):
    neverHeard.append(sys.stdin.readline().rstrip())

lst = sorted(list(set(neverSeen)&set(neverHeard)))
print(len(lst))
for i in lst:
    print(i)
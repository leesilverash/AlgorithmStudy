import sys

n,k = map(int, sys.stdin.readline().rstrip().split())
lst = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
print(lst[k-1])
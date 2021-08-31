import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    print(sorted(list(map(int,sys.stdin.readline().rstrip().split())), reverse=True)[2])

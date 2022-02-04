import sys
input = sys.stdin.readline()

p, q = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1,p+1):
    if p % i == 0:
        q -= 1
    if q == 0:
        print(i)
        break
else:
    print(-1)

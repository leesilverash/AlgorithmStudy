import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int,sys.stdin.readline().strip().split()))
stack = []
result = [0]*n

for i in range(n):
    num = int(sys.stding.readline().rstrip())
    if stack:
        if stack[-1] > num:
            result.append()
    else:
        stack.append(num)



import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int,sys.stdin.readline().strip().split()))
stack = []
answer = []
for i, j in enumerate(lst):
    while stack:
        if stack[-1][1] > j:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    else:
        answer.append(0)
    stack.append([i,j])

print(' '.join(map(str,answer)))

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = deque([i for i in range(1,n+1)])
answer = []
while lst:
    lst.rotate(-k+1)
    answer.append(lst.popleft())

s = '<'
for i in range(len(answer)):
    if i != len(answer)-1:
        s+=str(answer[i])+', '
    else:
        s+=str(answer[i])
s+='>'
print(s)

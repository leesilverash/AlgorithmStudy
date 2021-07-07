import sys

s = list(map(str, sys.stdin.readline().rstrip()))
t = list(map(str, sys.stdin.readline().rstrip()))

while(t):
    if t[-1] == 'B':
        t.pop()
        t.reverse()
    elif t[-1] == 'A':
        t.pop()
    if t == s:
        break
answer = 1 if t else 0
print(answer)

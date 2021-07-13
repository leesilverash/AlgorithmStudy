import sys

steps = int(sys.stdin.readline().rstrip())
s = list(map(str, sys.stdin.readline().rstrip()))
count = 0
level = 0
prev = 0
for i in s:
    prev = level
    if i == 'D':
        level -= 1
    else:
        level += 1
    if prev < 0 and level == 0:
        count += 1
print(count)

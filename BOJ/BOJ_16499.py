import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    s = sorted([ch for ch in sys.stdin.readline().rstrip()])
    if ''.join(s) not in lst:
        lst.append(''.join(s))

print(len(lst))

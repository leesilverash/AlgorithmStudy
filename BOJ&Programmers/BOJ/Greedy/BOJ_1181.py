import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    cnt = len(s)
    lst.append((s, cnt))
lst = list(set(lst))
lst.sort(key=lambda x: (x[1], x[0]))

for i in lst:
    print(i[0])

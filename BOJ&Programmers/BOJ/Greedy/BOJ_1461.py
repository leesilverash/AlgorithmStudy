import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
maxnum = abs(min(lst)) if abs(max(lst)) < abs(min(lst)) else abs(max(lst))
neg = []
pos = []
answer = 0
for i in lst:
    neg.append(i) if i < 0 else pos.append(i)
neg.sort()
pos.sort(reverse=True)
for i in range(0, len(pos), m):
    answer+=pos[i]*2
for i in range(0, len(neg), m):
    answer+=abs(neg[i])*2
print(answer-maxnum)

import sys

str = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
lst = []
count = 0

for i in range(n):
    lst.append(sys.stdin.readline().rstrip()*2)

for i in range(len(lst)):
    if str in lst[i]:
        count += 1

print(count)
import sys

A, B = map(int, sys.stdin.readline().strip().split())
answer = 0
list = []
i = 1

while len(list) <= B:
    list += [i]*i
    i += 1
print(list)
answer = sum(list[A-1:B])
print(answer)

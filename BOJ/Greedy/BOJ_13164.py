import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0
dif = []

for i in range(N-1):
    dif.append(lst[i+1] - lst[i])
dif.sort()


for i in range(N-K):
    answer += dif[i]
print(answer)
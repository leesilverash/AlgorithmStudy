from itertools import permutations

n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1]*(n-i)/i
a = list(range(1, n+1))
cnt = 0
for tmp in permutations(a):
    sum = 0
    for l, x in enumerate(tmp):
        sum+=(x*b[l])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break

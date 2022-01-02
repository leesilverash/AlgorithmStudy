import sys

dict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

N, M = map(int, sys.stdin.readline().rstrip().split())
lst = []

for i in range(N, M + 1):
    s = ''.join([dict[c] for c in str(i)])
    lst.append([i, s])
lst.sort(key=lambda x: x[1])

for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print()
    print(lst[i][0], end=' ')

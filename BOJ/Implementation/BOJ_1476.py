import sys

E, S, M = map(int, sys.stdin.readline().rstrip().split())
e, s, m = 1, 1, 1
answer = 1
while True:
    if e == E and s == S and m == M:
        print(answer)
        break
    e += 1
    s += 1
    m += 1

    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    answer += 1

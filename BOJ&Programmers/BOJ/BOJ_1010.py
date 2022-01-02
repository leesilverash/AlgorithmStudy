import sys

T = int(sys.stdin.readline().strip())

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for i in range(T):
    n,m = map(int, sys.stdin.readline().strip().split())
    o = factorial(m-n)
    m = factorial(m)
    n = factorial(n)
    print(m//(n*o))
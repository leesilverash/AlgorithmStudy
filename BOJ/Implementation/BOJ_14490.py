import sys

n, m = map(int, sys.stdin.readline().rstrip().split(':'))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
gcd = gcd(n,m)
print("{}:{}".format(n//gcd, m//gcd))
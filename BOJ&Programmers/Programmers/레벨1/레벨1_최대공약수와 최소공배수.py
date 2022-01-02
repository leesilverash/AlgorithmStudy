def getGCD(n,m):
    while(m):
        n,m = m, n%m
    return n
def getLCM(n,m):
    max = n if n > m else m
    for i in range(max, n*m+1):
        if i % n == 0 and i % m == 0:
            return i
def solution(n, m):
    return [getGCD(n,m), getLCM(n,m)]
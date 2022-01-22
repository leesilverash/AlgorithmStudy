def addDivisors(num):
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

def getMostDivisors(n, m):
    for i in range(n, m + 1):
        for j in range(1, int(i ** 0.5 + 1)):
            rest = i % j
            if rest == 0:
                addDivisors(j)
                addDivisors(i // j)
    dic[1] = 0
    return sorted(dic.items(), key=lambda k: (-k[1], k[0]))[0][0]

dic = {}

n, m = map(int, input().split())
if n > m:
    tmp = m
    m = n
    n = tmp

print(getMostDivisors(n,m))
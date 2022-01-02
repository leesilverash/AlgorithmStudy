def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return int(a * b / gcd(a,b))

def solution(arr):
    answer = 0
    arr.sort()
    tmp = arr[0]
    for i in range(1, len(arr)):
        tmp = lcm(tmp,arr[i])
    answer = tmp
    return answer
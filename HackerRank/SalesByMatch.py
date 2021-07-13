import sys

def sockMerchant(n, ar):
    dic = {}
    answer = 0
    for i in ar:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for key, val in dic.items():
        answer += val // 2
    return answer


n = int(sys.stdin.readline().rstrip())
ar = list(map(int, sys.stdin.readline().rstrip().split()))
print(sockMerchant(n, ar))

import sys
n = int(sys.stdin.readline().rstrip())
check = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    check[num] = check[num]+1

for i in range(10001):
    if check[i] != 0:
        for _ in range(check[i]):
            print(i)

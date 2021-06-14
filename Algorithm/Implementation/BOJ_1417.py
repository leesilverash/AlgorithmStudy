import sys

n = int(sys.stdin.readline().rstrip())
lst = [int(input()) for _ in range(n)]

dasom = lst[0]
lst.pop(0)
if n == 1:
    print(0)
else:
    answer = 0
    while True:
        lst.sort()
        if dasom > lst[-1]:
            print(answer)
            break
        lst[-1] -= 1
        dasom += 1
        answer += 1

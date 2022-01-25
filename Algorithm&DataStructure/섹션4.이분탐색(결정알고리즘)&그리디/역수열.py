n = int(input())
lst = list(map(int, input().split()))
a = [0] * n

def solve(idx, num):
    cnt = 0
    for i in range(n):
        if a[i] == 0:
            cnt += 1
        if cnt > num:
            a[i] = idx
            break

    return cnt

for i in range(n):
    solve(i+1, lst[i])

print(a)

# 8
# 5 3 4 0 2 1 1 0
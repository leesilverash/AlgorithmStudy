n = int(input())
lst = list(map(int,input().split()))
m = int(input())
lst.sort()
for i in range(m):
    lst[0] += 1
    lst[-1] -= 1
    lst.sort()

print(lst[-1] - lst[0])

# 10
# 69 42 68 76 40 87 14 65 76 81
# 50

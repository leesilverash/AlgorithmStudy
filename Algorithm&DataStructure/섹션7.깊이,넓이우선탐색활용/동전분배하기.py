def dfs(l):
    global res
    if l == n:
        cha = max(money) - min(money)
        if cha < res:
            print(cha)
            return
    else:
        for i in range(3):
            money[i] += coin[l]
            dfs(l+1)
            money[i] -= coin[l]
            dfs(l)


n = int(input())
coin = []
money = [0] * 3
res = 214700000

for i in range(n):
   coin.append(int(input()))

dfs(0)
print(res)

# 7
# 8
# 9
# 11
# 12
# 23
# 15
# 17
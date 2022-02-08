n = int(input())
dic = dict()
for _ in range(n):
    dic[input()] = 0
for _ in range(n-1):
    dic[input()] = 1
for k,v in dic.items():
    if v == 0:
        print(k)

# 5
# big
# good
# sky
# blue
# mouse
# sky
# good
# mouse
# big
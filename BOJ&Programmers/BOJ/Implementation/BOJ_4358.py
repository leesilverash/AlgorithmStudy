import sys
dic = {}
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1
sum = sum(dic.values())
lst = sorted(list(dic.keys()))
for i in lst:
    print('%s %.4f' %(i, dic[i]/sum*100))
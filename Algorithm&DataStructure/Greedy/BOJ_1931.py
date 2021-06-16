N = int(input())
count = 0
list = []
for i in range(N):
    x, y = map(int, input().split())
    list.append((x,y))
list.sort()
list = sorted(list, key = lambda x : x[1])
prev = 0
for i, j in list:
    if i >= prev:
        count+=1
        prev = j
print(count)


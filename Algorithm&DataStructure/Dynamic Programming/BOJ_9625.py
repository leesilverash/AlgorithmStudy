K = int(input())
sum = []
for i in range(K+1):
    if i < 2:
        sum.append(i)
    else:
        sum.append(sum[-1]+sum[-2])

print(sum[-2], sum[-1])

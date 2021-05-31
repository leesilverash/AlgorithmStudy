eq = input()
nums = eq.split('-')
numlist=[]
for num in nums:
    tmplist = num.split('+')
    sum = 0
    for i in tmplist:
        sum+=int(i)
    numlist.append(sum)
answer = numlist[0]

for i in range(1, len(numlist)):
    answer-=numlist[i]

print(answer)
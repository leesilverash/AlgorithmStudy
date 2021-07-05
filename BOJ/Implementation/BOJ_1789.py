import sys

s = int(sys.stdin.readline().rstrip())
sum = 0
count = 0
while sum < s:
    count+=1
    sum+=count
if sum > s:
    count-=1
print(count)

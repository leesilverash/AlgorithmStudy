# 투 포인터 알고리즘
N = int(input())
data = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
left, right = 0, N-1

while left < right:
    if data[left] + data[right] == x:
        answer+=1
        left+=1
    elif data[left] + data[right] > x:
        right-=1
    else:
        left+=1

print(answer)
# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. N의 크기는 항상 홀수이다.
# 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
# 현수과 수확하는 사과의 총 개수를 출력하세요.

n = int(input())
lst = []
answer = 0
med = int(n//2)
for i in range(n):
    lst.append(list(map(int,input().split())))

for i in range(n//2+1):
    if i == 0:
        answer += lst[i][med]
        answer += lst[n-1][med]
    elif i < med:
        answer += sum(lst[i][med-i:med+i+1])
        answer += sum(lst[n-i-1][med-i:med+i+1])
    else:
        answer += sum(lst[i])

print(answer)

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

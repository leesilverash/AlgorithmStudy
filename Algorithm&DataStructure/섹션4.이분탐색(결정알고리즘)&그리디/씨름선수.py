n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
answer = 0
for i in range(n):
    weight = lst[i][1]
    flag = True
    if i == n-1:
        answer += 1
    else:
        for j in range(i+1, n):
            if lst[j][1] > weight:
                flag = 0
                break
        if flag == True:
            answer += 1
print(answer)

# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60
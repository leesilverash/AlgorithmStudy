n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
for i in range(n):
    sum = lst[i]
    for j in range(i+1, n):
        if sum < m:
            sum += lst[j]
            if sum == m:
                answer += 1
                break
        else:
            if sum == m:
                answer += 1
                break
            break
print(answer)



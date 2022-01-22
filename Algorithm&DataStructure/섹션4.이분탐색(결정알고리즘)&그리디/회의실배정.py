n = int(input())
lst = []
for _ in range(n):
    start, end = map(int, input().split())
    lst.append([start,end])
lst.sort(key= lambda x: x[1])
answer = 1
end = lst[0][1]
for i in range(1, n):
    if end <= lst[i][0]:
        end = lst[i][1]
        answer += 1
print(answer)



# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7

# 20
# 18 19
# 2 20
# 4 21
# 2 22
# 12 15
# 12 23
# 2 8
# 5 20
# 22 23
# 1 5
# 13 21
# 16 20
# 9 19
# 5 9
# 14 20
# 16 22
# 11 12
# 4 16
# 21 23
# 11 13
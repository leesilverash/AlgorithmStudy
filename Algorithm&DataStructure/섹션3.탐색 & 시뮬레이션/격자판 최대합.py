n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

def findHorizontalMax():
    max = 0
    for i in range(n):
        print(lst[i], sum(lst[i]))
        if sum(lst[i]) > max:
            max = sum(lst[i])
    return max

def findVerticalMax():
    max = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += lst[j][i]
        if sum > max:
            max = sum
    return max

def findDiagonalMax():
    positive = 0
    negative = 0
    for i in range(n):
        negative += lst[i][i]
        positive += lst[n - 1 - i][i]

    return max(positive, negative)

print(max(findDiagonalMax(), findVerticalMax(), findHorizontalMax()))

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

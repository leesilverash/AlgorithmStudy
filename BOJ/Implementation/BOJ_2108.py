import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline().rstrip()))


def getMean():
    return round(sum(numbers) / len(numbers))


def getMedian():
    return sorted(numbers)[len(numbers) // 2]


def getMode():
    cnt = Counter(numbers)
    lst = sorted(list(cnt.items()), key=lambda x: x[1], reverse=True)
    modes = []
    maxNum = lst[0][1]

    for i in range(len(lst)):
        if lst[i][1] == maxNum:
            modes.append(lst[i])

    return modes[0][0] if len(modes) == 1 else sorted(modes, key=lambda x: x[0])[1][0]


def getDifference():
    return max(numbers) - min(numbers)


print(getMean())
print(getMedian())
print(getMode())
print(getDifference())

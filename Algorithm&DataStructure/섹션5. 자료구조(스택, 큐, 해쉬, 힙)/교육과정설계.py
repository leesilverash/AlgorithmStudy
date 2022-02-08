from collections import deque
order = (input())
num = int(input())
lst = [input() for _ in range(num)]
for i in range(len(lst)):
    tmp = deque(order)
    for j in lst[i]:
        if tmp and j == tmp[0]:
            tmp.popleft()
    if len(tmp) > 0:
        print("#{} No".format(i+1))
    else:
        print("#{} YES".format(i+1))


# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA
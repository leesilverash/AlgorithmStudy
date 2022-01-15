lst = []
for i in range(9):
    lst.append(list(map(int, input().split())))

def check():
    for i in range(9):
        if(len(set(lst[i]))) != 9:
            return False
        tmp1 = [0] * 10
        tmp2 = [0] * 10
        for j in range(9):
            tmp1[lst[i][j]], tmp2[lst[j][i]] = 1, 1
        if sum(tmp1) != 9 or sum(tmp2) != 9:
            return False

    a1, a2, b1, b2 = 0, 3, 0, 3

    while a2 < 10:
        tmp = {}
        for i in range(a1, a2):
            for j in range(b1, b2):
                if tmp.get(lst[i][j]):
                    return False
                else:
                    tmp[lst[i][j]] = 1
        a1 += 3
        a2 += 3
        b1 += 3
        b2 += 3
    return True

if check() == True:
    print('YES')
else:
    print('NO')

# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7
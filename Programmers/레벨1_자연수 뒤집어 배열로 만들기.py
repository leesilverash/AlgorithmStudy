def solution(n):
    lst = []
    n = str(n)
    for i in range(len(n), 0, -1):
        lst.append(int(n[i - 1]))

    return lst
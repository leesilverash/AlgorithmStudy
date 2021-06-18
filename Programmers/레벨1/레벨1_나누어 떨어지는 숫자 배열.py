def solution(strings, n):
    answer = []
    tmp = []
    for i in strings:
        tmp.append([i[n], i])
    tmp.sort()
    for i in tmp:
        answer.append(i[1])
    return answer
def getGrade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    lst = []
    for i in range(len(scores)):
        lst = []

        for j in range(len(scores[i])):
            lst.append(scores[j][i])
        if lst.count(lst[i]) == 1:
            if min(lst) == lst[i] or max(lst) == lst[i]:
                lst.remove(lst[i])
        grade = getGrade(sum(lst) / len(lst))
        answer += grade

    return answer
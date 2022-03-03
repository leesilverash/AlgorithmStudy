from itertools import permutations


def solution(k, dungeons):
    answer = 0
    lst = list(permutations(dungeons))

    for i in lst:
        cnt = 0
        energy = k
        for j in range(len(i)):
            if i[j][0] <= energy:
                energy -= i[j][1]
                cnt += 1
        if cnt > answer:
            answer = cnt
        if answer == len(dungeons):
            break

    return answer
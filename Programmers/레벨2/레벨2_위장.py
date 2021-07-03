def solution(clothes):
    answer = {}
    cnt = 1
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt-1
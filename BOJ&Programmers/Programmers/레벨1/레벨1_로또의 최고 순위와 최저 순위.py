def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    count = 0
    zeroCount = 0
    for i in lottos:
        if i == 0:
            zeroCount += 1
        if i in win_nums:
            count += 1
    if count < 5:
        answer.append(rank[count+zeroCount])
    else:
        answer.append(rank[6])
    answer.append(rank[count])
    return answer
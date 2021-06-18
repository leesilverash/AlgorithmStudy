def solution(N, stages):
    dict = {}
    count = len(stages)
    for i in range(1,N+1):
        num = stages.count(i)
        dict[i] = 0 if num == 0 else abs(num/count)
        count-=num

    return sorted(dict, key = lambda x : dict[x], reverse=True)
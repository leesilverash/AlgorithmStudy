import math
def solution(brown, yellow):
    answer = []
    lst = []
    num = brown+yellow
    for i in range(1, math.ceil(num/2)):
        if num % i == 0 and i >= num//i:
            lst.append([i,num//i])
    for i in lst:
        if i[0]*2 + i[1]*2-4 == brown:
            answer=i
    return answer
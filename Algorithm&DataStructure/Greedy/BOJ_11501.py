T = int(input())


def getAnswer(lst):
    st = []
    max = lst[-1]
    answer = 0
    for i in range(len(lst)-1, -1, -1):
        if max > lst[i]:
            answer+=max-lst[i]
        elif max <= lst[i]:
            max = lst[i]
    return answer


for i in range(T):
    num = int(input())
    lst = list(map(int, input().split()))
    print(getAnswer(lst))

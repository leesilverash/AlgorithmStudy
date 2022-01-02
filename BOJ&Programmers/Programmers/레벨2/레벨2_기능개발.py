import math
def solution(progresses, speeds):
    answer = []
    lst= []
    st = []
    for i in range(len(progresses)):
        lst.append(math.ceil((100-progresses[i])/speeds[i]))
    count = 1
    for i in range(len(lst)):
        if st:
            if st[-1] < lst[i]:
                answer.append(count)
                count = 1
                st.append(lst[i])
            else:
                count+=1
        else:
            st.append(lst[i])
        if i == len(lst)-1:
            answer.append(count)

    return answer
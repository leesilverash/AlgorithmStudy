from collections import deque
n = int(input())
answer = ''
len = 0
deq = deque(map(int,input().split()))
curr = 0
for i in range(n):
    if deq[0] > curr and deq[-1] > curr:
        if deq[0] > deq[-1]:
            answer += 'R'
            len += 1
            curr = deq.pop()
        else:
            answer+='L'
            len += 1
            curr = deq.popleft()
    elif deq[0] > curr:
        len += 1
        answer += 'L'
        curr = deq.popleft()
    elif deq[-1] > curr:
        len += 1
        answer += 'R'
        curr = deq.pop()
    else:
        break

print(len, answer)


# 5
# 2 4 5 1 3
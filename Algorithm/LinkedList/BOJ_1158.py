from collections import deque
deq = deque()
N, K = map(int, input().split())
for i in range(1, N+1):
    deq.append(i)
answer = []
while deq:
    deq.rotate(1-K)
    answer.append(deq.popleft())

result = ''
for i in range(len(answer)):
    if i != len(answer)-1:
        result += str(answer[i])+', '
    else:
        result += str(answer[i])
a = '{}{}{}'.format('<',result,'>')
print(a)



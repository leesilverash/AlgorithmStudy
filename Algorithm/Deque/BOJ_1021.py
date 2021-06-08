import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())  # N = 큐의 길이, M = 찾으려고 하는 값의 수
deq = deque(range(1, int(N) + 1))  # deq = 1-M 까지의 큐
target = list(map(int, sys.stdin.readline().strip().split()))  # 찾으려고 하는 값 리스트
answer = 0  # 연산 갯수

for i in target:  # 타겟을 다 찾을 때 까지 반복
    target_idx = deq.index(i)
    if target_idx <= len(deq) // 2:
        deq.rotate(target_idx * -1)
        answer += target_idx
        deq.popleft()
    else:
        deq.rotate(len(deq) - target_idx)
        answer += len(deq) - target_idx
        deq.popleft()
print(answer)

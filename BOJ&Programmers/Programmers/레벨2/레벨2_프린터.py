from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    idx = location

    while len(priorities) != 0:
        print(priorities)
        if idx == 0:
            if priorities[0] == max(priorities):
                priorities.popleft()
                answer += 1
                break
            else:
                priorities.append(priorities.popleft())
                idx = len(priorities)
        else:
            if priorities[0] == max(priorities):
                priorities.popleft()
                answer += 1
            else:
                priorities.append(priorities.popleft())
        idx -= 1
    return answer
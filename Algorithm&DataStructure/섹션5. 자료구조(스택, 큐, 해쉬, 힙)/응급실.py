from collections import deque
n, m = map(int, input().split())
people = deque([(pos, val) for pos, val in enumerate(map(int, input().split()))])
answer = 0

while True:
    cur = people.popleft()
    cur_pos = cur[0]
    cur_val = cur[1]
    if any(cur_val < x[1] for x in people):
        people.append(cur)
    else:
        answer += 1
        if cur_pos == m:
            break
print(answer)



# 5 2
# 60 50 70 80 90
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
s = deque([sys.stdin.readline().rstrip() for i in range(n)])
answers = []

def compare(n, m):
    answer = True
    while n <= m:
        if s[n] == s[m]:
            n += 1
            m -= 1
        elif s[n] < s[m]:
            return True
        else:
            return False
    return answer

while s:
    answers.append(s.popleft()) if compare(0, len(s)-1) else answers.append(s.pop())

length = len(answers)
if length <= 80:
    print(''.join(answers))
else:
    for i in range(length//80+1):
        if i == length//80:
            print(''.join(answers[i*80:]))
        else:
            print(''.join(answers[i*80:(i+1)*80]))


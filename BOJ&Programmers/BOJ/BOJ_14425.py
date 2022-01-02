import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
word_list = []
answer = 0

for i in range(n):
    word_list.append(sys.stdin.readline().rstrip())

for i in range(m):
    word = sys.stdin.readline().rstrip()
    if word in word_list:
        answer += 1
print(answer)
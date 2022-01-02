import sys
import string

word = sys.stdin.readline().strip()
alpha_list = list(string.ascii_lowercase)
answer = [0]*len(alpha_list)
for alpha in word:
    answer[alpha_list.index(alpha)] += 1

for n in answer:
    print(n, end=" ")

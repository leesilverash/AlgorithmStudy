import itertools
import sys
from itertools import combinations

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

def solution(s1, s2):
    for i in range(len(s1), -1, -1):
        lst = set(list(combinations(s1, i)))
        for j in lst:
            a = ''.join(j)
            if a in s2:
                return len(a)
print(solution(s1,s2))






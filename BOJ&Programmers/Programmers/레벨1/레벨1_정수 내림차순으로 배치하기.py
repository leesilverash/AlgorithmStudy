def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))
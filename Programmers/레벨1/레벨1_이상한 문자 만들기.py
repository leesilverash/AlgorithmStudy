def solution(s):
    answer = []
    for ch in s.split(' '):
        result = ''
        for i, j in enumerate(ch):
            if i%2 == 0:
                result+=j.upper()
            else:
                result+=j.lower()
        answer.append(result)
    return ' '.join(answer)
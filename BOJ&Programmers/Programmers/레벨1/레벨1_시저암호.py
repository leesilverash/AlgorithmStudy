def solution(s, n):
    answer = ''
    for i in s:
        dif = ord(i) + n
        if i.islower():
            if dif > 122:
                answer += chr(dif - 26)
            else:
                answer += chr(dif)
        elif i.isupper():
            if dif > 90:
                answer += chr(dif - 26)
            else:
                answer += chr(dif)
        else:
            answer += i
    return answer
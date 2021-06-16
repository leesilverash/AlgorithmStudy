def solution(phone_number):
    answer = ''
    for i,j in enumerate(phone_number):
        if len(phone_number) - i > 4:
            answer+='*'
        else:
            answer+=j
    return answer
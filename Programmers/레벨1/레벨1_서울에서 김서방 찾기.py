def solution(seoul):
    answer = ''
    for i, value in enumerate(seoul):
        if value == 'Kim':
             return "김서방은 {}에 있다".format(i)
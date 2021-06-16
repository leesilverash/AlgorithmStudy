def solution(a, b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [(1,31), (2,29), (3,31), (4,30), (5,31), (6, 30), (7,31), (8,31), (9,30), (10,31), (11,30), (12,31)]

    days = b-1
    for i in range(a-1):
        days+=month[i][1]
    num = days%7
    answer = day[num]
    return answer
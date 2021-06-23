def solution(people, limit):
    answer = 0
    i = 0
    j = len(people)-1
    people.sort()
    while i <= j:
        if people[i] + people[j] <= limit:
            i+=1
        j-=1
        answer+=1
    return answer
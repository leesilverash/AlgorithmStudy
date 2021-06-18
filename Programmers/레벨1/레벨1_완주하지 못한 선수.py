def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    i = 0
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]
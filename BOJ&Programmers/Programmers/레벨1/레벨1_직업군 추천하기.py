def solution(table, languages, preference):
    answer = ''
    score = {}
    for i in range(len(languages)):
        score[languages[i]] = preference[i]
    max_score = 0
    for information in table:
        inf = information.split()
        current_score = {inf[i]: 6 - i for i in range(1, len(inf))}
        total_score = 0

        for lan in score.keys():
            if current_score.get(lan):
                total_score += (current_score[lan] * score[lan])

        if total_score == max_score:
            if answer > inf[0]:
                answer = inf[0]

        if total_score > max_score:
            max_score = total_score
            answer = inf[0]

    return answer
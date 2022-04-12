def solution(genres, plays):
    answer = []
    dic_genres = {}
    for i in range(len(genres)):
        if genres[i] in dic_genres:
            a = dic_genres[genres[i]][2]
            a.append([i, plays[i]])
            dic_genres[genres[i]] = [dic_genres[genres[i]][0]+plays[i], dic_genres[genres[i]][1]+1, a]
        else:
            dic_genres[genres[i]] = [plays[i], 1, [[i, plays[i]]]]

    genre_sum = sorted(dic_genres.items(), key = lambda x : x[1], reverse=True)

    for genre in genre_sum:
        if genre[1][1] == 1:
            answer.append(genre[1][2][0][0])
        else:
            tmp = genre[1][2]
            tmp.sort(key = lambda x: x[1], reverse=True)
            for i in range(2):
                answer.append(tmp[i][0])

    return answer
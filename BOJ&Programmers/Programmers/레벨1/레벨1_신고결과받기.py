def solution(id_list, report, k):
    setReport = set(report)
    count = {}
    users = {}
    for i in range(len(id_list)):
        users[id_list[i]] = i

    for i in setReport:
        user, block = i.split()
        if block in count:
            count[block].append(users[user])
        else:
            count[block] = [users[user]]

    answer = [0] * len(id_list)

    for value in count.values():
        if len(value) >= k:
            for i in value:
                answer[i] += 1

    return answer
def solution(record):
    answer = []
    answers = []
    db = {}
    for user in record:
        action = user.split(' ')[0]
        uid = user.split(' ')[1]
        if action == 'Leave':
            answer.append([uid, action])
        elif action == 'Enter':
            name = user.split(' ')[2]
            db[uid] = name
            answer.append([uid, action])
        else:
            name = user.split(' ')[2]
            db[uid] = name

    for ans in answer:
        act = '들어왔습니다.' if ans[1] == 'Enter' else '나갔습니다.'
        result = '{}님이 {}'.format(db[ans[0]], act)
        answers.append(result)

    return answers
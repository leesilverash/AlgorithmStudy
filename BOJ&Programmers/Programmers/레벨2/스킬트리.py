def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        orders = list(skill) # ['c','b','d']
        a = list(s) # ['b','a','c','d','e']
        idx = 0
        flag = 1
        for c in a:
            if c in orders:
                if c == orders[idx]:
                    idx += 1
                else:
                    flag = 0
                    break
        if flag == 1:
            answer += 1

    return answer
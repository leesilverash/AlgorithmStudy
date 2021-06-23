def solution(n, words):
    lst = []
    for i in range(len(words)):
        if lst:
            if words[i] in lst:
                num = i % n + 1
                if num == 0:
                    num = 1
                return [num, i // n + 1]
            elif words[i].startswith(lst[-1][-1]):
                lst.append(words[i])
            else:
                num = i % n + 1
                if num == 0:
                    num = 1
                return [num, i // n + 1]
        else:
            lst.append(words[i])

    return [0, 0]

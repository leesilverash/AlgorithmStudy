def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    str_list = []
    specChar = ['-', '_', '.']
    for i in range(len(new_id)):
        if new_id[i].isdigit() or new_id[i].isalpha() or new_id[i] in specChar:
            if len(str_list) == 0:
                if new_id[i] == '.':
                    continue
                else:
                    str_list.append(new_id[i])
            else:
                if new_id[i] == '.':
                    if str_list[-1] != '.':
                        str_list.append(new_id[i])
                else:
                    # str_list[-1] != new_id[i]:
                    str_list.append(new_id[i])
        else:
            continue
    while True:
        if str_list and str_list[-1] == '.':
            str_list.pop()
        elif len(str_list) == 0:
            str_list.append('a')
        elif len(str_list) > 15:
            str_list.pop()
        elif len(str_list) < 3:
            str_list.append(str_list[-1])
        else:
            break
    for i in range(len(str_list)):
        answer += str_list[i]

    return answer
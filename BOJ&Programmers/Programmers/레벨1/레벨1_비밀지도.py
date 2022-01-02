def decode(num, n):
    lst = []
    code = str(format(num, 'b'))
    while len(code) < n:
        code = '0' + code
    for i in code:
        if i == '1':
            lst.append('#')
        elif i == '0':
            lst.append(' ')
    return lst


def solve(lst1, lst2):
    answer = []
    for i in range(len(lst1)):
        result = ''
        for j in range(len(lst1)):
            if lst1[i][j] != '#' and lst2[i][j] != '#':
                result += ' '
            else:
                result += '#'
        answer.append(result)
    return answer


def solution(n, arr1, arr2):
    lst1 = []
    lst2 = []

    for i in range(n):
        lst1.append(decode(arr1[i], n))

    for j in range(n):
        lst2.append(decode(arr2[j], n))

    return solve(lst1, lst2)
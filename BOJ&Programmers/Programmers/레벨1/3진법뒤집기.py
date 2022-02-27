def solution(n):
    def convert(n):
        tmp = ''
        while n > 0:
            n, mod = divmod(n, 3)
            tmp += str(mod)
        return tmp

    answer = convert(n)

    return int(answer, 3)

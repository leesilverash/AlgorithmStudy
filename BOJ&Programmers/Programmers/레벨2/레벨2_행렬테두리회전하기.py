def solution(rows, columns, queries):
    answer = []
    n = 1
    minVal = 1000000
    table = [[0 for col in range(columns)] for row in range(rows)]
    for i in range(rows):
        for j in range(columns):
            table[i][j] = n
            n += 1

    for x1, y1, x2, y2 in queries:
        tmp = table[x1 - 1][y1 - 1]
        minVal = tmp

        # left
        for k in range(x1 - 1, x2 - 1):
            t = table[k + 1][y1 - 1]
            table[k][y1 - 1] = t
            minVal = min(minVal, t)

        # bottom
        for k in range(y1 - 1, y2 - 1):
            t = table[x2 - 1][k + 1]
            table[x2 - 1][k] = t
            minVal = min(minVal, t)

        # right
        for k in range(x2 - 2, x1 - 2, -1):
            t = table[k][y2 - 1]
            table[k + 1][y2 - 1] = t
            minVal = min(minVal, t)

        # top
        for k in range(y2 - 1, y1, -1):
            t = table[x1 - 1][k - 1]
            table[x1 - 1][k] = t
            minVal = min(minVal, t)

        table[x1 - 1][y1] = tmp
        answer.append(minVal)

    return answer

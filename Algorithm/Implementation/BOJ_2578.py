import sys

board = []
num_list = []
answer = 1
bingo = 0
for i in range(5):
    board.extend(list(map(int, sys.stdin.readline().strip().split())))
for i in range(5):
    num_list.extend(list(map(int, sys.stdin.readline().strip().split())))


def seroBingo(board):
    count = 0
    for i in range(5):
        if sum(board[i::5]) == 0:
            count += 1
    return count


def garoBingo(board):
    count = 0
    i = 0
    j = i + 5
    for _ in range(5):
        if sum(board[i:j]) == 0:
            count += 1
        i += 5
        j = i + 5
    return count


def diagonal1(board):
    j = 4
    sum = 0
    count = 0
    for i in range(5):
        sum += board[j]
        j += 4
    if sum == 0:
        return 1
    else:
        return 0


def diagonal2(board):
    if sum(board[0::6]) == 0:
        return 1
    else:
        return 0


def bingoCount(board):
    garo = garoBingo(board)
    sero = seroBingo(board)
    diag1 = diagonal1(board)
    diag2 = diagonal2(board)
    # print('garo',garo)
    # print('sero',sero)
    # print('d1',diag1)
    # print('d2',diag2)
    return garo + sero + diag1 + diag2


for i, num in enumerate(num_list):
    board[board.index(num)] = 0
    if i >= 10:
        bingo = bingoCount(board)
        if bingo >= 3:
            break
    answer += 1

# print(board)
print(answer)

# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

lst = [list(map(int,input().split())) for _ in range(7)]

answer = 0
for i in range(7):
    for j in range(3):
        if lst[i][j] == lst[i][j+4] and lst[i][j+1] == lst[i][j+3]:
            answer += 1
        if lst[j][i] == lst[j+4][i] and lst[j+1][i] == lst[j+3][i]:
            answer += 1
print(answer)

# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
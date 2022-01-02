def solution(board, moves):
    st = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                st.append(board[j][i-1])
                board[j][i-1] = 0
                if len(st) >= 2:
                    if st[-1] == st[-2]:
                        st.pop()
                        st.pop()
                        answer += 2
                break
    return answer
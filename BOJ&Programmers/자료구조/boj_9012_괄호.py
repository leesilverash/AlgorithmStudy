import sys

n = int(sys.stdin.readline().rstrip())

def checkVPS(parenthesis):
    st = []
    isVPS = True
    for ch in parenthesis:
        if ch == '(':
            st.append(ch)
        else:
            if st:
                st.pop()
            else:
                isVPS = False
    if st:
        isVPS = False
    return isVPS

for _ in range(n):
    print('YES') if checkVPS(sys.stdin.readline().rstrip()) is True else print('NO')

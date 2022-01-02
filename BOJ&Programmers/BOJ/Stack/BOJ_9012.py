import sys

n = int(sys.stdin.readline().rstrip())


for i in range(n):
    lst = list(map(str, sys.stdin.readline().rstrip()))
    st = []
    for i in range(len(lst)):
        if st:
            if lst[i] == '(':
                st.append(lst[i])
            else:
                if st[-1] == '(':
                    st.pop()
        else:
            st.append(lst[i])
    print('YES') if len(st) == 0 else print('NO')


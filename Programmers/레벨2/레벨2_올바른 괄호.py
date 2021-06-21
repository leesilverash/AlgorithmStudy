
def solution(s):
    answer = True
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        elif len(st) == 0 and i == ')':
            return False
        else:
            if st and st[-1] == '(':
                st.pop()

    return True if len(st) == 0 else False
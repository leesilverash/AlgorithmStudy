def solution(number, k):
    st = []
    count = k
    for i in number:
        while st and st[-1] < i and count > 0:
            st.pop()
            count -= 1
        st.append(i)
    for i in range(count):
        st.pop()

    return ''.join(st)
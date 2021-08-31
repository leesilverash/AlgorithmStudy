import sys

s = [i for i in sys.stdin.readline().rstrip()]

st = []

for i in s:
    if len(st) == 0:
        st.append(i)
    else:
        if st[-1] == '(' and i == ')':
            st.pop()
        else:
            st.append(i)
print(len(st))
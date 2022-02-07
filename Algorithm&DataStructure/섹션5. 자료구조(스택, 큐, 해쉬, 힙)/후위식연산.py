a = list(input())
st = []
def solve(x, y, op):
    if op == '+':
        st.append(y + x)
    elif op == '-':
        st.append(y - x)
    elif op == '*':
        st.append(y * x)
    elif op == '/':
        st.append(y / x)

for i in range(len(a)):
    if a[i].isdecimal():
        st.append(int(a[i]))
    else:
        x = st.pop()
        y = st.pop()
        solve(x, y, a[i])
print(st[0])
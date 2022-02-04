paren = input()
st = []
answer = 0

for i in range(len(paren)):
    if paren[i] == '(':
        st.append(paren[i])
    else:
        st.pop()
        if paren[i-1] == '(':
            answer += len(st)
        else:
            answer += 1
print(answer)

# ()(((()())(())()))(())
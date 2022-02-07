eq = input()
st = []
answer = ''
for i in eq:
    if i.isdecimal():
        answer += i
    else:
        if i == '(':
            st.append(i)
        elif i == '*' or i == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                answer += st.pop()
            st.append(i)
        elif i == '+' or i == '-':
            while st and st[-1] != '(':
                answer += st.pop()
            st.append(i)
        else:
            while st and st[-1] != '(':
                answer += st.pop()
            st.pop()
while st:
    answer += st.pop()

print(answer)
# 3+5*2/(7-2)
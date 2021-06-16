import sys


while True:
    str = sys.stdin.readline().rstrip()
    st = []
    isTrue = True
    for ch in str:
        if ch == '(' or ch =='[':
            st.append(ch)
        elif ch == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                isTrue = False
                break
        elif ch == ']':
            if st and st[-1] == '[':
                st.pop()
            else:
                isTrue = False
    if str == '.':
        break
    if isTrue == True and len(st)==0:
        print('yes')
    else:
        print('no')



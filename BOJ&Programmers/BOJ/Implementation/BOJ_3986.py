import sys

n = int(sys.stdin.readline().rstrip())
answer = 0

for i in range(n):
    word = sys.stdin.readline().rstrip()
    st = []
    for ch in word:
        if len(st) != 0 and st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
    if len(st) == 0:
        answer +=1
print(answer)




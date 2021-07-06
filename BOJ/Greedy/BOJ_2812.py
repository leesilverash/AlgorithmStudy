import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
num = sys.stdin.readline().rstrip()
lst = [int(num[i]) for i in range(len(num))]
st = []
count = 0
for i in range(len(lst)):
    while count < k and st:
        if st[-1] < num[i]:
            st.pop()
            count += 1
        else:
            break
    st.append(num[i])

print(''.join(st[:n-k]))

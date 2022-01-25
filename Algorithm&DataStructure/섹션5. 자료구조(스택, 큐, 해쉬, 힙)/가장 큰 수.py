n, m = input().split()
lst = list(n)
cnt = 0
st = []
idx = 0
for i in range(len(lst)):
    if cnt < int(m):
        if len(st) == 0:
            st.append(lst[i])
        else:
            while len(st) > 0 and st[-1] < lst[i]:
                if cnt == int(m):
                    break
                st.pop()
                cnt += 1
            st.append(lst[i])
    else:
        idx = i
        break
print(''.join(st) + ''.join(lst[i:]))

# 5276823 3

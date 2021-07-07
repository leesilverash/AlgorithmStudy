import sys

s = sys.stdin.readline().rstrip()
answer = ''
lst = s.split('.')
for i in range(len(lst)):
    if len(lst[i]) % 4 == 0:
        answer+='A'*len(lst[i])
    elif len(lst[i]) % 2 == 0:
        A = 4 * (len(lst[i])//4)
        B = len(lst[i])%4
        answer +='A'*A
        answer +='B'*B
    else:
        answer = -1
        break
    if i != len(lst)-1:
        answer += '.'

print(answer)
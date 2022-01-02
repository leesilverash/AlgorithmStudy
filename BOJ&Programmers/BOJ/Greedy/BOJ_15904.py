import sys, re

s = sys.stdin.readline().rstrip()
ucpc = ['U', 'C', 'P','C']
ans = True
for i in range(len(ucpc)):
    if ucpc[i] in s:
        s = s[s.find(ucpc[i])+1:]
    else:
        ans = False
        break
print('I love UCPC') if ans else print('I hate UCPC')



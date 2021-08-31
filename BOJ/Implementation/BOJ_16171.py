import sys

s = sys.stdin.readline().rstrip()
k = sys.stdin.readline().rstrip()
lst = []

for ch in s:
    if (ord(ch) >= 65 and ord(ch) < 91) or (ord(ch) >= 97 and ord(ch) < 123):
        lst.append(ch)

word = ''.join(lst)

print(1 if k in word else 0)

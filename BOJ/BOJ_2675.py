n = int(input())
for i in range(n):
    P, S = input().split()
    for j in range(len(S)):
        print(S[j]*int(P), end='')
    print()

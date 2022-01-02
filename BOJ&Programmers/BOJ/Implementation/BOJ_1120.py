A, B = input().split()

answer = 50

for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            cnt += 1
    if cnt < answer:
        answer = cnt

print(answer)
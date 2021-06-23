N, K = map(int,input().split())
list_M = [0]*6
list_W = [0]*6
answer = 0

for i in range(N):
    S, Y = map(int,input().split())
    if S == 1:
        list_M[Y-1]+=1
    else:
        list_W[Y-1]+=1

for i in list_M:
    answer += i // K
    if i%K != 0:
        answer+=1

for i in list_W:
    answer += i // K
    if i % K != 0:
        answer += 1
print(answer)


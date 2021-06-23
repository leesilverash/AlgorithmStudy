N = int(input())
A = list(map(int, input().split()))
B = []
answer = 0
A.sort()
for i in range(N):
    answer += A[i]
    B.append(answer)
print(sum(B))
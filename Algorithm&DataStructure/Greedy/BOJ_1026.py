N =int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
A.sort()
for i in range(N):
    count+= A[i]*max(B)
    B.remove(max(B))

print(count)
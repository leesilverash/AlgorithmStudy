N, K = map(int, input().split())
arr=[]
for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)

arr.sort()
if K > len(arr):
    print(0)
else:
    print(arr[K-1])

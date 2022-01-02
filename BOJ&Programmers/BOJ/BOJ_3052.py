arr=[]
answer=[]
for i in range(10):
    arr.append(int(input())%42)
    if arr[i] not in answer:
        answer.append(arr[i])
print(len(answer))



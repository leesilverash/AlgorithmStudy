N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
answer = 0
list.reverse()

for i in range(len(list)):
    if list[0] < len(list):
        break
    else:
        if i == 0:
            continue
        if list[i] >= list[i-1]:
            answer += (list[i]-list[i-1]+1)
            list[i] = list[i-1]-1
print(answer)
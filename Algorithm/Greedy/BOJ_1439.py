N = input()
count = 0
for i in range(len(N)-1):
    if N[i] != N[i+1]:
        count+=1
print((count+1)//2)
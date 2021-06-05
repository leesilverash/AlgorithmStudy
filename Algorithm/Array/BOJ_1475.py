N = list(input())
frequency = [0]*10
answer = 0
sixnine= 0
for i in set(N):
    frequency[int(i)] = N.count(i)
    if i == '6' or i == '9':
        frequency[int(i)] = 0
        sixnine+=N.count(i)

if sixnine % 2 == 0:
    sixnine= sixnine//2
else:
    sixnine = sixnine//2 + 1
big = max(frequency)
answer = max(big, sixnine)

print(answer)
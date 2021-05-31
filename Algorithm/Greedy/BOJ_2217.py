N = int(input())
rope = []

for i in range(N):
    rope.append(int(input()))
rope=sorted(rope,reverse=True)
answer = 0
for i in range(N):
    if answer < rope[i]*(i+1):
        answer = rope[i]*(i+1)

print(answer)


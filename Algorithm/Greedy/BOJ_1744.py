N = int(input())
positive = []
negative = []
one = []
for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    else:
        one.append(num)

positive.sort(reverse=True)
negative.sort()


answer = 0
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        answer += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        answer+=positive[i] * positive[i+1]
    answer+=positive[len(positive)-1]

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        answer += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        answer+=negative[i] * negative[i+1]
    answer+=negative[len(negative)-1]

answer += sum(one)
print(answer)
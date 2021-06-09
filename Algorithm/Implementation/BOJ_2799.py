import sys

M, N = map(int, sys.stdin.readline().strip().split())

type = [1, 2, 3, 4, 5]
apartment = []
answer = [0] * 5
for i in range(5 * M + 1):
    line = sys.stdin.readline().strip()
    for c in line:
        apartment.append(c)

def fillWithHash(index):
    for i in range(4):
        apartment[index + i] = '#'

def blind(index):
    count = 0
    for i in range(4):
        if apartment[index] == '*':
            count += 1
            fillWithHash(index)
        else:
            fillWithHash(index)
        index += 5 * N + 1
    return count

for idx in range(len(apartment)):
    if apartment[idx] == '#':
        continue
    else:
        status = blind(idx)
        answer[status] += 1

for i in answer:
    print(i, end=' ')
import heapq

q = []
ordered_list = []
for i in range(2):
    n = int(input())
    lst = list(map(int, input().split()))
    for i in lst:
        heapq.heappush(q, i)

while len(q) > 0:
    ordered_list.append(heapq.heappop(q))

for i in ordered_list:
    print(i, end=' ')
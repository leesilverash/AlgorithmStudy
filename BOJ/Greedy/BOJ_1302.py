import sys

n = int(sys.stdin.readline().rstrip())
dic = {}
for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

mostSold = max(dic.values())
bestSellers = []
for book, count in dic.items():
    if mostSold == count:
        bestSellers.append(book)
print(sorted(bestSellers)[0])


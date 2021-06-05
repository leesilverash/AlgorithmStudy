a = list(input())
b = list(input())
total = len(a)+len(b)
intersection = list(set(a) & set(b))
duplicated = 0
for i in intersection:
    duplicated += (min(a.count(i),b.count(i)))*2
print(total-duplicated)
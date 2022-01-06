cards = [i for i in range(1,21)]

def reverseCard(a,b):
    x = a-1
    y = b-1
    while x < y:
        tmpX = cards[x]
        cards[x] = cards[y]
        cards[y] = tmpX
        x +=1
        y -=1

for i in range(10):
    a,b = map(int, input().split())
    reverseCard(a,b)

for i in cards:
    print(i, end=' ')

# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20
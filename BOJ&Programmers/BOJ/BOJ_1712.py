a, b, c = input().split()

cost = a
print(cost)
i = int(1)
price = 0
BP = int(0)
while True:
    cost = cost+(b*i)
    price *= i
    if cost > price:
        i = i + 1
        BP= BP + 1
    else:
        print(BP)
        break

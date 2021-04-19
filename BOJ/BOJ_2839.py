n = int(input())
x,y = 5,3
count = 0
while True:
    if (n % 5) == 0:
        count = count + (n//x)
        print(count)
        break
    n = n -3
    count += 1
    if n < 0:
        print("-1")
        break
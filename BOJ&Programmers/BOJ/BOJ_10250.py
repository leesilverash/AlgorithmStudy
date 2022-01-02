#ACM HOTEL
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = 0
    roomNum = 0
    if N % H == 0:
        floor = H*100
        roomNum = N // H
    else:
        floor = (N % H) * 100
        roomNum = 1 + N // H
    print(floor+roomNum)



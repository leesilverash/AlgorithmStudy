# 동전 거스름돈 문제
# 10, 50, 100, 500원 동전들을 무한하게 갖고있다. 손님에게 거스름돈을 거슬러주려고 할 때 동전을 최소한으로 주는 방법은?

# price = 물건 가격, money = 사용자가 낸 금액

def solution(money, price):
    coins = [500, 100, 50, 10]
    exchange = money - price
    count = 0
    idx = 0
    while exchange != 0:
        cnt = exchange // coins[idx]
        if cnt > 0:
            count+=cnt
            exchange = exchange % coins[idx]
        if idx < len(coins) -1:
            idx += 1
    return count

price = int(input('물건 가격:'))
money = int(input('사용자가 낸 금액:'))

print(solution(money, price))
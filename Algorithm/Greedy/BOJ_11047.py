N, K = map(int, input().split())
coin_list = []
for i in range(N):
    coin_list.insert(0, int(input()))

def coin(num):
    answer = 0
    i = 0
    while num != 0:
        answer += num//coin_list[i]
        num %= coin_list[i]
        i+=1
    return answer

print(coin(K))

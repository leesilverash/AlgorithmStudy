N = int(input())
answer =[]
def isPrime(num):
    if num==1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num% i == 0:
            return False
        return True


for i in range(2, N):
    if N % i == 0:
        print(N, i)
        N = N%i
        answer.append(i)
        i = 2

        continue
    else:
        print('else',N, i)
        continue

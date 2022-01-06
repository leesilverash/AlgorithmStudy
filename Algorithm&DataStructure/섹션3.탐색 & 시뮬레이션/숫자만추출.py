# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
# 만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.즉첫자리0은자연수화할때무시합니다. 출력은120를출력하고,다음줄에120 의 약수의 개수를 출력하면 됩니다.
# 추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

def extractNumber(str):
    ans = ''
    for i in str:
        if i.isnumeric():
            ans+=i
    return int(ans)

def getDivisorNumber(num):
    ans = 0
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            ans+=1
    return ans*2
str = input()
num = extractNumber(str)
divisor = getDivisorNumber(num)

print(num)
print(divisor)
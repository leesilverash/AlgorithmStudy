# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용 해서 출력해야 합니다.

n = int(input())

def convert(x):
    if x == 0:
        return
    else:
        convert(x//2)
        print(x%2, end='')
convert(n)

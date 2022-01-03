# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.

n,m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    for j in range(1, m+1):
        num = i + j
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
lst = sorted(dic.items(),key = lambda x: x[1], reverse=True)

val = lst[0][1]
answer = []
for i in range(len(lst)):
    if lst[i][1] != val:
        break
    else:
        print(lst[i][0], end=' ')







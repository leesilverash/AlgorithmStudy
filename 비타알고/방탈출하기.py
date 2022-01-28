# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

# 딕셔너리를 이용한 풀이법

# dict = {}
# lst1.sort()
# for i in range(user_input):
# 	dict[lst1[i]] = 1
# user_input2 = int(input())
# m = list(map(int, input().split()))

# for i in range(user_input2):
# 	if lst2[i] not in dict:
# 		print(0)
# 	else:
# 		print(1)


# 이분 탐색을 이용한 풀이법
for i in range(m):
    lt = 0
    rt = n - 1

    # 찾을 숫자
    find = lst2[i]

    answer = 0

    while lt <= rt:
        # 중앙 값 인덱스
        mid = (lt + rt) // 2
        if lst1[mid] == find:
            answer = 1
            break
        else:
            if find <= lst1[mid]:
                rt = mid - 1
            else:
                lt = mid + 1

    print(answer)



import sys

n = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().strip().split()))
stack = []
answer = [-1]*n

for i in range(n):
    if stack:
        if num[stack[-1]] >= num[i]:
            stack.append(i)
        else:
            while stack and num[stack[-1]] < num[i]:
                temp = stack.pop()
                answer[temp] = num[i]
            stack.append(i)
    else:
        stack.append(i)
for i in answer:
    print(i, end= ' ')


# 시간 초과 케이스
# n = int(sys.stdin.readline().strip())
# A = list(map(int,sys.stdin.readline().strip().split()))
# result = []
#
# for left in range(len(A)-1):
#     right = left+1
#     count = 0
#     while right < len(A):
#         if A[left] < A[right]:
#             count += 1
#             result.append(A[right])
#             break
#         else:
#             right+=1
#     if count == 0:
#         result.append(-1)
# result.append(-1)
#
# for i in result:
#     print(i, end=' ')















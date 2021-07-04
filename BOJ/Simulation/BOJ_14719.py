import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, len(lst) - 1
l_max, r_max = lst[left], lst[right]
answer = 0

while left < right:
    l_max = max(lst[left], l_max)
    r_max = max(lst[right], r_max)
    if l_max <= r_max:
        answer += l_max - lst[left]
        left += 1
    else:
        answer += r_max - lst[right]
        right -= 1
print(answer)

def solution(nums):
    answer = 0
    myList = set(nums)
    if len(nums)/2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums)/2
    return answer

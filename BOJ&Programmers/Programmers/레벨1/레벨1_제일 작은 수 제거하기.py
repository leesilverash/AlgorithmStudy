def solution(arr):
    answer = [i for i in arr if i > min(arr)]
    return answer if answer else [-1]
def isPrime(num):
    for i in range(3, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    lst = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                lst.append(nums[i] + nums[j] + nums[k])
    for i in lst:
        if isPrime(i):
            answer += 1
    print(answer)

    return answer
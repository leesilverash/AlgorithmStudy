def solution(numbers, hand):
    answer = ''
    L = [1, 4, 7]
    R = [3, 6, 9]
    left = 10
    right = 12

    def getDistance(absNum):
        return absNum // 3 + absNum % 3

    for i in numbers:
        if i in L:
            left = i
            answer+='L'
        elif i in R:
            right = i
            answer+='R'
        else:
            if i == 0:
                i = 11
            absL = abs(i-left)
            absR = abs(i-right)
            if getDistance(absL) < getDistance(absR):
                left = i
                answer += 'L'
            elif getDistance(absL) > getDistance(absR) :
                right = i
                answer += 'R'
            elif getDistance(absL) == getDistance(absR) :
                if hand == 'left' :
                    left = i
                    answer += 'L'
                else :
                    right = i
                    answer += 'R'
    return answer
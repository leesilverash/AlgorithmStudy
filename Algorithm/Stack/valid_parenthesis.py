# s는 괄호 - [ { ( ) } ]로만 이루어져있는 문자열이다.
# 해당 문자열의 괄호들이 올바르게 짝지어있는 지를 판별하라.
# 만약 올바르다면 True 아니라면 False를 출력하라.

s = input()
answer = True
def isValid(s):
    opening = "{[("                                 # 여는 괄호
    closing = "}])"                                 # 닫는 괄호
    brackets = {')': '(', '}': '{', ']': '['}       # 괄호들의 짝을 dictionary에 저장하여 사용
    stack = []
    for char in s:
        if char in opening:                         # 괄호가 여는 괄호라면 스택에 집어넣는다.
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:                     # 닫는 괄호이지만 비교해야 할 스택이 비어있다면 False
                return False
            if stack[-1] == brackets[char]:         # 스택의 탑과 char의 짝( brackets[char] )이 일치하다면 pop
                stack.pop()
            else:
                return False                        # 스택의 탑과 char의 짝이 일치하지 않다면 False
    return len(stack) == 0                          # 스택이 비어있다면 True, 아니면 False

print(isValid(s))
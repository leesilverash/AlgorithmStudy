n = int(input())
stack = []
result = []
isValid=True
count = 0

for i in range(n):
    number = int(input())
    while count < number:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1]==number:
        stack.pop()
        result.append("-")
    else:
        isValid = False
        exit(0)

if isValid==False:
    print("NO")
else:
    print("\n".join(result))
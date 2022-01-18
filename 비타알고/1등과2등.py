import sysgit

n = sys.stdin.readline().rstrip()

# 방법 1

answer = False
tmp = n.replace('21','x',1).replace('12','x',1)
tmp1 = n.replace('12','x',1).replace('21','x',1)

if tmp.count('x') == 2 or tmp1.count('x') == 2:
	answer= True
print('Yes') if answer is True else print('No')



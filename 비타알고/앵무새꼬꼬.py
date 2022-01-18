import re

n = int(input())
lst = [input() for _ in range(n)]
for i in lst:
	lst = re.findall('[aeiouAEIOU]', i)
	if len(lst) == 0:
		print('???')
	else:
		print(''.join(lst))






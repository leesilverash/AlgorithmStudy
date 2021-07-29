import sys

n = int(sys.stdin.readline().rstrip())
company = {}
for i in range(n):
    name, status = map(str, sys.stdin.readline().rstrip().split())
    if name in company:
        del(company[name])
    else:
        company[name] = 1

for name in company.items():
    print(name[0])
ans = sorted(company.items(), reverse=True)
for i in ans:
    print(i[0])

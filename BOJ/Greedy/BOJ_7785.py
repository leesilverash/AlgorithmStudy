import sys

n = int(sys.stdin.readline().rstrip())
company = {}
for i in range(n):
    name, status = map(str, sys.stdin.readline().rstrip().split())
    if name in company:
        del(company[name])
    else:
        company[name] = 1

ans = sorted(company.items(), reverse=True)
for i in ans:
    print(i[0])
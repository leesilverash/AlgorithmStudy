from itertools import combinations
lst = [int(input()) for _ in range(9)]
# lst.sort()
# for comb in combinations(lst, 7):
#     if sum(comb) == 100:
#         for i in comb:
#             print(i)
#         break

for i in lst:
    for j in lst:
        if i != j and sum(lst) - i - j == 100:
            lst.remove(i)
            lst.remove(j)
            break
for i in sorted(lst):
    print(i)




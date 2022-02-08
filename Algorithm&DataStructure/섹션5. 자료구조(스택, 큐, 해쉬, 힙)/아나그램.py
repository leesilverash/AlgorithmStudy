# x = input()
# y = input()
# x_dic = {}
# y_dic = {}
# answer = True
# for i in range(len(x)):
#     if x[i] not in x_dic:
#         x_dic[x[i]] = 1
#     elif x[i] in x_dic:
#         x_dic[x[i]] += 1
#
#     if y[i] not in y_dic:
#         y_dic[y[i]] = 1
#     elif y[i] in y_dic:
#         y_dic[y[i]] += 1
#
# for k, v in x_dic.items():
#     if y_dic[k] != v:
#         answer = False
#         break
#
# print('YES') if answer is True else print('NO')

x = input()
y = input()
dic = {}
answer = True
for i in x:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in y:
    if i not in dic:
        answer = False
        break
    else:
        dic[i] -= 1

for v in dic.values():
    if v != 0:
        answer = False

print('YES') if answer is True else print('NO')

# AbaAeCe
# baeeACA

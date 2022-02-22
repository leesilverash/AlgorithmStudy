lst1 = []
lst2 = []
lst3 = []
def DFS(v):
    if v > 7:
        return
    else:
        lst1.append(v)
        DFS(v*2)
        lst2.append(v)
        DFS(v*2+1)
        lst3.append(v)

DFS(1)

print('전위순회 출력 :', end=' ')
for i in lst1:
    print(i, end= ' ')
print()
print('전위순회 출력 :', end=' ')
for i in lst2:
    print(i, end=' ')
print()
print('후위순회 출력 :', end=' ')
for i in lst3:
    print(i, end= ' ')

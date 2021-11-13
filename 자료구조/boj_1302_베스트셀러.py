n = int(input())

dict = {}

for _ in range(n):
    book = input()
    if book in dict:
        dict[book]+=1
    else:
        dict[book] = 1

lst = [(k,v) for k,v in dict.items()]
filteredList = sorted(list(filter(lambda x:x[1] == max(dict.values()), lst)), key = lambda x: x[0])
print(filteredList[0][0])




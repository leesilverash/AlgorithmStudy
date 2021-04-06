natural_num = set(range(1,10001))
generated_num = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
        generated_num.add(i)


self_num = natural_num - generated_num

print(self_num)


natural_number_set = set(range(1, 1001))
generated_number_set = set()

for i in range(1, 1001):
    for j in str(i):
        i += int(j)
    generated_number_set.add(i)
    print()

self_numbers_set = natural_number_set - generated_number_set
for self_num in sorted(self_numbers_set):
    print(self_num)

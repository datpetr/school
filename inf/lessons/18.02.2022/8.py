from itertools import permutations


s = set(list(permutations('НАСТЯ', 6)))
count = 0

for i in s:
    if i.count('А') <= 1 and i.count('Я') <= 1:
        count += 1

print(count)

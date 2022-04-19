from itertools import product


a = set(list(product('АБВГДЕ', repeat=7)))

count = 0

for j in a:
    i = ''.join(j)
    if i.count('Е') == 1 and ((i[-1] == 'Б' and i.count('Б') == 1) or 'Б' not in i):
        count += 1

print(count)

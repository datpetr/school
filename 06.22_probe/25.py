from itertools import product

a = [126789]
for i in range(10):
    a.append(int('12' + str(i) + '6789'))

for i in range(10):
    for j in range(10):
        a.append(int('12' + str(i) + str(j) + '6789'))


a.sort()
for i in a:
    if i % 39 == 0:
        print(i, i // 39)

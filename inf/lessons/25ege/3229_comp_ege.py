a = []

for i in range(10):
    for j in range(10):
        a.append(int('12345' + str(i) + '6' + str(j) + '8'))

a.sort()
for i in a:
    if i % 17 == 0:
        print(i, i // 17)

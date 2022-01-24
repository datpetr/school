from random import randint as ran

a = []

for i in range(ran(1, 10000)):
    a.append(ran(-100000000000000, 10000000000000000))

n = len(a)

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            break

print(a)

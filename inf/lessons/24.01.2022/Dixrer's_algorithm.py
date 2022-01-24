from random import randint as ran

n = 6
w = []

for i in range(n):
    w.append([0] * n)

for i in range(n):
    for j in range(i):
        w[i][j] = ran(-1000, 1000)

print(w)

active = [True] * n
r = w[0][:]
p = [0] * n
active[0] = False
p[0] = -1

for i in range(n - 1):
    minDist = 1e10
    for j in range(n):
        if active[j] and r[j] < minDist:
            minDist = r[j]
            kMin = j
    active[kMin] = False
    for j in range(n):
        if r[kMin] + w[kMin][j] < r[j]:
            r[j] = r[kMin] + w[kMin][j]
            p[j] = kMin

print(r[-1])

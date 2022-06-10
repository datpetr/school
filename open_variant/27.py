from itertools import accumulate


f = list(map(int, open('files/27_A.txt', 'r').readlines()))

n = f.pop(0)
a = f
f = a + f
pr = [0] + list(accumulate(f))
s = sum(min(j, n - j) * f[j] * 3 for j in range(n))
ms = s

for i in range(1, n):
    s = s - (pr[i + n // 2] - pr[i]) + (pr[i + n] - pr[i + n // 2])
    ms = min(ms, s)

print(ms * 3)

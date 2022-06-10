from itertools import accumulate

with open('files/27_B.txt') as f:
    n = int(f.readline())
    m = [int(f.readline()) for _ in range(n)] * 2
    c = 3

pr = [0] + list(accumulate(m))
ms = 10 ** 100
s = sum([min(n - k, k) * m[k] * c for k in range(n)])

for i in range(1, n):
    s = s - (pr[i + n // 2] - pr[i]) + (pr[i + n] - pr[i + n // 2])
    ms = min(s, ms)

print(ms)

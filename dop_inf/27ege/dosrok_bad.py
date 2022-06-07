f = list(map(int, open('files/27-A.txt', 'r').readlines()))
n = f.pop(0)

min_sum = bestPos = 10 ** 10

for pos in range(n):
    s = 0
    for i in range(n):
        dist = min(abs(i - pos), n - abs(i - pos))
        s += f[i] * dist
    if s < min_sum:
        min_sum = s
        bestPos = pos

print(bestPos + 1, min_sum)

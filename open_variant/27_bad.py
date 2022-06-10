f = list(map(int, open('files/27_A.txt', 'r').readlines()))

n = f.pop(0)

costs = []

for i in range(n):
    s = sum(min(abs(i - j), n - abs(i - j)) * f[j] * 3 for j in range(n))
    costs.append(s)

print(min(costs), costs.index(min(costs)) + 1)

f = open('files/26.txt')

n = int(f.readline())

a = []
r, m = 0, 0

for _ in range(n):
    pair = list(map(int, f.readline().split()))
    pair[1] = -pair[1]
    a.append(pair)

a.sort()
print(a)

for i in range(1, n):
    if a[i][0] == a[i - 1][0]:
        if a[i][1] - a[i - 1][1] == 3:
            r = a[i][0]
            m = -a[i][1] + 1

print(r, m)

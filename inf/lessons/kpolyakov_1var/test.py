f = open('files/26.txt')

n = int(f.readline())

a = []
r, m = 0, 0

for _ in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort(key=lambda k: [k[0], -k[1]])

for i in range(n - 1):
    if a[i][0] == a[i + 1][0]:
        if a[i][1] - a[i + 1][1] == 3:
            r = a[i][0]
            m = a[i + 1][1] + 1

print(r, m)

f = open('files/3230.txt', 'r')

n = int(f.readline())
a = []
mx_r = mn_pos = 0
for _ in range(n):
    a.append(list(map(int, f.readline().split())))

f.close()

a.sort(key=lambda x: (x[0], -x[1]))
print(a)

for i in range(n - 1):
    if (a[i + 1][0] == a[i][0]) and (a[i][1] == a[i + 1][1] + 12):
        mx_r = a[i + 1][0]
        mn_pos = a[i + 1][1] + 1

print(mx_r, mn_pos)

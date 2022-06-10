f = open('files/26.txt', 'r')

n = int(f.readline())
a = []
mx_row = mn_place = 0

for _ in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort(key=lambda x: (x[0], -x[1]))
print(a)
for i in range(n - 1):
    if a[i][0] == a[i + 1][0] and (a[i][1] - a[i + 1][1] == 14):
        mx_row = a[i][0]
        mn_place = a[i + 1][1] + 1

print(mx_row, mn_place)

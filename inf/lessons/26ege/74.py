f = open('files/26-73.txt', 'r')

n = int(f.readline())
a = []
mx_row = count_current = mx = 0

for _ in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort()

for i in range(n - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] + 2 == a[i + 1][1]:
        count_current += 1
    else:
        if a[i][1] != a[i + 1][1]:
            if mx < count_current:
                mx = count_current
                mx_row = a[i][0]
            count_current = 0

print(mx + 1, mx_row)

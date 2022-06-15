f = open('files/26.txt', 'r')

n = int(f.readline())
mx_length, mx_row, count = 0, 0, 1
a = []

for _ in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort()
print(a)
for i in range(n - 1):
    if a[i][0] == a[i + 1][0] and a[i][1] == a[i + 1][1]:
        continue
    elif a[i][0] == a[i + 1][0] and a[i][1] + 1 == a[i + 1][1]:
        count += 1
    else:
        if count > mx_length:
            mx_row = a[i][0]
            mx_length = count
        count = 1

print(mx_length, mx_row)
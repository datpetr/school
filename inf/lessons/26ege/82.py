f = open('files/26-82.txt', 'r')

n = int(f.readline())
a = []
mx_row = count_even = mx_count_even = 0

for _ in range(n):
    a.append(list(map(int, f.readline().split())))

f.close()
a.sort()

for i in range(n - 1):
    if a[i][0] == a[i + 1][0]:
        if a[i][1] % 2 == 0:
            count_even += 1
    else:
        if a[i][1] % 2 == 0:
            count_even += 1
        if i == n - 1 and a[i + 1][1] % 2 == 0:
            count_even += 1
        if count_even > mx_count_even:
            mx_count_even = count_even
            mx_row = a[i][0]
        count_even = 0


print(mx_count_even, mx_row)

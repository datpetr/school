f = list(map(int, open('files/2710.txt', 'r').readlines()))

count = 0
mx_difference = 0

for i in range(1, len(f) - 1):
    if f[i] < f[i - 1] and f[i] < f[i + 1]:
        count += 1
        mx_difference = max(mx_difference, f[i - 1] - f[i])
        mx_difference = max(mx_difference, f[i + 1] - f[i])


if f[0] < f[1]:
    count += 1
    mx_difference = max(mx_difference, f[1] - f[0])
if f[-1] < f[-2]:
    count += 1
    mx_difference = max(mx_difference, f[-1] - f[-2])

print(count, mx_difference)

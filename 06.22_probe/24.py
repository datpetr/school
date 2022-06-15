f = open('files/24_2.txt', 'r').readline()

count, mx = 0, 0
for j in range(2):
    for i in range(j, len(f) - 1, 2):
        if f[i] + f[i + 1] == 'BB' or f[i] + f[i + 1] == 'DD':
            count += 1
            mx = max(mx, count)
        else:
            count = 0

print(mx)

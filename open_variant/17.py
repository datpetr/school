f = list(map(int, open('files/17.txt', 'r').readlines()))

mn_elem = 100_000 + 1
mx_pair = count = 0

for i in f:
    if i % 21 == 0 and i < mn_elem:
        mn_elem = i

for i in range(len(f) - 1):
    if f[i] % mn_elem == 0 or f[i + 1] % mn_elem == 0:
        count += 1
        if f[i] + f[i + 1] > mx_pair:
            mx_pair = f[i] + f[i + 1]

print(count, mx_pair)
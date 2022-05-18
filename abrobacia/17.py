f = list(map(int, open('files/17.txt', 'r').readlines()))

mn = max(f) + 1
count = 0
mx_pair = 0

for i in f:
    if i % 6 == 0 and i < mn:
        mn = i

for i in range(len(f) - 1):
    if f[i] % mn == 0 and f[i + 1] % mn == 0:
        count += 1
        if f[i] + f[i + 1] > mx_pair:
            mx_pair = f[i] + f[i + 1]

print(count, mx_pair)

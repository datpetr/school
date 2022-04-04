f = list(map(int, open('files/2937.txt', 'r').readlines()))

count = 0
mx_pair = 0
mx_elem = 0

for i in f:
    if i % 11 == 0 and i > mx_elem:
        mx_elem = i

for i in range(len(f) - 1):
    if (f[i] % 11 == 0 or f[i + 1] % 11 == 0) and ((f[i] + f[i + 1]) <= mx_elem):
        count += 1
        if (f[i] + f[i + 1]) > mx_pair:
            mx_pair = (f[i] + f[i + 1])

print(count, mx_pair)

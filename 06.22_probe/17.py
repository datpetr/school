f = list(map(int, open('files/17.txt', 'r').readlines()))

mx_elem_11 = 0

for i in f:
    if i % 11 == 0 and i > mx_elem_11:
        mx_elem_11 = i

count = 0
mn_pair = 200_001

for i in range(len(f) - 1):
    if f[i] > mx_elem_11 or f[i + 1] > mx_elem_11:
        count += 1
        if f[i] + f[i + 1] < mn_pair:
            mn_pair = f[i] + f[i + 1]


print(count, mn_pair)

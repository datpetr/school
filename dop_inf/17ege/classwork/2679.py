f = list(map(int, open('files/2679.txt', 'r').readlines()))

mx_elem = 0
mx_pair = 0
count = 0

for i in f:
    if i > mx_elem and str(i)[-1] == str(i)[-2]:
        mx_elem = i

for i in range(len(f) - 1):
    if ((f[i] % 5 == 0 or
         f[i] % 7 == 0 or
         f[i + 1] % 5 == 0 or
         f[i + 1] % 7 == 0)
            and (f[i] + f[i + 1] <=
                 mx_elem)):
        count += 1
        if f[i] + f[i + 1] > mx_pair:
            mx_pair = f[i] + f[i + 1]


print(count, mx_pair)

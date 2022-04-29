f = list(map(int, open('files/26.txt', 'r').readlines()))
n = f.pop(0)

a_even = []
count = mx_pair = 0

for i in range(n):
    if f[i] % 2 == 0:
        a_even.append(f[i])
print(len(a_even) ** 2)
for i in range(len(a_even)):
    for j in range(i + 1, len(a_even)):
        pair = (a_even[i] + a_even[j]) // 2

        if pair in f:
            count += 1
            if pair > mx_pair:
                mx_pair = pair

print(count, mx_pair)

def x_to_n(x, n):
    s = ''
    while x:
        s += str(x % n)
        x //= n
    return s[::-1]


x = 5 * (216 ** 3031) + 4 * (36 ** 3042) - 3 * (6 ** 3053) - 3064
count = 0
n_6 = x_to_n(x, 6)
for i in n_6:
    count += int(i)

print(count)
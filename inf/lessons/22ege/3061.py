def f(x, y):
    while x != y:
        if x < y:
            x -= y
        else:
            y -= x

    return x


count = 0
for x in range(1019, 10000000, 1019):
    for y in range(1019, 10000000, 1019):
        if f(x, y) == 1019:
            count += 1

print(count)

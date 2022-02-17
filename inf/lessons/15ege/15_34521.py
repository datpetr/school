max_a = 0

for x in range(1000):
    for a in range(1000):
        if (int(bin(x)[2:]) & int(bin(51)[2:])) == 0 or (((int(bin(x)[2:]) & int(bin(41)[2:]) == 0) <= (int(bin(x)[2:]) & int(bin(a)[2:] == 0)))):
            if a > mx_a:
                mx_a = a
print(mx_a)

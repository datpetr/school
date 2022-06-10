def f(n):
    r = bin(n)[2:]

    if int(r) % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'

    return int(r, 2)


print(f(4), f(5))
for n in range(10000):
    if f(n) > 441:
        print(n)
        break

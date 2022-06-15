def f(n):
    r = bin(n)[2:]
    if int(r) % 2 == 0:
        r = '10' + r + '10'
    else:
        r = '1' + r + '00'

    return int(r, 2)


a = []
for i in range(1000):
    s = f(i)
    if s > 100:
        a.append(s)

print(min(a))

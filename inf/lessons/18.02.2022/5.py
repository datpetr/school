def f(numb):
    n = numb
    if n % 2 == 0:
        n //= 2
    else:
        n -= 1

    if n % 3 == 0:
        n //= 3
    else:
        n -= 1

    if n % 5 == 0:
        n //= 5
    else:
        n -= 1

    return n


count = 0

for i in range(10000):
    if f(i) == 1:
        count += 1

print(count)

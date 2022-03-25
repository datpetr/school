def ege25(x):
    t = int(x ** 0.5)
    a = {1, x}

    for i in range(2, t + 1):
        if len(a) > 4:
            return a
        if x % i == 0:
            a.add(i)
            a.add(x // i)
    return sorted(a)


for i in range(185311, 185331):
    n = ege25(i)
    if n:
        print(*n)

def ege25(x):
    t = int(x ** 0.5)
    a = []

    for i in range(1, t + 1):
        if x % i == 0:
            a.append(i)
            j = x // i
            if x != i:
                a.append(j)
    return sorted(a)


for i in range(185311, 185331):
    n = ege25(i)
    if len(n) == 4:
        print(*n)

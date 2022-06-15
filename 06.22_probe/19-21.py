def f(a, b, c, m):
    if a + b >= 300:
        return c % 2 == m % 2

    if c == m:
        return 0

    h = [f(a + 3, b, c + 1, m),
         f(a * 2, b, c + 1, m),
         f(a, b + 3, c + 1, m),
         f(a, b * 2, c + 1, m)]

    return any(h) if c % 2 != m % 2 else all(h)


for s in range(1, 280):
    for m in range(1, 6):
        if f(20, s, 0, m):
            if m == 5:
                print(s, m)
            break

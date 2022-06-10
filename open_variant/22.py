for i in range(10000):
    x = i
    q = 8
    p = 10
    k1 = 0
    k2 = 0

    while x <= 100:
        k1 = k1 + 1
        x = x + p

    while x >= q:
        k2 = k2 + 1
        x = x - q

    l = x + k1
    m = x + k2

    if l == 12 and m == 19:
        print(i)

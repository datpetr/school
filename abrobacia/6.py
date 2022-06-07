for i in range(10000):
    s = i
    s = (s - 21) // 10
    n = 1
    while s > 0:
        n *= 2
        s -= n
    if n == 16:
        print(i)
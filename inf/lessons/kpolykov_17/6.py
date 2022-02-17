for i in range(1000):
    s = i
    n = 1
    while s < 54:
        s = s + 7
        n = n * 3
    if n == 243:
        print(i)

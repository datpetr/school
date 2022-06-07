for i in range(300, 1000000):
    x = i
    a = 5 * x + 345
    b = 5 * x - 807
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 96:
        print(i)
        break

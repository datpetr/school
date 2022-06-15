def dell(m, n):
    return m % n == 0


for a in range(70, 1000):
    for x in range(1000):
        if not(((not dell(x, 15)) or (not dell(x, 28)) or dell(x, a)) and (a > 70)):
            break
    else:
        print(a)
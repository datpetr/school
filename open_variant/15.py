def dell(n, m):
    return n % m == 0


for a in range(1, 1000):
    for x in range(1, 1000):
        if not ((dell(x, 3) <= (not dell(x, 5))) or (x + a >= 90)):
            break
    else:
        print(a)
        break

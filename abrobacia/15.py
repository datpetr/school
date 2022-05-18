def dell(a):
    for x in range(1, 10000):
        if not (((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 90)):
            return False
    return True


for a in range(1, 10000):
    if dell(a):
        print(a)
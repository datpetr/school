A = 1

while True:
    for x in range(1, 100000):
        if not(((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & A != 0))):
            break
    else:
        print(A)
        break
    A += 1

A = 1

while True:
    for x in range(1, 100000):
        if not((x & 49 != 0) <= ((x & 41 == 0) <= (x & A != 0))):
            break
    else:
        print(A)
        break
    A += 1

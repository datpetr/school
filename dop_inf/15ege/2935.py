a = 1

while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((2 * y + 3 * x != 135) or (y > a) or (x > a)):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1

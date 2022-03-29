a = 1

while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x * y < 2 * a) or (x >= 11) or (x < 2 * y)):
                break
        else:
            continue
        break
    else:
        print(a)

    a += 1

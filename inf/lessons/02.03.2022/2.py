A = 1

while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((y + 2 * x < A) or (x > 30) or (y > 20)):
                break
        else:
            continue
        break
    else:
        print(A)
        break
    A += 1

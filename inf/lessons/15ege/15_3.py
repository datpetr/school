for A in range(10000, 1, -1):
    flag = True

    for x in range(10000):
        if ((x & 51 == 0) or (x & 41 != 0) or (x & A == 0)) == 0:
            flag = False
            break

    if flag:
        print(A)
        break

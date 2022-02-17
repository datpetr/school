flag = False

for a in range(10000, 1, -1):
    for x in range(1, 1000):
        if not((not (x % a == 0)) <= ((x % 6 == 0) <= (not (x % 4 == 0)))):
            print(a)
            flag = True
            break
    if flag:
        break


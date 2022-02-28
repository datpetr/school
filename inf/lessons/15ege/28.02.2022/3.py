# x&77 ≠ 0 → (x&12 = 0 → x&А ≠ 0)
# min a

a = 1
while True:
    for x in range(1, 1000):
        if not((x & 77 != 0) <= ((x & 12 == 0) <= (x & a != 0))):
            break
    else:
        print(a)
        break
    a += 1

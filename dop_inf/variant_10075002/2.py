print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                constant = (((x <= y) and (z or w)) <= ((x == w) or (y and (not z))))
                if not constant:
                    print(x, y, z, w, constant)

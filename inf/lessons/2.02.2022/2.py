print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                expression = x and (not y) and ((not z) or w)
                if expression:
                    print(x, y, z, w)

print('a b c d F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a and b) == (not(c))) and (b <= d):
                    print(a, b, c, d)

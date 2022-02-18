count = 0

for a1 in 'НАСТЯ':
    for a2 in 'НАСТЯ':
        for a3 in 'НАСТЯ':
            for a4 in 'НАСТЯ':
                for a5 in 'НАСТЯ':
                    for a6 in 'НАСТЯ':
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if s.count('А') <= 1 and s.count('Я') <= 1:
                            count += 1

print(count)

def solution():
    a = int(input('input value a: '))
    b = int(input('input value b: '))
    c = int(input('input value c: '))

    res = []

    d = b ** 2 - 4 * a * c

    print('d = b ** 2 - 4ac = {}'.format(d))
    print(f'{a}x^2 + {b}x + {c} = 0')

    if d > 0:
        res.append((-b + d ** 0.5) / (2 * a))
        res.append((-b - d ** 0.5) / (2 * a))
        print(f'(-{b} + {d} ** 0.5) / (2 * {a}) = {res[0]}')
        print(f'(-{b} + {d} ** 0.5) / (2 * {a}) = {res[1]}')
        return f'x1 = {res[0]}; x2 = {res[1]}'
    if d == 0:
        res.append((-b) / 2 * a)
        print(f'(-{b} / (2 * {a}) = {res}')
        return f'x = {res}'
    else:
        return 'd < 0 that is, there are no solutions'


print(solution())
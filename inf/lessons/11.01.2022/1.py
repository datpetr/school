def x_to_n(x, n):
    st = ""
    dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    while x:
        digit = x % n
        st += str(digit)
        x //= n

    return st[::-1]


def n_to_10(x, n):
    st = str(x)[::-1]
    k = []
    res = 0

    for i in range(len(st)):
        res += int(st[i]) * (n ** i)

    for i in range(len(st) - 1, -1, - 1):
        if i == 0:
            k.append('{} * {}^{}'.format(st[i], n, i))
            k.append(' = {}'.format(res))
        else:
            k.append('{} * {}^{} + '.format(st[i], n, i))
    for i in k:
        print(i, end='')
    print()
    return res


def x_to_any(x, n1, n2):
    if n1 == 10:
        return x_to_n(x, n2)
    else:
        return x_to_n(n_to_10(x, n1), n2)


x = int(input('please, enter the number you want to translate: '))
n1 = int(input('please, the numeral system of the entered number: '))
n2 = int(input('please, enter the number system you want to translate: '))

print(x_to_any(x, n1, n2))

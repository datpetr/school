def x_to_n(x, n):
    st = ""

    while x:
        digit = x % n
        st += str(digit)
        x //= n

    return int(st[::-1])


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


x = int(input('please, enter the number you want to translate: '))
n = int(input('please, enter the number system you want to translate: '))

func = (x_to_n(x, n))

print(func, n_to_10(func, n))

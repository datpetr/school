def f(n):
    n_2 = bin(n)[2:]
    n_2 += n_2[-1]

    if n_2.count('1') % 2 == 0:
        n_2 += '0'
    else:
        n_2 += '11'

    return int(n_2, 2)


for i in range(10000):
    n = f(i)
    print(i, bin(i)[2:], n, bin(n)[2:])
    if (len(bin(n)) - len(bin(i))) == 3:
        if n >= 90:
            print(n)
            break

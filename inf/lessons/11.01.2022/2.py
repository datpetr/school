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
    if x.isdigit():
        x = int(x)
        while x:
            digit = x % n
            if digit >= 10:
                st += dict[digit]
            else:
                st += str(digit)
            x //= n

    return st[::-1]


def n_to_10(x, n):
    st = str(x)[::-1]

    k = []
    res = 0

    dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    for i in range(len(st)):
        if st[i] in dict:
            res += int(dict[st[i]]) * (n ** i)
        else:
            res += int(st[i]) * (n ** i)

    return res


def x_to_any(x, n1, n2):
    if n1 == 10:
        return x_to_n(x, n2)
    else:
        return x_to_n(n_to_10(x, n1), n2)


x = input('please, enter the number you want to translate: ')
n1 = int(input('please, the numeral system of the entered number: '))
n2 = int(input('please, enter the number system you want to translate: '))

print(x_to_any(x, n1, n2))

from itertools import product


def x_to_n(x, n):
    s = ''
    while x:
        s += str(x % n)
        x //= n

    return s


for j in range(1, 10):
    for i in range(5):
        a = list(map(''.join, product('0123456789', repeat=i)))
        for elem in a:
            n = int('1' + elem + '586' + str(j) + '6')
            s = x_to_n(n, 7)
            if s[::-1] == s:
                count = 0
                for k in s:
                    count += int(k)
                print(n, count)
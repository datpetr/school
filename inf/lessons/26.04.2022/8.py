def x_to_n(x, n):
    s = ''
    while x:
        s += str(x % n)
        x //= n
    return s[::-1]


n = (16 ** 8) * (4 ** 20) - (4 ** 5) - 64
print(x_to_n(n, 4).count('3'))

def x_to_n(x, n):
    s = ''
    while x:
        s += str(x % n)
        x //= n
    return int(s[::-1])


print(x_to_n(10, 2))
n = int('30', 9) + int('75', 9) + int('32', 9)
print(x_to_n(n, 5))

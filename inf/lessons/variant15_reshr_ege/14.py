def x_to_n(x, n):
    st = ''
    while x:
        st += str(x % n)
        x //= n

    return st[::-1]


expression = 343 ** 5 + 7 ** 3 - 1

for x in range(1000):
    if x_to_n(expression - x, 7).count('6') == 12:
        print(x)
        break

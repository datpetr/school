def f(n):
    n_2 = bin(n)[2:]
    n_2 += n_2[-1]
    n_2 += str(n_2.count('1') % 2)
    return int(int(n_2, 2))


for i in range(1, 10000):
    n = f(i)
    if n > 105:
        print(n)
        break